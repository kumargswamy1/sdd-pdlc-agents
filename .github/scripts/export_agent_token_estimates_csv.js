#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');
const os = require('os');

function usage() {
  console.log('Usage: node .github/scripts/export_agent_token_estimates_csv.js [output.csv]');
  console.log('Optional env var: COPILOT_WORKSPACE_STORAGE (defaults to VS Code macOS path).');
}

function isObject(v) {
  return typeof v === 'object' && v !== null && !Array.isArray(v);
}

function safeJsonParse(line) {
  try {
    return JSON.parse(line);
  } catch {
    return null;
  }
}

function estimateTokensFromText(text) {
  if (!text) {
    return 0;
  }
  return Math.ceil(text.length / 4);
}

function collectText(value, out, allowRawString = false) {
  if (typeof value === 'string') {
    if (allowRawString) {
      out.push(value);
    }
    return;
  }
  if (Array.isArray(value)) {
    for (const item of value) {
      collectText(item, out, allowRawString);
    }
    return;
  }
  if (!isObject(value)) {
    return;
  }

  for (const [key, inner] of Object.entries(value)) {
    const k = key.toLowerCase();
    const likelyTextField =
      k.includes('prompt') ||
      k.includes('message') ||
      k.includes('content') ||
      k.includes('text') ||
      k.includes('response') ||
      k.includes('input') ||
      k.includes('output') ||
      k.includes('delta');

    if (likelyTextField) {
      collectText(inner, out, true);
    } else {
      collectText(inner, out, false);
    }
  }
}

function getActualUsage(record) {
  const usage = {
    input: 0,
    output: 0,
    total: 0,
    found: false,
  };

  function walk(v) {
    if (!v) {
      return;
    }
    if (Array.isArray(v)) {
      for (const item of v) {
        walk(item);
      }
      return;
    }
    if (!isObject(v)) {
      return;
    }

    const hasUsage = [
      'prompt_tokens',
      'completion_tokens',
      'input_tokens',
      'output_tokens',
      'total_tokens',
    ].some((f) => Number.isFinite(v[f]));

    if (hasUsage) {
      usage.found = true;
      usage.input += (Number(v.prompt_tokens) || 0) + (Number(v.input_tokens) || 0);
      usage.output += (Number(v.completion_tokens) || 0) + (Number(v.output_tokens) || 0);
      usage.total += Number(v.total_tokens) || 0;
    }

    for (const inner of Object.values(v)) {
      walk(inner);
    }
  }

  walk(record);

  if (usage.found && usage.total === 0) {
    usage.total = usage.input + usage.output;
  }

  return usage;
}

function csvEscape(value) {
  const v = String(value ?? '');
  if (v.includes(',') || v.includes('"') || v.includes('\n')) {
    return `"${v.replace(/"/g, '""')}"`;
  }
  return v;
}

function defaultWorkspaceStorage() {
  return path.join(
    os.homedir(),
    'Library',
    'Application Support',
    'Code',
    'User',
    'workspaceStorage'
  );
}

function findMainJsonlFiles(root) {
  const files = [];

  function walk(dir) {
    let entries;
    try {
      entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch {
      return;
    }

    for (const entry of entries) {
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        walk(full);
      } else if (entry.isFile() && entry.name === 'main.jsonl' && full.includes('GitHub.copilot-chat/debug-logs/')) {
        files.push(full);
      }
    }
  }

  walk(root);
  return files;
}

function analyzeMainJsonl(filePath) {
  const raw = fs.readFileSync(filePath, 'utf8');
  const lines = raw.split(/\r?\n/).filter((l) => l.trim().length > 0);

  let invalid = 0;
  let eventCount = 0;
  let estimatedTotal = 0;
  let actualInput = 0;
  let actualOutput = 0;
  let actualTotal = 0;
  let firstTs = null;
  let lastTs = null;

  for (const line of lines) {
    const record = safeJsonParse(line);
    if (!record) {
      invalid += 1;
      continue;
    }

    eventCount += 1;
    if (Number.isFinite(record.ts)) {
      firstTs = firstTs === null ? record.ts : Math.min(firstTs, record.ts);
      lastTs = lastTs === null ? record.ts : Math.max(lastTs, record.ts);
    }

    const textChunks = [];
    collectText(record, textChunks);
    estimatedTotal += estimateTokensFromText(textChunks.join('\n'));

    const usage = getActualUsage(record);
    actualInput += usage.input;
    actualOutput += usage.output;
    actualTotal += usage.total;
  }

  return {
    filePath,
    eventCount,
    invalidJsonLines: invalid,
    estimatedTotal,
    actualInput,
    actualOutput,
    actualTotal,
    hasActualUsage: actualTotal > 0 || actualInput > 0 || actualOutput > 0,
    firstTs: firstTs ?? '',
    lastTs: lastTs ?? '',
  };
}

