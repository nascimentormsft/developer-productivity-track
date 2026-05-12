# Demo Codebase - Developer Productivity with GitHub Copilot

## Folder Structure

```
demo/
├── 01-quick-win/
│   ├── demo_quickwin.py          # Empty file with a comment → let Copilot generate
│   └── legacy_risk_calculator.py  # Dense function to /explain
│
├── 02-prompt-progression/
│   └── demo_prompts.py           # Instructions for bad → better → best prompts
│
├── 03-productivity-patterns/
│   ├── transaction_processor.py   # Code explanation + documentation demos
│   ├── account_service.py         # Refactoring + test generation demos
│   └── payment_gateway.py         # Debugging + multi-step task demos
│
├── 04-pandas-scenario/
│   ├── generate_dataset.py        # Run once to create the CSV
│   ├── financial_transactions.csv # 10K synthetic transactions (pre-generated)
│   ├── pandas_demo.py            # Full demo script with prompts and backup code
│   └── test_pandas_demo.py       # Backup tests for Step 6
│
└── 05-hands-on-lab/
    ├── financial_transactions.csv # Same dataset for participants
    ├── lab_exercise.py           # Participant starter file (with instructions)
    └── lab_solution.py           # Solution (facilitator only, don't share!)
```

## Demo Flow

### 1. Quick Win (Section 1 – 3 min)
1. Open `01-quick-win/demo_quickwin.py` → cursor below comment → Tab to accept Copilot suggestion
2. Open `01-quick-win/legacy_risk_calculator.py` → select function → `/explain`

### 2. Prompt Progression (Section 2 – 5 min)
1. Open `02-prompt-progression/demo_prompts.py` for prompt reference
2. Use Copilot Chat to type each prompt iteration
3. Show how results improve dramatically

### 3. Productivity Patterns (Section 3 – 18 min)
1. `03-productivity-patterns/transaction_processor.py` → Explain + Document
2. `03-productivity-patterns/account_service.py` → Refactor + Generate Tests
3. `03-productivity-patterns/payment_gateway.py` → Debug + Multi-step

### 4. Pandas Scenario (Section 4 – 25 min)
1. Open `04-pandas-scenario/pandas_demo.py`
2. Follow the numbered steps (each has naive + improved prompts)
3. Use Copilot Chat to generate code at each step
4. Show the prompt progression throughout

### 5. Hands-on Lab (Section 5 – 10 min)
- Participants open `05-hands-on-lab/lab_exercise.py`
- They use Copilot Chat to complete the task
- Solution in `lab_solution.py` (for facilitator reference only)

## Pre-Flight Checklist

- [ ] Python 3.9+ available
- [ ] `pip install pandas numpy pytest` completed
- [ ] `financial_transactions.csv` exists in both `04-pandas-scenario/` and `05-hands-on-lab/`
- [ ] VS Code font size ≥ 16
- [ ] Copilot extension active and responding
- [ ] All files open in correct tab order
- [ ] Chat history cleared
