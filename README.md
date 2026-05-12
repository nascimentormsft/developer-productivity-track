# Developer Productivity with GitHub Copilot – Workshop

A 90-minute hands-on workshop teaching engineers how to become more productive using GitHub Copilot in real developer workflows, with a focus on Python and pandas for data engineering.

## Prerequisites

- **GitHub Copilot license** – active individual or business subscription
- **VS Code** – latest stable version ([download](https://code.visualstudio.com/))
- **Python 3.9+** – required for all demos and the hands-on lab
- **Basic Python knowledge** – variables, functions, lists, dictionaries

## Setup

### 1. Install VS Code Extensions

Open VS Code and install:
- [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
- [GitHub Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### 2. Install Python

**Windows**
```powershell
# Option A: Microsoft Store
winget install Python.Python.3.12

# Option B: python.org installer
# Download from https://www.python.org/downloads/ and check "Add to PATH"
```

**macOS**
```bash
brew install python@3.12
```

**Linux (Debian/Ubuntu)**
```bash
sudo apt update && sudo apt install python3 python3-pip python3-venv
```

### 3. Create a Virtual Environment and Install Dependencies

**Windows (PowerShell)**
```powershell
cd <repo-root>
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install pandas numpy pytest
```

**macOS / Linux**
```bash
cd <repo-root>
python3 -m venv .venv
source .venv/bin/activate
pip install pandas numpy pytest
```

### 4. Generate the Synthetic Dataset

The dataset CSV is included in the repo, but if you need to regenerate it:

```bash
cd demo/04-pandas-scenario
python generate_dataset.py
```

This creates `financial_transactions.csv` (10,000 synthetic transactions). Copy it to the lab folder:

```bash
cp demo/04-pandas-scenario/financial_transactions.csv demo/05-hands-on-lab/
```

### 5. Verify Everything Works

```bash
python -c "import pandas; import numpy; print('Ready!')"
```

## Workshop Structure

| # | Section | Time | Folder |
|---|---------|------|--------|
| 1 | Introduction & Fundamentals | 12 min | `demo/01-quick-win/` |
| 2 | Prompting Fundamentals | 15 min | `demo/02-prompt-progression/` |
| 3 | Developer Productivity Patterns | 20 min | `demo/03-productivity-patterns/` |
| 4 | Core Pandas Scenario | 25 min | `demo/04-pandas-scenario/` |
| 5 | Hands-on Lab | 10 min | `demo/05-hands-on-lab/` |
| 6 | Advanced Capabilities | 5 min | Slides only |
| 7 | Wrap-up | 3 min | Slides only |

## How to Use

### For Facilitators

1. **Preparation** – Read `workshop/06-facilitator-guide.md` for the full prep checklist, delivery tips, and fallback plans.
2. **Slides** – Follow the storyline in `workshop/02-slide-storyline-outline.md` to build your deck. Each slide has a title, key message, and speaker notes.
3. **Demos** – Open the files in the `demo/` folders in tab order. Each file has presenter instructions as comments at the top. Follow the prompts in sequence.
4. **Prompts** – Reference `workshop/05-prompt-library.md` for reusable prompts you can share with participants.
5. **Lab** – Distribute `demo/05-hands-on-lab/lab_exercise.py` to participants. Keep `lab_solution.py` for yourself.

### For Participants

1. Clone this repo and complete the setup above.
2. Open `demo/05-hands-on-lab/lab_exercise.py` in VS Code.
3. Follow the instructions in the file — use Copilot Chat to complete the analysis task.
4. Try the stretch goals if you finish early.

## Folder Overview

```
├── workshop/                          # Facilitator materials
│   ├── 00-workshop-overview.md        # Objectives, audience, business value
│   ├── 01-detailed-agenda.md          # Minute-by-minute timeline
│   ├── 02-slide-storyline-outline.md  # Slide deck blueprint
│   ├── 03-demo-plan.md               # Step-by-step demo instructions
│   ├── 04-hands-on-lab.md            # Lab design document
│   ├── 05-prompt-library.md          # Reusable prompt collection
│   ├── 06-facilitator-guide.md       # Prep, delivery tips, fallbacks
│   └── 07-synthetic-dataset-design.md # Dataset schema & generation details
│
├── demo/                              # Live demo & lab code
│   ├── 01-quick-win/                  # Comment-to-code + /explain demos
│   ├── 02-prompt-progression/         # Bad → better → best prompt demo
│   ├── 03-productivity-patterns/      # Refactoring, debugging, testing demos
│   ├── 04-pandas-scenario/            # End-to-end pandas walkthrough
│   └── 05-hands-on-lab/              # Participant exercise + solution
│
└── .gitignore
```