function getWorkspaceAndSession(filePath) {
  const marker = `${path.sep}GitHub.copilot-chat${path.sep}debug-logs${path.sep}`;
  const idx = filePath.indexOf(marker);
  if (idx < 0) {
    return { workspaceId: '', sessionId: '' };
  }

  const left = filePath.slice(0, idx);
  const workspaceId = path.basename(left);

  const right = filePath.slice(idx + marker.length);
  const parts = right.split(path.sep);
  const sessionId = parts[0] || '';

  return { workspaceId, sessionId };
}

function estimateFromSessionResources(workspaceId, sessionId) {
  if (!workspaceId || !sessionId) {
    return { resourceFileCount: 0, resourceEstimatedTokens: 0 };
  }

  const base = path.join(
    defaultWorkspaceStorage(),
    workspaceId,
    'GitHub.copilot-chat',
    'chat-session-resources',
    sessionId
  );

  if (!fs.existsSync(base)) {
    return { resourceFileCount: 0, resourceEstimatedTokens: 0 };
  }

  let resourceFileCount = 0;
  let resourceEstimatedTokens = 0;

  function walk(dir) {
    let entries;
    try {
      entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch {
      return;
    }

    for (const entry of entries) {
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        walk(full);
      } else if (entry.isFile() && entry.name === 'content.txt') {
        resourceFileCount += 1;
        try {
          const txt = fs.readFileSync(full, 'utf8');
          resourceEstimatedTokens += estimateTokensFromText(txt);
        } catch {
          // Ignore unreadable resource file.
        }
      }
    }
  }

  walk(base);
  return { resourceFileCount, resourceEstimatedTokens };
}

function main() {
  if (process.argv.includes('-h') || process.argv.includes('--help')) {
    usage();
    process.exit(0);
  }

  const root = process.env.COPILOT_WORKSPACE_STORAGE || defaultWorkspaceStorage();
  const outputPath = path.resolve(process.argv[2] || 'output/copilot-token-estimates.csv');

  if (!fs.existsSync(root)) {
    console.error(`Workspace storage path not found: ${root}`);
    process.exit(2);
  }

  const files = findMainJsonlFiles(root);

  const rows = files.map((f) => {
    const analysis = analyzeMainJsonl(f);
    const ids = getWorkspaceAndSession(f);
    const resourceEstimate = estimateFromSessionResources(ids.workspaceId, ids.sessionId);
    const dataQuality =
      analysis.hasActualUsage
        ? 'ACTUAL_USAGE'
        : analysis.estimatedTotal > 0
          ? 'LOG_ESTIMATE_ONLY'
          : resourceEstimate.resourceEstimatedTokens > 0
            ? 'RESOURCE_ESTIMATE_ONLY'
            : 'NO_USABLE_TOKEN_DATA';
    return {
      workspace_id: ids.workspaceId,
      session_id: ids.sessionId,
      event_count: analysis.eventCount,
      invalid_json_lines: analysis.invalidJsonLines,
      estimated_total_tokens: analysis.estimatedTotal,
      resource_file_count: resourceEstimate.resourceFileCount,
      resource_estimated_tokens: resourceEstimate.resourceEstimatedTokens,
      actual_input_tokens: analysis.actualInput,
      actual_output_tokens: analysis.actualOutput,
      actual_total_tokens: analysis.actualTotal,
      has_actual_usage: analysis.hasActualUsage ? 'YES' : 'NO',
      data_quality: dataQuality,
      first_ts: analysis.firstTs,
      last_ts: analysis.lastTs,
      log_path: analysis.filePath,
    };
  });

  rows.sort((a, b) => b.estimated_total_tokens - a.estimated_total_tokens);

  const header = [
    'workspace_id',
    'session_id',
    'event_count',
    'invalid_json_lines',
    'estimated_total_tokens',
    'resource_file_count',
    'resource_estimated_tokens',
    'actual_input_tokens',
    'actual_output_tokens',
    'actual_total_tokens',
    'has_actual_usage',
    'data_quality',
    'first_ts',
    'last_ts',
    'log_path',
  ];

  const lines = [header.join(',')];
  for (const row of rows) {
    lines.push(header.map((h) => csvEscape(row[h])).join(','));
  }

  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  fs.writeFileSync(outputPath, `${lines.join('\n')}\n`, 'utf8');

  const withActual = rows.filter((r) => r.has_actual_usage === 'YES').length;

  console.log(`CSV written: ${outputPath}`);
  console.log(`Sessions scanned: ${rows.length}`);
  console.log(`Sessions with actual usage: ${withActual}`);
  console.log(`Sessions estimate-only: ${rows.length - withActual}`);
}

main();
