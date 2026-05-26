# Demo Plan

## Demo 1: Quick Win (Section 1 – Fundamentals)

### Objective
Show Copilot's value in under 2 minutes with two simple, relatable tasks.

### Setup
- Open VS Code with a Python file (`demo_quickwin.py`)
- Have a pre-written complex function ready in a separate file for the "explain" demo

### Step-by-Step

**Part A: Generate from Comment**
1. Open `demo_quickwin.py` (the comment is already written)
2. Place your cursor at the end of the comment line and press Enter
3. Start typing: `def calc`
4. Let Copilot suggest the function body, Tab to accept
5. Point out: correct parameters, type hints, docstring, formula

**Part B: Explain Unfamiliar Code**
1. Open `legacy_risk_calculator.py` (pre-prepared file with a dense 64-line function)
2. Select the entire function
3. Open Copilot Chat, type: `/explain`
4. Show the explanation: what it does, the algorithm, edge cases
5. Say: "This is 30 seconds vs. 15 minutes of reading and tracing."

### Key Talking Points
- "Notice I didn't have to leave my editor."
- "The explanation is in plain English—great for code reviews and onboarding."
- "We used Ask mode here — quick, one-shot interactions. We'll see Agent mode later in the customizations section."

---

## Demo 2: Prompt Progression (Section 2 – Prompting)

### Objective
Demonstrate how prompt quality directly affects output quality using three iterations.

### Setup
- Open a Python file for a data validation task
- Have the three prompts ready (can type live or paste)

### Step-by-Step

**Iteration 1: Bad Prompt**
1. In Copilot Chat, type:
   ```
   write a validation function
   ```
2. Show the result: generic, not useful, wrong assumptions
3. Say: "Copilot doesn't know what we're validating, for what context, or what 'valid' means."

**Iteration 2: Better Prompt**
1. Type:
   ```
   Write a Python function that validates a financial transaction record.
   A transaction has: amount (float), currency (str), timestamp (datetime), account_id (str).
   Return True if valid, False otherwise.
   ```
2. Show the result: more relevant but still making assumptions about rules
3. Say: "Better—it knows the domain. But what are our validation rules?"

**Iteration 3: Best Prompt**
1. Type:
   ```
   Write a Python function `validate_transaction` that checks a financial transaction dict with these rules:
   - amount must be positive and ≤ 1,000,000
   - currency must be one of: EUR, USD, GBP
   - timestamp must not be in the future
   - account_id must match pattern: 2 letters + 8 digits (e.g., NL12345678)
   
   Return a tuple of (is_valid: bool, errors: list[str]).
   Use early returns. Include type hints. Follow Google docstring style.
   ```
2. Show the result: precise, usable, matches requirements
3. Say: "Same task. The difference is how we asked."

### Key Talking Points
- "Intent → Context → Constraints. That's the formula."
- "You're not 'being nice to the AI'—you're being precise like you would in a code review comment."

---

## Demo 3: Developer Productivity Patterns (Section 3)

### Objective
Rapid-fire demos showing six patterns in real code scenarios.

### Setup
- Pre-prepared Python files simulating a financial services codebase:
  - `transaction_processor.py` (main logic, some complexity)
  - `account_service.py` (needs refactoring)
  - `payment_gateway.py` (has a bug)

### Step-by-Step (6 patterns, ~2 min each + 2 min recap = 15 min total)

**Pattern 1: Code Explanation (2 min)**
1. Open `transaction_processor.py`
2. Select `process_batch_transactions()` (lines 42–137)
3. Open Copilot Chat, type: `/explain`
4. Show structured explanation with identified concerns

**Pattern 2: Refactoring (2 min)**
1. Open `account_service.py` with a function that has:
   - Nested if/else (4 levels deep)
   - Magic numbers
   - No error handling
2. Select the function, Ctrl+I:
   ```
   Refactor this to:
   - Use early returns to reduce nesting
   - Extract magic numbers to named constants
   - Add appropriate error handling for a financial service
   ```
3. Show the clean result

**Pattern 3: Test Generation (2 min)**
1. With the refactored function still visible
2. Copilot Chat:
   ```
   /tests Generate pytest tests for the refactored validate_account_status function.
   Include: happy path, boundary cases, invalid inputs, and edge cases for financial compliance.
   Use parametrize for the boundary cases.
   ```
3. Show generated tests with meaningful test names

**Pattern 4: Debugging (2 min)**
1. Open `payment_gateway.py` which has a subtle timezone bug
2. Copilot Chat:
   ```
   This function is returning incorrect timestamps for transactions processed
   near midnight UTC. The amounts are correct but settlement_date is sometimes
   one day off. Can you identify the bug and suggest a fix?
   ```
3. Show Copilot identifying the naive vs. aware datetime issue

