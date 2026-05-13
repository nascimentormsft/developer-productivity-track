# Demo Codebase - Developer Productivity with GitHub Copilot

## Folder Structure

```
demo/
├── 01-quick-win/                        # Section 1: Introduction (3 min)
│   ├── demo_quickwin.py                 # Empty file → let Copilot generate
│   └── legacy_risk_calculator.py        # Dense function to /explain
│
├── 02-prompt-progression/               # Section 2: Prompt Engineering (5 min)
│   └── demo_prompts.py                  # Bad → better → best prompt examples
│
├── 03-productivity-patterns/            # Section 3: Patterns (15 min)
│   ├── transaction_processor.py         # Explain + Document demos
│   ├── account_service.py              # Refactor + Test Generation demos
│   └── payment_gateway.py             # Debug + Multi-step demos
│
├── 04-customizations/                   # Section 4: Customizations (13 min)
│   ├── demo_instructions.py            # Presenter script with demo flow
│
├── ../.github/
│   ├── copilot-instructions.md         # Part B: Team coding standards
│   ├── agents/
│   │   └── pipeline-scaffolder.agent.md # Part D: CI/CD pipeline agent
│   ├── prompts/
│       └── terraform-module.prompt.md  # Part A: Reusable prompt template
│   └── skills/
│       └── pandas-analysis/SKILL.md    # Part C: Domain knowledge skill
│
└── 05-labs/                             # Section 5: Choose Your Adventure (25 min)
    ├── track-a-pandas/                  # Track A: Data engineering
    │   ├── generate_dataset.py          # Run once to create CSV
    │   ├── financial_transactions.csv   # 10K synthetic transactions
    │   └── lab_exercise.py             # Participant starter file
    │
    └── track-b-fullstack/               # Track B: Full-stack application
        ├── lab_instructions.py          # Participant exercise guide
        ├── requirements.txt             # Python dependencies
        ├── backend/
        │   ├── main.py                  # FastAPI application
        │   ├── models.py                # Pydantic models
        │   ├── routes/
        │   │   └── transactions.py      # Transaction CRUD endpoints
        │   └── tests/
        │       └── test_transactions.py # Existing tests
        └── frontend/
            ├── index.html               # Dashboard page
            ├── app.js                   # Frontend logic
            └── styles.css               # Styling
```

## Demo Flow (Facilitator Demos: Sections 1–4)

### 1. Quick Win (Section 1 – 3 min)
1. Open `01-quick-win/demo_quickwin.py` → cursor below comment → Tab to accept
2. Open `01-quick-win/legacy_risk_calculator.py` → select function → `/explain`

### 2. Prompt Progression (Section 2 – 5 min)
1. Open `02-prompt-progression/demo_prompts.py` for prompt reference
2. Type each prompt iteration in Copilot Chat
3. Show how results improve with intent + context + constraints

### 3. Productivity Patterns (Section 3 – 15 min)
1. `03-productivity-patterns/transaction_processor.py` → Explain + Document
2. `03-productivity-patterns/account_service.py` → Refactor + Generate Tests
3. `03-productivity-patterns/payment_gateway.py` → Debug + Multi-step

### 4. Customizations (Section 4 – 13 min)
Keep the repository root open as workspace root. Follow `04-customizations/demo_instructions.py`:
- **Part A:** Invoke the Terraform prompt template (3 min)
- **Part B:** Show instructions enforcing coding standards (3 min)
- **Part C:** Use the pandas skill for domain-aware analysis (3 min)
- **Part D:** Agent mode + pipeline scaffolder agent (4 min)

## Hands-on Labs (Section 5 – 25 min)

Participants choose one (or both):

### Track A: Pandas & Financial Data
- Open `05-labs/track-a-pandas/lab_exercise.py`
- Generate the dataset first: `python generate_dataset.py`
- Practice prompt progression on data engineering tasks

### Track B: Full-Stack Application
- Open `05-labs/track-b-fullstack/`
- Install: `pip install -r requirements.txt`
- Start backend: `cd backend && uvicorn main:app --reload`
- Use Agent mode to add features across backend + frontend

## Pre-Flight Checklist

- [ ] Python 3.9+ available
- [ ] `pip install pandas numpy pytest fastapi uvicorn httpx` completed
- [ ] `financial_transactions.csv` generated in `05-labs/track-a-pandas/`
- [ ] Track B backend starts successfully (`uvicorn main:app --reload`)
- [ ] VS Code font size ≥ 16
- [ ] Copilot extension active and responding
- [ ] Copilot Chat models available (Claude, GPT-4o)
- [ ] All demo files open in correct tab order
- [ ] Chat history cleared
