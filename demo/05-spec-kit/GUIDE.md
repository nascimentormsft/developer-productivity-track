# Spec Kit Demo: github/spec-kit Workflow

**Time:** ~10 min  
**Goal:** Demonstrate the real `github/spec-kit` workflow inside Copilot, from intent to executable task list.

---

## Prerequisites (before session)

1. Install `uv` (required by Specify CLI):

```bash
# Windows (PowerShell)
winget install --id astral-sh.uv -e

# macOS
brew install uv

# Linux/macOS (official installer)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Install Specify CLI.

Replace `vX.Y.Z` with a real release tag (example: `v0.8.14`):

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z
```

Windows note: if `uv` is not recognized right after install, open a new terminal or run with the full path:

```powershell
& "$env:USERPROFILE\.local\bin\uv.exe" tool install specify-cli --from git+https://github.com/github/spec-kit.git@v0.8.14
```

3. Initialize a throwaway demo project (once):

```bash
specify init spec-kit-demo --integration copilot
cd spec-kit-demo
```

Note: `specify init --integration copilot` installs the `/speckit.*` commands for Copilot chat.

---

## Step 1: Define Principles (2 min)

In Copilot Chat, run:

```text
/speckit.constitution Create principles focused on code quality, testing standards, UX consistency, and performance requirements.
```

**What to notice:**
- Principles become persistent guardrails for all downstream spec, plan, and task generation.

---

## Step 2: Create the Spec (3 min)

1. Open [feature_request.md](feature_request.md).
2. Paste the business request into:

```text
/speckit.specify <paste the transfer-guard request>
```

3. Optionally refine unclear areas with:

```text
/speckit.clarify
```

**What to notice:**
- The command focuses on the "what" and "why" first.
- Ambiguities are surfaced before implementation details.

---

## Step 3: Plan and Task Breakdown (3 min)

1. Open [spec_template.md](spec_template.md) and use it as your architecture/constraint prompt for planning.
2. Run:

```text
/speckit.plan <paste stack and constraints prompt>
```

3. Generate implementation tasks:

```text
/speckit.tasks
```

4. Optional quality gate:

```text
/speckit.analyze
```

**What to notice:**
- Output is separated into artifacts: spec, technical plan, then actionable tasks.
- This creates a review point before coding starts.

---

## Step 4: Execute (2 min)

Use:

```text
/speckit.implement
```

For workshops, you can stop at `/speckit.tasks` and discuss generated task quality instead of full implementation.

---

## Key Message for Participants

`github/spec-kit` is not just a prompt template. It is a structured spec-driven workflow with reusable commands that turn intent into governed, executable delivery artifacts.
