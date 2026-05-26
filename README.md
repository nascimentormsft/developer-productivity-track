# Developer Productivity with GitHub Copilot – Workshop

A 90-minute hands-on workshop teaching engineers how to become more productive using GitHub Copilot in real developer workflows, tailored for financial services teams.

## Prerequisites

- **GitHub Copilot license** – active individual or business subscription
- **VS Code** – latest stable version ([download](https://code.visualstudio.com/))
- **Python 3.9+** – required for all demos and hands-on labs
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
winget install Python.Python.3.12
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

```powershell
cd <repo-root>
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install pandas numpy pytest fastapi uvicorn httpx
```

### 4. Generate the Synthetic Dataset (Track A lab)

```bash
cd demo/06-labs/track-a-pandas
python generate_dataset.py
```

### 5. Verify Everything Works

```bash
python -c "import pandas; import numpy; import fastapi; print('Ready!')"
```

## Workshop Structure

| # | Section | Time | Folder |
|---|---------|------|--------|
| 1 | Introduction & Fundamentals | 12 min | `demo/01-quick-win/` |
| 2 | Prompting Fundamentals | 15 min | `demo/02-prompt-progression/` |
| 3 | Developer Productivity Patterns | 15 min | `demo/03-productivity-patterns/` |
| 4 | Customizations | 15 min | `demo/04-customizations/` |
| 5 | Spec Kit Demo | 10 min | `demo/05-spec-kit/` |
| 6 | Hands-on Labs (choose your track) | 28 min | `demo/06-labs/` |
| 7 | Wrap-up | 5 min | Slides only |

## How to Use

### For Facilitators

1. **Preparation** – Read `workshop/06-facilitator-guide.md` for the full prep checklist, delivery tips, and fallback plans.
2. **Slides** – Follow the storyline in `workshop/02-slide-storyline-outline.md` to build your deck.
3. **Demos** – Follow `workshop/03-demo-plan.md`. Each demo file has presenter instructions as comments at the top.
4. **Prompts** – Reference `workshop/05-prompt-library.md` for reusable prompts you can share with participants.
5. **Labs** – Section 6 is "Choose Your Adventure" — participants pick Track A (Pandas) or Track B (Full-Stack), or both.

### For Participants

1. Clone this repo and complete the setup above.
2. Pick your lab track:
   - **Track A (Pandas):** Open `demo/06-labs/track-a-pandas/lab_exercise.py`
   - **Track B (Full-Stack):** Open `demo/06-labs/track-b-fullstack/lab_instructions.py`
3. Follow the instructions in the file — use Copilot Chat to complete each part.
4. Try the stretch goals or switch tracks if you finish early.

## Folder Overview

```
├── workshop/                              # Facilitator materials
│   ├── 00-workshop-overview.md            # Objectives, audience, business value
│   ├── 01-detailed-agenda.md              # Minute-by-minute timeline
│   ├── 02-slide-storyline-outline.md      # Slide deck blueprint
│   ├── 03-demo-plan.md                    # Step-by-step demo instructions
│   ├── 04-hands-on-lab.md                 # Lab design (Track A + Track B)
│   ├── 05-prompt-library.md               # Reusable prompt collection
│   ├── 06-facilitator-guide.md            # Prep, delivery tips, fallbacks
│   └── 07-synthetic-dataset-design.md     # Dataset schema & generation details
│
├── demo/                                  # Live demo & lab code
│   ├── 01-quick-win/                      # Comment-to-code + /explain demos
│   ├── 02-prompt-progression/             # Bad → better → best prompt demo
│   ├── 03-productivity-patterns/          # Refactoring, debugging, testing demos
│   ├── 04-customizations/                 # Instructions, prompts, skills, agents
│   ├── 05-spec-kit/                       # Spec-to-plan workflow demo
│   └── 06-labs/                           # Hands-on labs
│       ├── track-a-pandas/                # Data engineering with pandas
│       └── track-b-fullstack/             # FastAPI backend + frontend
│
├── context/                               # Workshop design context
│   └── initial-prompt.md                  # Original design brief
│
└── .gitignore
```
