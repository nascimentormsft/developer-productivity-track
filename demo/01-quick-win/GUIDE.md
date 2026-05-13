# Quick Win: Your First Copilot Interactions

**Time:** ~5 min  
**Goal:** Experience two core Copilot capabilities — code generation and code explanation.

---

## Exercise A: Generate a Function from a Comment

> See how Copilot turns a plain English comment into working code.

1. Open [`demo_quickwin.py`](demo_quickwin.py)
2. Place your cursor at the **end of the comment line** and press **Enter**
3. Start typing: `def calc`
4. Wait for Copilot's ghost text suggestion to appear
5. Press **Tab** to accept

**What to notice:**
- Did Copilot add type hints to the parameters?
- Did it generate a docstring?
- Is the compound interest formula correct?
- How many seconds did that take vs. writing it yourself?

> **Try it again:** Delete the generated function, change the comment to something else (e.g., "Calculate simple moving average for a list of prices"), and repeat.

---

## Exercise B: Explain Unfamiliar Code

> Use Copilot to understand a dense, undocumented function instantly.

1. Open [`legacy_risk_calculator.py`](legacy_risk_calculator.py)
2. Select the **entire** `calculate_portfolio_var` function (lines 13–80)
3. Open Copilot Chat (`Ctrl+Alt+B`) and type:
   ```
   /explain
   ```
4. Read the explanation Copilot produces

**What to notice:**
- Does it identify the three calculation methods (historical, parametric, Monte Carlo)?
- Does it explain the risk parameters (confidence level, horizon)?
- Could you have understood this code faster by reading it line by line?

> **Try a follow-up:** With the function still selected, ask:
> ```
> What are the potential issues or bugs in this code?
> ```

---

## Key Takeaway

Two interactions, under 2 minutes:
- **Generate** — go from intent to working code
- **Explain** — understand unfamiliar code without reading every line

Both happened without leaving your editor.
