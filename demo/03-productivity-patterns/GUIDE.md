# Developer Productivity Patterns

**Time:** ~15 min  
**Goal:** Practice six patterns you can use in your daily coding workflow.

Each pattern uses a different file in this folder. Work through them in order, or jump to the ones most relevant to your work.

---

## Pattern 1: Code Explanation (2 min)

> Understand complex code without reading every line.

**File:** [`transaction_processor.py`](transaction_processor.py)

1. Open the file and find the `process_batch_transactions()` function
2. Select the entire function
3. In Copilot Chat, type: `/explain`
4. Read the structured explanation

**What to notice:** Does it identify the risk checks, velocity limits, and error handling? Could you onboard onto this code faster with this approach?

---

## Pattern 2: Refactoring (2 min)

> Clean up messy code with a single prompt.

**File:** [`account_service.py`](account_service.py)

1. Open the file and find `validate_account_status()` — notice the deeply nested if/else
2. Select the entire function
3. Press `Ctrl+I` (inline chat) and type:
   ```
   Refactor this to:
   - Use early returns to reduce nesting
   - Extract magic numbers to named constants
   - Add appropriate error handling for a financial service
   ```
4. Review the diff and accept

**What to notice:** How many nesting levels were removed? Did it name the magic numbers (1000000, 500000)?

---

## Pattern 3: Test Generation (2 min)

> Bootstrap tests from the code you just refactored.

**File:** Continue with [`account_service.py`](account_service.py)

1. With the refactored function visible, open Copilot Chat and type:
   ```
   /tests Generate pytest tests for the refactored validate_account_status function.
   Include: happy path, boundary cases, invalid inputs, and edge cases for financial compliance.
   Use parametrize for the boundary cases.
   ```
2. Review the generated tests

**What to notice:** Are the test names descriptive? Does it test the boundaries you'd care about (e.g., exactly at the daily limit)?

---

## Pattern 4: Debugging (2 min)

> Find a subtle bug without stepping through the debugger.

**File:** [`payment_gateway.py`](payment_gateway.py)

1. Open the file and find `process_payment()`
2. Open Copilot Chat and type:
   ```
   This function is returning incorrect timestamps for transactions processed
   near midnight UTC. The amounts are correct but settlement_date is sometimes
   one day off. Can you identify the bug and suggest a fix?
   ```
3. Review Copilot's diagnosis

**What to notice:** Does it identify the naive vs. timezone-aware datetime issue? Is the suggested fix correct?

---

## Pattern 5: Documentation (2 min)

> Generate comprehensive docstrings in context.

**File:** [`transaction_processor.py`](transaction_processor.py)

1. Select the `process_batch_transactions()` function
2. Press `Ctrl+I` and type:
   ```
   Generate a comprehensive docstring including parameters, returns, raises, and a usage example
   ```
3. Accept the generated docstring

**What to notice:** Does it document the parameters with correct types? Does the usage example make sense?

---

## Pattern 6: Multi-step Tasks (3 min)

> Break a complex request into structured output.

**File:** [`payment_gateway.py`](payment_gateway.py)

1. Open Copilot Chat and type:
   ```
   I need to add retry logic to the payment_gateway.process_payment() function.
   Requirements:
   - Max 3 retries with exponential backoff
   - Only retry on timeout or 5xx errors
   - Log each retry attempt
   - Raise after final failure with context
   
   Please provide:
   1. The retry decorator
   2. The updated function
   3. Updated tests
   ```
2. Review the multi-part response

**What to notice:** Did Copilot structure its response matching your numbered list? Is the retry logic production-ready?

---

## Key Takeaway

Six patterns, one tool:

| Pattern | When to use it |
|---------|---------------|
| Explain | Onboarding, code reviews, unfamiliar repos |
| Refactor | Tech debt, code smells, readability |
| Test | After writing or refactoring code |
| Debug | Reproducing issues, tracing logic errors |
| Document | Before PRs, for team knowledge |
| Multi-step | Complex features, cross-cutting changes |

Pick one or two patterns and try them on **your own code** after the workshop.
