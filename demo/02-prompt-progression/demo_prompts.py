"""
Demo 2: Prompt Progression - Bad → Better → Best

INSTRUCTIONS FOR PRESENTER:
This file is your workspace for the prompt progression demo.
You'll use Copilot Chat to show three iterations of the same task.

SETUP:
1. Open this file in VS Code
2. Open Copilot Chat panel

DEMO FLOW:

────────────────────────────────────────────
ITERATION 1 - BAD PROMPT
────────────────────────────────────────────
In Copilot Chat, type:

    write a validation function

→ Show the result: generic, not useful, wrong assumptions
→ Say: "Copilot doesn't know what we're validating, for what context,
   or what 'valid' means."

────────────────────────────────────────────
ITERATION 2 - BETTER PROMPT
────────────────────────────────────────────
In Copilot Chat, type:

    Write a Python function that validates a financial transaction record.
    A transaction has: amount (float), currency (str), timestamp (datetime),
    account_id (str). Return True if valid, False otherwise.

→ Show the result: more relevant but still making assumptions about rules
→ Say: "Better—it knows the domain. But what are our validation rules?"

────────────────────────────────────────────
ITERATION 3 - BEST PROMPT
────────────────────────────────────────────
In Copilot Chat, type:

    Write a Python function `validate_transaction` that checks a financial
    transaction dict with these rules:
    - amount must be positive and ≤ 1,000,000
    - currency must be one of: EUR, USD, GBP
    - timestamp must not be in the future
    - account_id must match pattern: 2 letters + 8 digits (e.g., NL12345678)

    Return a tuple of (is_valid: bool, errors: list[str]).
    Use early returns. Include type hints. Follow Google docstring style.

→ Show the result: precise, usable, matches requirements
→ Say: "Same task. The difference is how we asked."

────────────────────────────────────────────
KEY TAKEAWAY
────────────────────────────────────────────
"Intent → Context → Constraints. That's the formula."
"""

# This is where the generated code will appear during the demo.
# You can paste Copilot's output here to keep a record of each iteration.

# --- Iteration 1 result (paste here during demo) ---


# --- Iteration 2 result (paste here during demo) ---


# --- Iteration 3 result (paste here during demo) ---
