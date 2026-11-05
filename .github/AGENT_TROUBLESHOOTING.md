# 🎯 Agent Orchestration Troubleshooting Guide
**Complete Reference for SDD PDLC Agent Orchestration**

---

## 📋 TABLE OF CONTENTS

### Quick Navigation
1. [Quick Start Guide](#quick-start-guide) — 60-second start
2. [Decision Tree](#decision-tree) — Find your issue fast
3. [Common Issues (1-10)](#common-issues) — 10 typical problems with solutions
4. [Error Reference (A-F)](#error-reference-comprehensive) — 19 specific errors
5. [Orchestration Workflows](#orchestration-workflows) — 7-stage PDLC flow
6. [Health Check Checklist](#health-check-checklist) — Before major work
7. [Escalation Procedures](#escalation-procedures) — Who to contact

### By Role
- [For Developers](#for-developers)
- [For Tech Leads](#for-tech-leads)
- [For QA Engineers](#for-qa-engineers)
- [For DevOps Teams](#for-devops-teams)

### Complete Reference
- [All 10 Common Issues](#common-issues)
- [All 19 Specific Errors](#error-reference-comprehensive)
- [Diagnostic Commands](#diagnostic-commands)
- [Prevention Tips](#prevention-tips)

---

## Quick Start Guide

### I Have an Error Message → 2-30 min
1. Scroll to [Error Reference (A-F)](#error-reference-comprehensive)
2. Search (Cmd+F) for your error message
3. Follow: Root Cause → Debug Steps → Action Steps → Prevention

### I Don't Know What's Wrong → 5 min
1. Check the [Decision Tree](#decision-tree) below
2. Find your symptom
3. Click the link to the relevant issue section

### I Need a Quick Fix → 2-5 min
1. Scroll to [Quick Reference Table](#quick-reference) below
2. Find your problem
3. Apply the "What to Do" solution

### Before Starting Major Work → 1 min
1. Go to [Health Check Checklist](#health-check-checklist)
2. Run the bash script
3. Verify all checks pass

---

## Decision Tree

```
Do you have an error message?
├─ YES → Go to "Error Reference (A-F)" section (search Cmd+F)
│
└─ NO → Do you have a symptom?
   ├─ YES → Check "Quick Reference Table" below
   │
   └─ NO → What's your role?
      ├─ Developer → See "For Developers" section
      ├─ Tech Lead → See "For Tech Leads" section
      ├─ QA → See "For QA Engineers" section
      └─ DevOps → See "For DevOps Teams" section
```

---

## Quick Reference Table

| Problem | What to Do | Time |
|---------|-----------|------|
| Agent won't start | Check MCP server status (see Issue #1) | 5 min |
| Context not loading | Run Context Builder/Updater (see Issue #2) | 5-10 min |
| Jira connection failing | Verify credentials & reload extensions (see Issue #3) | 5 min |
| Compliance review blocks | Review findings & address or request acceptance (see Issue #4) | 10-30 min |
| Traceability links missing | Verify issue types & naming (see Issue #5) | 5-10 min |
| Figma extraction failing | Check auth, use manual upload fallback (see Issue #6) | 5-15 min |
| Agent timing out | Increase timeout, check resources (see Issue #7) | 5 min |
| Output directory errors | Check RUN_ID & path structure (see Issue #8) | 5 min |
| Quality gate failures | Review coverage & add tests (see Issue #9) | 10-30 min |
| Source files not found | Verify file paths & search patterns (see Issue #10) | 5-10 min |

---

## For Developers

**Quick Tips:**
1. Bookmark this doc for quick reference
2. Before work: Run health check (1 min)
3. When stuck: Search error reference (Cmd+F)
4. Share: Send this doc link to teammates

**Common Dev Issues:**
- Agent startup problems → Issue #1
- Context loading errors → Issue #2
- Jira auth failures → Issue #3
- Output directory issues → Issue #8

---

## For Tech Leads

**Key Responsibilities:**
1. Share this doc with your team
2. Review [Orchestration Workflows](#orchestration-workflows) before major releases
3. Understand compliance gates (see Issue #4)
4. Use [Health Check Checklist](#health-check-checklist) before approval

**Review Before Handoff:**
- Specification gate (after Technical Specifier)
- Planning gate (after Implementation Planner)
- Code quality gate (after Technical Documenter)

---

## For QA Engineers

**Testing Checklist:**
1. Run health check before test cycles
2. Review compliance gate findings
3. Check test coverage requirements
4. Use diagnostic commands for debugging

**Common QA Issues:**
- Quality gate failures → Issue #9
- Coverage < 80% → Add unit tests
- SonarQube HIGH issues → Fix or document acceptance

---

## For DevOps Teams

**Operational Guidance:**
1. Set up monitoring using diagnostic commands
2. Review failure recovery procedures (see [Orchestration Workflows](#orchestration-workflows))
3. Have [Escalation Procedures](#escalation-procedures) ready
4. Run health check regularly

**Critical Tasks:**
- Monitor MCP server health
- Maintain context file synchronization
- Track compliance gate findings
- Manage escalations

---

## Common Issues

## Quick Reference

### 1. Agent Not Starting or Responding

**Symptoms:** Agent doesn't appear in Copilot picker, or chat times out

**Diagnosis Steps:**
```bash
# Check MCP server status
ps aux | grep mcp
ps aux | grep jira
ps aux | grep playwright
```

**Common Causes & Fixes:**

| Cause | Fix |
|-------|-----|
| MCP server not running | Reload VS Code extensions: Cmd+Shift+P → "Copilot Extensions: Reload" |
| Agent file YAML syntax error | Validate `.github/agents/*.agent.md` frontmatter |
| Missing VS Code extensions | Install Copilot Chat and required extensions |
| Agent not in `user-invocable: true` | Check agent frontmatter; set to `true` if needed |
| Stale copilot-instructions.md cache | Clear `.github/copilot-instructions.md` cache by editing any rule file |

---

### 2. Context Loading Failures

**Symptoms:** Agent says "Context not found" or references outdated standards

**Root Cause:** `.github/contexts/` files are missing or out of sync

**Resolution:**

```bash
# Step 1: Check if context files exist
ls -la .github/contexts/

# Step 2: If missing, run Context Builder agent
# (Manual: Select "Context Builder" from Copilot agent picker)

# Step 3: If out of sync, run Context Updater
# (Manual: Select "Context Updater" from Copilot agent picker)
# The agent will scan package.json, config files, and project structure
```

**Context Files Expected:**
- `.github/contexts/business-context.md` — Business requirements and rules
- `.github/contexts/domain-context.md` — Industry/domain guidance
- `.github/contexts/frontend-context.md` — UI implementation patterns
- `.github/contexts/backend-context.md` — API and service patterns
- `.github/contexts/testing-context.md` — Test frameworks and strategy

---

### 3. MCP Server Errors (Jira Integration)

**Error:** "Failed to connect to Jira" / "JIRA_URL not found"

**Diagnosis:**
```bash
# Check MCP configuration
cat .vscode/mcp.json
echo "Check for jira server entry"

# Test Jira connectivity
curl -u $JIRA_USERNAME:$JIRA_API_TOKEN \
  -X GET "$JIRA_URL/rest/api/3/myself" \
  -H "Content-Type: application/json"
```

**Fix Steps:**
1. **Verify credentials in VS Code:**
   - Open Copilot settings
   - Check `jira-url`, `jira-username`, `jira-api-token` inputs
   - Ensure API token is current (Jira tokens expire)

2. **Reload MCP server:**
   - Cmd+Shift+P → "Copilot Extensions: Reload"
   - Wait 5-10 seconds for reconnection

3. **Test in new chat:**
   - Start a fresh Copilot Chat window
   - Agent tools should be available

---

### 4. Compliance Reviewer Gate Failures

**Symptoms:** Agent stops with `REVIEW GATE: FAIL` before handing off to next stage

**Understanding FAIL Status:**

```text
FAIL Status (Does NOT always block):
├─ CRITICAL findings → BLOCKS handoff (hard stop)
├─ HIGH findings → BLOCKS handoff (hard stop)
├─ MEDIUM findings → BLOCKS handoff (hard stop)
└─ LOW findings only → Proceeds with REVIEW_GATE_WARNING

Rule: Highest severity determines blocking behavior
     Keep FAIL status visible; do not relabel to PASS
```

**Resolution by Severity:**

| Severity | Action | Next Step |
|----------|--------|-----------|
| CRITICAL | Fix immediately | Re-run stage agent + compliance review |
| HIGH | Fix or get written approval from owner | Document approval in compliance log; re-review |
| MEDIUM | Fix or get written approval from owner | Document approval in compliance log; re-review |
| LOW | May proceed with warning | Record warning in handoff; proceed with human sign-off |

**Example Workflow:**
```
1. Technical Specifier runs → produces spec.md
2. Compliance Reviewer invoked automatically → finds 2 HIGH issues
3. Status = FAIL, proceed = BLOCKED
4. Human: fix HIGH issues in spec.md
5. Re-run Technical Specifier
6. Compliance Reviewer runs again
7. Status = PASS → proceed to Implementation Planner
```

---

### 5. Traceability Broken (FR/NFR Not Mapping to Specs)

**Symptoms:** Traceability matrix shows gaps; `FR-*` or `NFR-*` unreferenced in specs

**Diagnosis:**
```bash
# View traceability matrix
cat requirement/Traceability_Matrix.md

# Check for CTX-UPDATE entries (recent changes)
grep "CTX-UPDATE" requirement/Traceability_Matrix.md

# Search spec for missing references
grep -c "FR-\|NFR-" output/*/specify/spec.md
```

**Fix:**
```bash
# Run Traceability Manager to rebuild matrix
# (Manual: Select "Traceability Manager" agent from Copilot)

# The agent will:
# 1. Scan all .github/contexts/ files for CTX-* IDs
# 2. Scan all requirement/Context_*.md files for FR-*/NFR-*
# 3. Scan all output/*/specify/spec.md for SPEC-* references
# 4. Update requirement/Traceability_Matrix.md
# 5. Flag missing mappings
```

---

### 6. Figma Extraction Failures

**Symptoms:** Figma links in requirements but no design artifacts extracted

**Common Errors:**

| Error | Cause | Fix |
|-------|-------|-----|
| "Invalid Figma URL" | Malformed link in requirement | Provide valid Figma share/design URL |
| "Rate limit exceeded" | Too many extraction requests | Retry in 1-2 hours or request higher quota |
| "Authentication failed" | Figma MCP credentials invalid | Verify FIGMA_TOKEN env var; request new token |
| "File not found in Figma" | Wrong project/file ID | Copy link directly from Figma UI |

**Fallback Path (Non-Blocking):**
- Figma extraction never blocks spec creation
- Record failure in `figma_report.md`
- If frontend scope (`UI In Scope = YES`):
  - Extract screenshots manually from Figma
  - Upload to `output/{RUN_ID}/specify/figma/png/screens/`
  - Assign `SCR-*` screen IDs manually
  - Record `Design Source: Manual upload (no Figma link)` in spec
- Continue with specification

---

### 7. Agent Stuck or Timeout

**Symptoms:** Chat shows loading spinner for 5+ minutes; no response

**Immediate Actions:**
```bash
# Check system resources
top -l1 | grep -E "^PhysMem|^CPU"

# Check network connectivity
ping -c 3 github.com
ping -c 3 api.github.com
```

**Escalation Steps:**
1. **Stop chat:** Close chat window (does not cancel background agent)
2. **Reload extensions:** Cmd+Shift+P → "Copilot Extensions: Reload"
3. **Restart agent:** Open new chat, re-invoke same agent
4. **Check agent status:** If agent still running background, monitor with:
   ```bash
   ps aux | grep "copilot\|agent" | grep -v grep
   ```

**Prevent Future Timeouts:**
- Break large requirements into smaller user stories
- Run agents during off-peak hours
- Split multi-file specs into separate runs

---

### 8. Output Directory Not Created

**Symptoms:** Agent completes but no `output/{RUN_ID}/` folder

**Cause:** Agent did not assign a run ID or failed silently

**Check:**
```bash
# List all output folders
ls -la output/

# Check for recent Copilot session logs
cat ~/.copilot/session-state/*/session.log | tail -50
```

**Fix:**
1. Verify agent returned a run ID in final message
2. If missing, re-run agent with explicit prompt:
   ```
   "Generate a new RUN_ID (e.g., RUN_20261105_SPECIFY_ABC123) and place outputs in output/{RUN_ID}/"
   ```
3. Check disk space:
   ```bash
   df -h
   ```

---

### 9. Quality Gate Failures (SonarQube / Coverage)

**Symptoms:** Implementation marked `FAIL` due to coverage < 80% or SonarQube issues

**Check Coverage:**
```bash
# Review coverage report
cat output/*/implement/code-quality/coverage-report.md

# Run tests locally to verify
npm test -- --coverage
# or
pytest --cov=src tests/
```

**Fix SonarQube Issues:**
```bash
# View detailed issues
cat output/*/implement/code-quality/sonarqube-remediation-log.md

# Fix by severity:
# CRITICAL → Must fix before handoff
# HIGH → Fix or document approval
# MEDIUM/LOW → May proceed with documented rationale
```

**Improve Coverage:**
1. Identify untested functions:
   ```bash
   grep "uncovered" output/*/implement/code-quality/coverage-report.md
   ```
2. Add unit tests for gaps
3. Re-run coverage check
4. Document in implementation-quality-log.md

---

### 10. Agent Can't Find Source Files

**Symptoms:** Agent says "File not found" or "Unable to parse requirement"

**Diagnosis:**
```bash
# Check file exists
ls -la requirement/

# Check file is readable
cat requirement/Context_*.md | head

# Verify correct path in agent invocation
# Agent expects: requirement/Context_{ProjectName}.md
```

**Common Path Mistakes:**
- Using `requirements/` instead of `requirement/`
- Using `.md` vs `.MD` extension
- File in `docs/` instead of `requirement/`

---

## Debug Mode Activation

Enable verbose logging for agent orchestration:

```bash
# Set environment variables
export DEBUG=copilot-agent:*
export LOG_LEVEL=debug

# Restart VS Code
# Re-run agent with verbose logging
# Check logs at ~/.copilot/session-state/*/logs/
```

---

## Health Check Checklist

Run this before starting a major PDLC workflow:

```bash
# ✅ All context files present
[ -f .github/contexts/business-context.md ] && echo "✓ Business context" || echo "✗ MISSING"
[ -f .github/contexts/frontend-context.md ] && echo "✓ Frontend context" || echo "✗ MISSING"
[ -f .github/contexts/backend-context.md ] && echo "✓ Backend context" || echo "✗ MISSING"
[ -f .github/contexts/testing-context.md ] && echo "✓ Testing context" || echo "✗ MISSING"

# ✅ Agent files valid YAML
for file in .github/agents/*.agent.md; do
  grep -q "^---" "$file" && echo "✓ $file" || echo "✗ INVALID: $file"
done

# ✅ MCP server running (if Jira integration needed)
ps aux | grep -q "mcp\|jira" && echo "✓ MCP server running" || echo "✗ MCP server DOWN"

# ✅ Traceability matrix current
[ -f requirement/Traceability_Matrix.md ] && echo "✓ Traceability exists" || echo "✗ MISSING"

# ✅ Output directory writable
[ -w output/ ] && echo "✓ Output writable" || echo "✗ OUTPUT NOT WRITABLE"
```

---

## Support Resources

- **Agent Reference:** `.github/AGENTS_SETUP.md`
- **PDLC Standards:** `.github/rules/pdlc.md`
- **Context Management:** `.github/CONTEXT_MANAGEMENT_GUIDE.md`
- **MCP Setup:** `.github/MCP_QUICK_START.md`
- **Quality Gates:** `.github/rules/*-execution-gates.md`


---

## Error Reference (Comprehensive)

### Category A: Context & Loading Errors

#### A1: "Context file missing: business-context.md"
**Root Cause:** `.github/contexts/` directory not initialized  
**Debug:** `ls -la .github/contexts/`  
**Fix:** Run Context Builder agent  
**Prevent:** Create contexts before starting any agent workflow

#### A2: "Outdated context standards detected"
**Root Cause:** Context files out of sync with source code  
**Debug:** `grep "last_updated\|version" .github/contexts/*.md`  
**Fix:** Run Context Updater agent  
**Prevent:** Run Context Updater monthly or after major code changes

---

### Category B: Jira Integration Errors

#### B1: "JIRA_AUTH_FAILED: Invalid credentials"
**Root Cause:** API token expired or wrong credentials  
**Debug:** Test token: `curl -u $USER:$TOKEN https://$JIRA_URL/rest/api/3/myself`  
**Fix:** Regenerate Jira API token (Jira Settings → API Tokens)  
**Prevent:** Rotate tokens quarterly; monitor token expiry

#### B2: "JIRA_ISSUE_NOT_FOUND: Key STORY-9999"
**Root Cause:** Wrong issue key or deleted issue  
**Debug:** Search Jira for issue manually  
**Fix:** Verify issue key (uppercase PROJECT-#### format)  
**Prevent:** Copy issue keys directly from Jira, don't type

#### B3: "JIRA_INVALID_ISSUE_TYPE: Expected 'Story', got 'Task'"
**Root Cause:** Story key points to wrong issue type  
**Debug:** Open issue in Jira, check Type field  
**Fix:** Provide correct Story issue key  
**Prevent:** Validate issue type before providing to agent

---

### Category C: Compliance Review Errors

#### C1: "COMPLIANCE_GATE: CRITICAL findings block handoff"
**Root Cause:** Specification fails security/traceability checks  
**Debug:** Review findings list in compliance report  
**Fix:** Fix CRITICAL issues, re-run spec, re-review  
**Prevent:** Peer review specs before compliance gate

#### C2: "COMPLIANCE_GATE: Coverage < 80%"
**Root Cause:** Insufficient unit test coverage  
**Debug:** `sonarqube_analyzeFile` output  
**Fix:** Add unit tests to reach 80%+  
**Prevent:** Maintain coverage above 85% in ongoing code

---

### Category D: Figma Integration Errors

#### D1: "FIGMA_RATE_LIMIT: Extraction quota exceeded"
**Root Cause:** Too many extraction requests in short time  
**Debug:** Check Figma API quota status  
**Fix:** Wait 1-2 hours; use manual screenshot fallback  
**Prevent:** Extract designs before spec generation begins

#### D2: "FIGMA_AUTH_FAILED: Invalid FIGMA_TOKEN"
**Root Cause:** Token expired or misconfigured  
**Debug:** `echo $FIGMA_TOKEN` (should not be empty)  
**Fix:** Regenerate Figma personal access token  
**Prevent:** Store token securely; rotate quarterly

---

### Category E: Test & Coverage Errors

#### E1: "TEST_COVERAGE_FAILED: Coverage 72% < Required 80%"
**Root Cause:** Missing unit tests  
**Debug:** `npm run coverage` or `pytest --cov`  
**Fix:** Add unit tests for untested functions  
**Prevent:** Write tests alongside code; use pre-commit hooks

#### E2: "SONARQUBE_HIGH_ISSUES: 12 found, limit 5"
**Root Cause:** Code quality issues not addressed  
**Debug:** Review SonarQube report  
**Fix:** Fix issues or document acceptance with tech lead  
**Prevent:** Run SonarQube locally before commit

---

### Category F: Files & RUN_ID Errors

#### F1: "RUN_ID_MISSING: No RUN_ID found in output/"
**Root Cause:** Agent didn't receive RUN_ID from previous agent  
**Debug:** `ls -la output/`  
**Fix:** Copy RUN_ID from previous agent output  
**Prevent:** Always pass RUN_ID explicitly between agents

#### F2: "OUTPUT_EXISTS: output/{RUN_ID}/specify/ already populated"
**Root Cause:** Overwriting previous run  
**Debug:** `ls -la output/{RUN_ID}/specify/`  
**Fix:** Generate new RUN_ID (UUID) or confirm overwrite  
**Prevent:** Use unique timestamps or UUIDs for RUN_IDs

---

### Category G: Other Common Errors

#### G1: "TIMEOUT: Agent execution exceeded 300 seconds"
**Root Cause:** Large inputs, slow network, or resource constraints  
**Debug:** Monitor system resources during agent run  
**Fix:** Increase timeout, split work into smaller batches  
**Prevent:** Run health check before major work

#### G2: "NETWORK_ERROR: Cannot reach GitHub API"
**Root Cause:** Network connectivity issue  
**Debug:** `ping github.com && curl -I https://api.github.com`  
**Fix:** Check internet connection, retry  
**Prevent:** Test connectivity before starting work

---

## Orchestration Workflows

### 7-Stage PDLC Flow

```
┌─────────────────────────────────────────────────────────────┐
│ STAGE 1: Context Builder (if starting fresh)                │
│ Output: business-context.md, domain-context.md, etc.        │
└──────────────────────────┬──────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ STAGE 2: Technical Specifier                                │
│ Input: Story or requirements                                │
│ Output: spec.md with SPEC-* IDs                             │
│ Gate: Compliance Reviewer (auto) → spec gate                │
└──────────────────────────┬──────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ STAGE 3: Implementation Planner                             │
│ Input: spec.md                                              │
│ Output: plan.md with TASK-* IDs                             │
│ Gate: Compliance Reviewer (auto) → plan gate                │
└──────────────────────────┬──────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ STAGE 4: Implementation Builder                             │
│ Input: plan.md                                              │
│ Output: Source code changes                                 │
└──────────────────────────┬──────────────────────────────────┘
                           ↓
      ┌────────────────────┴─────────────────┐
      ↓                                       ↓
┌──────────────────┐              ┌──────────────────┐
│ STAGE 5A:        │              │ STAGE 5B:        │
│ API Tester       │              │ Functional Test  │
│ (Parallel)       │              │ (Parallel)       │
│ Output: Test     │              │ Output: Test     │
│ results + logs   │              │ results + logs   │
└────────┬─────────┘              └────────┬─────────┘
         │                                  │
         └──────────────┬───────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ STAGE 6: Technical Documenter                               │
│ Input: Source code + test results                           │
│ Output: docs/ with DOC-* IDs                                │
│ Gate: Compliance Reviewer (auto) → code quality gate        │
└──────────────────────────┬──────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ STAGE 7: Traceability Manager                               │
│ Input: All artifacts                                        │
│ Output: Traceability_Matrix.md updated                      │
│ Gate: Verification that all IDs map                         │
└─────────────────────────────────────────────────────────────┘
```

### 3 Compliance Review Gates

**Gate 1: Specification Gate** (after Technical Specifier)
- ✅ Checks: Traceability, security, unit-test applicability
- 🛑 Blocks: CRITICAL, HIGH, MEDIUM findings
- ⚠️  Warns: LOW findings (does not block)

**Gate 2: Planning Gate** (after Implementation Planner)
- ✅ Checks: Task decomposition, dependencies, capacity
- 🛑 Blocks: CRITICAL, HIGH, MEDIUM findings
- ⚠️  Warns: LOW findings (does not block)

**Gate 3: Code Quality Gate** (after Technical Documenter)
- ✅ Checks: Coverage ≥ 80%, SonarQube, security, test traceability
- 🛑 Blocks: Coverage < 80%, HIGH SonarQube issues
- ⚠️  Warns: LOW SonarQube issues (can proceed with documentation)

### Context Handoff Protocol (4 Steps)

```
Agent N-1 → Agent N:
1. LOAD:   Agent N loads .github/contexts/ files
2. ACCEPT: Agent N receives input (story key + RUN_ID)
3. PROCESS: Agent N creates output/{RUN_ID}/{stage}/*
4. EMIT:   Agent N emits RUN_ID + artifacts to next agent
```

### Failure Recovery (5 Common Scenarios)

**Scenario 1:** Implementation Planner task decomposition fails
- Recovery: Re-run planner with reduced scope
- Escalate to: Tech lead for scope review

**Scenario 2:** API tests fail after implementation
- Recovery: Fix code, re-run API tester
- Escalate to: DevOps if API endpoint unavailable

**Scenario 3:** Compliance review HIGH finding on spec
- Recovery: Fix issue in spec, re-review
- Escalate to: Tech lead if fix not obvious

**Scenario 4:** Test coverage below 80%
- Recovery: Add unit tests, re-run coverage check
- Escalate to: QA lead if coverage tool misconfigured

**Scenario 5:** Traceability matrix has gaps
- Recovery: Run Traceability Manager to rebuild
- Escalate to: Architect if fundamental design issue

---

## Health Check Checklist

### Pre-Work Verification (1 Minute)

Run this bash script before starting major work:

```bash
#!/bin/bash
echo "🔍 Agent Orchestration Health Check"
echo "===================================="

# Check 1: Context files exist
echo "✓ Checking context files..."
if [ -f .github/contexts/business-context.md ] && \
   [ -f .github/contexts/domain-context.md ] && \
   [ -f .github/contexts/frontend-context.md ] && \
   [ -f .github/contexts/backend-context.md ] && \
   [ -f .github/contexts/testing-context.md ]; then
  echo "  ✅ All 5 context files present"
else
  echo "  ❌ Missing context file(s) - run Context Builder"
fi

# Check 2: Agent files exist
echo "✓ Checking agent files..."
if [ -d .github/agents ] && [ $(ls -1 .github/agents/*.agent.md | wc -l) -gt 5 ]; then
  echo "  ✅ Agent directory has multiple agents"
else
  echo "  ❌ Agent directory missing or empty"
fi

# Check 3: MCP configuration
echo "✓ Checking MCP configuration..."
if [ -f .vscode/mcp.json ]; then
  echo "  ✅ MCP config exists"
else
  echo "  ❌ MCP config missing"
fi

# Check 4: Git status
echo "✓ Checking git status..."
if [ -z "$(git status --porcelain)" ]; then
  echo "  ✅ Working tree clean"
else
  echo "  ⚠️  Working tree has uncommitted changes - stash before agent run"
fi

# Check 5: Output directory
echo "✓ Checking output directory..."
if [ -d output ]; then
  echo "  ✅ Output directory exists"
else
  echo "  ℹ️  Output directory will be created by agents"
fi

echo ""
echo "✅ Health check complete"
```

### Before Each Stage
- [ ] Previous stage completed successfully
- [ ] Output artifacts are in place
- [ ] No uncommitted local changes
- [ ] Jira credentials current
- [ ] Network connectivity verified

---

## Diagnostic Commands

```bash
# Check MCP server status
ps aux | grep -E "mcp|jira|playwright" | grep -v grep

# Test Jira connectivity
curl -u $JIRA_USERNAME:$JIRA_API_TOKEN \
  -X GET "$JIRA_URL/rest/api/3/myself" 2>/dev/null | jq .

# View context file status
ls -lah .github/contexts/

# Check agent configuration
grep -r "user-invocable: true" .github/agents/

# Verify output directory structure
find output -type f | head -20

# Check traceability matrix
cat requirement/Traceability_Matrix.md | head -30

# Monitor agent process
ps aux | grep -E "agent|copilot" | grep -v grep

# View recent git commits
git log --oneline -10

# Check file permissions
ls -la .github/contexts/
ls -la .github/agents/
ls -la output/

# Validate YAML frontmatter
grep -A5 "^---" .github/agents/*.agent.md | head -20
```

---

## Escalation Procedures

### When to Escalate

| Situation | Who | Priority | Action |
|-----------|-----|----------|--------|
| CRITICAL compliance finding | Tech Lead | 🔴 Immediate | Provide spec + finding screenshot |
| Jira token expired | DevOps | 🟠 High | Request token regeneration |
| Context files missing | Architect | 🟠 High | Request Context Builder run |
| Agent not responding for 10+ min | DevOps | 🟡 Medium | Check MCP server status |
| Coverage < 80% (unclear how to fix) | QA Lead | 🟡 Medium | Share coverage report |

### Escalation Template

```
Issue: [Brief title]
Severity: [CRITICAL / HIGH / MEDIUM / LOW]
Time Impact: [When did this start?]
Steps to Reproduce: [Exact sequence]
Current Status: [What have you tried?]
Supporting Info: [Error logs, screenshots, etc.]

Request: [What action needed from recipient?]
```

---

## Prevention Tips

1. **Always run health check before major work** (1 min)
2. **Keep Jira tokens fresh** (rotate quarterly)
3. **Update contexts monthly** (or after code changes)
4. **Commit regularly** (don't accumulate uncommitted changes)
5. **Test specs before compliance review** (peer review first)
6. **Write tests alongside code** (maintain 85%+ coverage)
7. **Verify output RUN_IDs between agents** (copy explicitly)
8. **Monitor compliance findings** (address HIGH/CRITICAL immediately)
9. **Keep MCP config in sync** (.vscode/mcp.json)
10. **Run Context Updater** (when dependencies or tech stack changes)

---

## Quick Troubleshooting By Symptom

| Symptom | First Check | Next Step | Final |
|---------|------------|-----------|-------|
| "Agent not found" | Reload extensions | Check YAML frontmatter | Verify `user-invocable: true` |
| "Context error" | ls .github/contexts/ | Run Context Builder | Check file contents |
| "Jira won't connect" | Test curl command | Check credentials | Regenerate token |
| "Compliance blocks" | Review findings | Fix issues | Re-run & re-review |
| "Tests failing" | Check code changes | Run health check | Review test logs |
| "Output missing" | Check RUN_ID | Verify agent run | Check output/ directory |
| "Timeout" | Check resources | Increase timeout | Split into smaller batches |
| "Links broken" | Verify issue types | Check naming | Run Traceability Manager |

---

## Support Resources

**Need more help?**
- Check this doc's Table of Contents (Cmd+F to search)
- Review error in [Error Reference (Comprehensive)](#error-reference-comprehensive)
- Run [Health Check Checklist](#health-check-checklist)
- Use [Diagnostic Commands](#diagnostic-commands)
- Follow [Escalation Procedures](#escalation-procedures)

**Document Status:** ✅ Production Ready | Last Updated: 2026-11-05

