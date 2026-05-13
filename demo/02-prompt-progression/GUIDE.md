# Prompt Progression: From Vague to Precise

**Time:** ~10 min  
**Goal:** See how the same task produces dramatically different results depending on how you prompt.

---

## The Formula

> **Intent** + **Context** + **Constraints** = Great Output

You'll ask Copilot the same thing three times, improving your prompt each time.

---

## Iteration 1 — Vague Prompt

Open Copilot Chat (`Ctrl+Alt+B`) and type:

```
write a validation function
```

**Observe the result:**
- What language did it pick? What is it validating?
- Is this useful to you? Could you drop it into your codebase?
- What assumptions did Copilot make that are wrong?

> The problem: Copilot doesn't know *what* you're validating, *for what domain*, or what *"valid" means*.

---

## Iteration 2 — Add Context

Now type:

```
Write a Python function that validates a financial transaction record.
A transaction has: amount (float), currency (str), timestamp (datetime),
account_id (str). Return True if valid, False otherwise.
```

**Observe the improvement:**
- It knows the domain (financial transactions)
- It knows the data structure
- But it's still guessing at the validation rules

> Better — but *what are your specific rules?*

---

## Iteration 3 — Add Constraints

Now type:

```
Write a Python function `validate_transaction` that checks a financial
transaction dict with these rules:
- amount must be positive and ≤ 1,000,000
- currency must be one of: EUR, USD, GBP
- timestamp must not be in the future
- account_id must match pattern: 2 letters + 8 digits (e.g., NL12345678)

Return a tuple of (is_valid: bool, errors: list[str]).
Use early returns. Include type hints. Follow Google docstring style.
```

**Observe the result:**
- Precise validation rules, exactly as specified
- Clean code structure with early returns
- Type hints and docstring included
- Ready to use — minimal editing needed

---

## Try It Yourself

Open [`demo_prompts.py`](demo_prompts.py) and paste each result below the corresponding section marker. Compare the three side by side.

**Bonus challenge:** Pick a task from your own work and write three iterations:
1. A one-liner (vague)
2. Add domain context (what, where, why)
3. Add constraints (rules, format, style, edge cases)

---

## Key Takeaway

Same task, same AI, completely different results.  
The difference is **how you asked** — not how smart the model is.

**Remember:** Intent → Context → Constraints.