**Pattern 5: Documentation (2 min)**
1. Select `process_batch_transactions()`
2. Inline chat: "Generate a comprehensive docstring including parameters, returns, raises, and a usage example"
3. Show the docstring generated in context

**Pattern 6: Multi-step Tasks (3 min)**
1. Copilot Chat:
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
2. Show Copilot providing a structured, multi-part solution

---

## Demo 4: Customizations (Section 4)

### Objective
Show how customizations replace repetitive tasks with reusable team assets, using real workflow scenarios (Terraform, CI/CD, Azure DevOps).

### Setup
- Pre-prepared customization files in a `.github/` folder structure
- Example Terraform module template
- Example Azure DevOps pipeline YAML

### Step-by-Step

**Part A: Custom Prompts (3 min)**
1. Show the `.github/prompts/` folder structure
2. Open a pre-prepared `terraform-module.prompt.md` file:
   ```markdown
   ---
   description: "Generate a Terraform module following team conventions"
   ---
   Create a Terraform module for {{resource_type}} with:
   - Variables file with descriptions and validation rules
   - Main resource configuration following our naming convention: {project}-{env}-{resource}
   - Outputs file exposing key attributes
   - Use azurerm provider
   - Apply standard tags: environment, team, cost-center, managed-by
   - Include a README.md with usage example
   ```
3. Invoke the prompt from Copilot Chat
4. Show how it generates a complete, convention-compliant Terraform module
5. Say: "This prompt is now available to every team member. No more Slack messages asking 'what's our Terraform template?'"

**Part B: Custom Instructions (3 min)**
1. Open `.github/copilot-instructions.md`:
   ```markdown
   # Team Coding Standards
   - Use Python type hints for all function signatures
   - Follow Google docstring style
   - Use `pathlib` instead of `os.path`
   - All Terraform resources must include standard tags
   - Azure DevOps pipeline YAML must include security scanning stages
   - Commit messages follow Conventional Commits format
   ```
2. Show how Copilot now automatically follows these rules when generating code
3. Create a quick Python function and show type hints + docstring appear automatically
4. Say: "Instructions are invisible guardrails. Set them once, forget about them."

**Part C: Skills (3 min)**
1. Open `.github/skills/pandas-analysis/SKILL.md` (pre-prepared):
   ```markdown
   # Pandas Financial Data Analysis Skill
   When analyzing financial transaction data:
   - Always check for duplicate transaction IDs first
   - Convert amounts to EUR using standard rates
   - Flag transactions > €50,000 for regulatory review
   - Use vectorized operations, never iterrows()
   - Standard aggregation: group by customer, month, category
   ```
2. Show how Copilot references this skill when working with pandas in the project
3. Say: "This is your team's institutional knowledge, encoded and shareable."

**Part D: Agents (4 min)**
1. Open `.github/agents/pipeline-scaffolder.agent.md` (pre-prepared):
   ```markdown
   ---
   description: "Scaffolds an Azure DevOps CI/CD pipeline with security scanning"
   tools: ["editFiles", "runInTerminal"]
   ---
   You are a CI/CD pipeline scaffolding agent.
   When asked to create a pipeline for a service:
   1. Create azure-pipelines.yml with standard stages: build, test, security-scan, deploy
   2. Include GitHub Advanced Security for Azure DevOps scanning
   3. Include Trivy container image scanning
   4. Add environment-specific deployment gates
   5. Configure artifact publishing
   ```
2. Invoke the agent: "Create a CI/CD pipeline for the payments-api service"
3. Show the agent creating the YAML file with all standard stages
4. Say: "This is a 30-minute task reduced to 30 seconds — and it follows your standards every time."

### Key Talking Points
- "Customizations scale your team's expertise. The senior engineer's knowledge is available to everyone."
- "Start with instructions (5 min to set up). Add prompts next. Skills and agents when you're ready."
- "Think about your Azure DevOps workflows — what do you configure repeatedly?"

---

## Demo Environment Checklist

| Item | Status |
|------|--------|
| VS Code with Copilot extension (latest) | ☐ |
| Python 3.9+ environment | ☐ |
| pandas, numpy, pytest, fastapi, uvicorn, httpx installed | ☐ |
| Synthetic dataset generated (`06-labs/track-a-pandas/`) | ☐ |
| Demo files 01–04 pre-prepared and tested | ☐ |
| `04-customizations/` folder openable as workspace root | ☐ |
| Track B backend starts (`uvicorn main:app --reload`) | ☐ |
| Backup screenshots of all demo outputs | ☐ |
| Font size set to 16+ for visibility | ☐ |
| Dark theme for projector readability | ☐ |
| Copilot Chat panel visible | ☐ |
| Second monitor for speaker notes | ☐ |
