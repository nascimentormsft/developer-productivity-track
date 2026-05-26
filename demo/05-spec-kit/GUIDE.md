# Spec Kit Demo: From Request to Build Plan

**Time:** ~10 min  
**Goal:** Show how Copilot can convert an unstructured request into a structured, reviewable implementation spec.

---

## Step 1: Start from a Raw Request (2 min)

1. Open [feature_request.md](feature_request.md)
2. Ask Copilot Chat:

```text
Transform this request into a complete engineering spec.
Use the structure from 05-spec-kit/spec_template.md.
Keep all assumptions explicit and add measurable acceptance criteria.
```

3. Review the output in chat.

**What to notice:**
- Did it preserve the real business constraint (decision support only)?
- Did it produce measurable criteria and not vague goals?

---

## Step 2: Tighten the Spec (4 min)

Ask a second prompt:

```text
Critique the spec you generated.
Identify ambiguous requirements, missing edge cases, and test gaps.
Then produce a revised version with explicit error handling.
```

**What to notice:**
- Ambiguous terms replaced with concrete definitions
- Edge cases listed (missing profile data, unsupported currency, stale behavior window)
- Acceptance criteria rewritten in Given/When/Then format

---

## Step 3: Generate an Execution Plan (4 min)

Ask a final prompt:

```text
Create a delivery plan from this spec with:
1) implementation tasks,
2) testing tasks,
3) rollout tasks,
4) owner role for each task,
5) done criteria.
```

**What to notice:**
- The plan separates build, test, and rollout work
- Work is scoped into independently reviewable tasks
- Done criteria reduces rework in implementation

---

## Key Message for Participants

A good spec is a productivity multiplier.
Copilot helps you move from "idea" to "execution-ready plan" in minutes, while keeping assumptions and acceptance criteria visible.
