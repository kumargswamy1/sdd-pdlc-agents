#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');

function usage() {
  console.log('Usage: node .github/scripts/estimate_agent_loop_tokens.js <path-to-main.jsonl>');
  console.log('Example: node .github/scripts/estimate_agent_loop_tokens.js "$HOME/.../debug-logs/<session-id>/main.jsonl"');
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
  // Conservative fallback estimate for mixed English/code text.
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

    const fields = [
      'prompt_tokens',
      'completion_tokens',
      'input_tokens',
      'output_tokens',
      'total_tokens',
      'cached_tokens',
    ];

    const hasUsage = fields.some((f) => Number.isFinite(v[f]));
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

function inferLoopKey(record, index) {
  const attrs = isObject(record.attrs) ? record.attrs : {};
  const candidates = [
    record.turnId,
    record.loopId,
    record.interactionId,
    attrs.turnId,
    attrs.loopId,
    attrs.interactionId,
    record.spanId,
    attrs.spanId,
    record.sid ? `${record.sid}:${record.name || record.type || 'event'}` : null,
  ].filter(Boolean);

  if (candidates.length > 0) {
    return String(candidates[0]);
  }

  return `event-${String(index + 1).padStart(4, '0')}`;
}

function formatNum(v) {
  return String(v).padStart(8, ' ');
}

function main() {
  const inputPath = process.argv[2];
  if (!inputPath || inputPath === '--help' || inputPath === '-h') {
    usage();
    process.exit(inputPath ? 0 : 1);
  }

  const absPath = path.resolve(inputPath);
  if (!fs.existsSync(absPath)) {
    console.error(`File not found: ${absPath}`);
    process.exit(2);
  }

  const raw = fs.readFileSync(absPath, 'utf8');
  const lines = raw.split(/\r?\n/).filter((l) => l.trim().length > 0);

  if (lines.length === 0) {
    console.log('No events found in log file.');
    process.exit(0);
  }

  const loops = new Map();
  let invalid = 0;

  lines.forEach((line, idx) => {
    const record = safeJsonParse(line);
    if (!record) {
      invalid += 1;
      return;
    }

    const loopKey = inferLoopKey(record, idx);
    const usage = getActualUsage(record);

    const textChunks = [];
    collectText(record, textChunks);
    const joined = textChunks.join('\n');
    const estimated = estimateTokensFromText(joined);

    if (!loops.has(loopKey)) {
      loops.set(loopKey, {
        loopKey,
        events: 0,
        inputActual: 0,
        outputActual: 0,
        totalActual: 0,
        estimated: 0,
        firstTs: record.ts || 0,
        lastTs: record.ts || 0,
        names: new Set(),
      });
    }

    const bucket = loops.get(loopKey);
    bucket.events += 1;
    bucket.inputActual += usage.input;
    bucket.outputActual += usage.output;
    bucket.totalActual += usage.total;
    bucket.estimated += estimated;
    bucket.firstTs = Math.min(bucket.firstTs || Number.MAX_SAFE_INTEGER, record.ts || bucket.firstTs || 0);
    bucket.lastTs = Math.max(bucket.lastTs || 0, record.ts || bucket.lastTs || 0);
    if (record.name || record.type) {
      bucket.names.add(record.name || record.type);
    }
  });

  const rows = [...loops.values()].sort((a, b) => a.firstTs - b.firstTs);

  console.log(`Log file: ${absPath}`);
  console.log(`Parsed events: ${lines.length} (invalid JSON lines: ${invalid})`);
  console.log('');
  console.log('Per-loop token usage:');
  console.log('LOOP_KEY                                 EVENTS  ACT_INPUT ACT_OUTPUT ACT_TOTAL  EST_TOTAL  SOURCE');

  let sumInput = 0;
  let sumOutput = 0;
  let sumActual = 0;
  let sumEst = 0;

  for (const row of rows) {
    const hasActual = row.totalActual > 0 || row.inputActual > 0 || row.outputActual > 0;
    const source = hasActual ? 'actual+est' : 'estimate';

    sumInput += row.inputActual;
    sumOutput += row.outputActual;
    sumActual += row.totalActual;
    sumEst += row.estimated;

    const key = row.loopKey.length > 40 ? `${row.loopKey.slice(0, 37)}...` : row.loopKey.padEnd(40, ' ');

    console.log(
      `${key} ${String(row.events).padStart(6, ' ')} ${formatNum(row.inputActual)} ${formatNum(row.outputActual)} ${formatNum(row.totalActual)} ${formatNum(row.estimated)}  ${source}`
    );
  }

  console.log('');
  console.log('Totals:');
  console.log(`  Actual input tokens : ${sumInput}`);
  console.log(`  Actual output tokens: ${sumOutput}`);
  console.log(`  Actual total tokens : ${sumActual}`);
  console.log(`  Estimated total     : ${sumEst}`);

  if (sumActual === 0) {
    console.log('');
    console.log('Note: No exact usage fields found in this log. Estimated totals are character-based approximations.');
    console.log('If your VS Code/Copilot build does not emit usage counters, exact per-loop token usage is not recoverable from local debug logs.');
  }
}

main();
