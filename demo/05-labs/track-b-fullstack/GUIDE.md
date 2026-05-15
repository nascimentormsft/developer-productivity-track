
# Track B: Full-Stack API Lab

Welcome to the Full-Stack API Lab! This lab is designed to help you practice code exploration, debugging, refactoring, prompt engineering, and documentation automation using Copilot.

## Quick Reference: The 6 Phases

| Phase | Goal | Time | Key Activity |
|-------|------|------|______________|
| 1 | Explore backend & frontend | 5 min | Use Copilot to understand API and UI code |
| 2 | Find & fix the bug | 8-12 min | Debug and fix subtle logic error |
| 3 | Refactor code smells | 10-15 min | Apply team instructions to improve code quality |
| 4 | Implement repetitive features | 12-18 min | Create custom prompt to generate similar endpoints |
| 5 | Create documentation agent | 10-15 min | Build your own Mermaid diagram agent |
| 6 | Embed diagram in README | 5 min | Paste diagram and verify |

---

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start the backend API:

```bash
cd backend
uvicorn main:app --reload
```

3. In a new terminal, open the frontend:

```bash
# Open frontend/index.html in a browser or use VS Code Live Server
```

4. Verify API is running:

Visit `http://localhost:8000/health` — you should see `{"status": "healthy"}`

5. Open Copilot Chat (`Ctrl+Shift+I` or `Ctrl+Alt+B`) and ensure you're in **agent mode**.

---

## Phase 1: Explore Backend & Frontend Code (5 min)

### Goal
Understand the full-stack architecture and identify what's missing or unclear.

### Your Tasks

1. **Explain the backend API structure:**

In Copilot Chat, copy/paste this prompt:

```text
Explain the FastAPI backend structure in backend/:
- What files make up the API? (models, routes, main)
- What endpoints are currently available?
- What Pydantic models are defined?
- How are transactions stored and retrieved?

Be concise.
```

2. **Explain the frontend structure:**

```text
Explain the frontend structure:
- What does frontend/index.html contain?
- What does frontend/app.js do?
- How does the frontend communicate with the backend?
- What features are currently working?
```

3. **Understand the full data flow:**

```text
Trace a complete request/response flow:
1. User clicks "Load Transactions" button
2. What JavaScript function is called?
3. What API endpoint is hit?
4. What data is returned?
5. How is it rendered in the HTML?

Walk through this step by step.
```

### Expected Outcome
You understand the full-stack architecture and how frontend and backend communicate.

---

## Phase 2: Find & Fix the Bug (8-12 min)

### Goal
There is a **subtle logic bug** in the code that produces incorrect results. Find and fix it using Copilot.

### Your Tasks

1. **Run the backend and frontend:**

Visit `http://localhost:8000/docs` (Swagger UI) to see available endpoints. Try calling `/health` and `/transactions/` to see what data is returned.

2. **Identify the bug:**

Ask Copilot:

```text
In backend/routes/transactions.py, the get_customer_summary endpoint:
- Filters transactions by customer_id
- Calculates statistics (total, count, average, top category)
- Returns the results

There's a subtle logic bug in how transactions are filtered or counted.
Walk through the code mentally. What might be wrong?
Hint: Look at date filtering - does < vs <= make a difference?
```

3. **Debug further:**

```text
In get_customer_summary in backend/routes/transactions.py:
1. Find all transactions for a customer
2. Apply some filtering
3. Calculate statistics

Tell me: Are all transactions included in the summary calculation?
Or are some being excluded incorrectly?
What's the bug?
```

4. **Fix the bug:**

Once you identify it, ask Copilot:

```text
Fix the bug in get_customer_summary in backend/routes/transactions.py.
The issue is: [describe what you found]
Implement the fix while keeping all other logic the same.
Make sure the endpoint returns correct statistics for ALL transactions.
```

### Expected Outcome
The summary endpoint returns correct statistics. All transactions are included. Tests pass.

---

## Phase 3: Refactor Code Smells (10-15 min)

### Goal
Improve code quality by applying team standards from [track-b-instructions.md](track-b-instructions.md).

### Team Standards to Apply

From [track-b-instructions.md](track-b-instructions.md):
- ✅ Use Pydantic field validation (e.g., `Field(gt=0)` for positive integers)
- ✅ Move hardcoded values to config.py
- ✅ All routes must include docstrings with parameters and responses
- ✅ Use Google docstring style

### Your Tasks

1. **Identify code smells:**

```text
In backend/models.py and backend/routes/transactions.py, identify code quality issues:
- Missing field validation on Pydantic models
- Hardcoded values (port, CORS origins, limits)
- Routes missing docstrings explaining parameters and responses
- Missing type hints

List the issues you find.
```

2. **Create a config file:**

Ask Copilot:

```text
Create backend/config.py with:
- API_HOST = "0.0.0.0"
- API_PORT = 8000
- ALLOWED_ORIGINS = ["*"]
- MAX_LIMIT = 500

Then update backend/main.py to import and use these values instead of hardcoded ones.
```

3. **Refactor models with validation:**

```text
In backend/models.py, follow the team standards and update the Pydantic models:
- TransactionCreate: add Field validation
  - amount: must be > 0
  - customer_id: must have min_length=1
  - currency: must match pattern (EUR|USD|GBP)
  - transaction_type: must match pattern (PURCHASE|TRANSFER|WITHDRAWAL|REFUND)
  - merchant_category: must have min_length=1

Apply the team coding standards.
```

4. **Add docstrings to routes:**

```text
In backend/routes/transactions.py, add Google-style docstrings to all route functions:
- list_transactions
- get_transaction
- create_transaction
- get_customer_summary

Each docstring should explain:
- What the endpoint does
- Parameters and their types
- What it returns
- Any special cases (e.g., 404 errors)

Keep the bug fix from Phase 2.
```

5. **Verify everything still works:**

```bash
cd backend
pytest -v
```

### Expected Outcome
Models have validation. Config values are centralized. Routes have clear docstrings. Tests pass.

---

## Phase 4: Implement Repetitive Features Using Custom Prompt (12-18 min)

### Goal
Use prompt engineering to automate repetitive endpoint creation.

### Your Tasks

1. **Understand the repetitive pattern:**

The `get_customer_summary` endpoint follows a pattern:
- Filter by an ID or criteria
- Aggregate/group data
- Return a summary model
- Handle 404 cases

You need to create similar endpoints for different groupings.

2. **Create your custom prompt in [prompts/api-summary-endpoints.md](prompts/api-summary-endpoints.md):**

Expand the template with specific, detailed requirements:

```text
I need to implement three new endpoints following the same pattern as GET /transactions/summary/{customer_id}:

1. GET /transactions/summary/by-merchant/{merchant_category}
   - Filter transactions by merchant_category
   - Return same summary format with merchant metrics
   - Return 404 if no transactions found

2. GET /transactions/summary/by-date-range
   - Query parameters: start_date, end_date, group_by (day|week|month)
   - Return list of summaries grouped by the specified period
   - Validate date format

3. GET /transactions/top-merchants
   - Return top 10 merchants by transaction count
   - Include transaction count and total amount for each
   - Sort by count descending

Implement in backend/routes/transactions.py using the same patterns.
Follow team coding standards: validation, docstrings, proper error handling, Pydantic models.
Keep the existing bug fix.
```

3. **Use your custom prompt in Copilot:**

Copy your custom prompt from [prompts/api-summary-endpoints.md](prompts/api-summary-endpoints.md) and paste it into Copilot Chat. Copilot will generate all three endpoints.

4. **Test the implementation:**

```bash
cd backend
pytest tests/test_summaries.py -v
```

Or manually test via `http://localhost:8000/docs`

### Expected Outcome
Three new endpoints implemented. Tests pass. Code follows team standards. Endpoints return correct data.

---

## Phase 5: Create Your Own Documentation Agent (10-15 min)

### Goal
Build a custom Copilot agent that generates Mermaid diagrams of your API architecture.

### Your Tasks

1. **Create your agent file:**

Create a new file: `agents/api_architecture_agent.md`

2. **Define the agent with clear instructions:**

Ask Copilot to help you create the agent:

```text
I want to create a Copilot agent called "API Architecture Documentarian" that:
1. Analyzes FastAPI applications and creates Mermaid diagrams
2. Shows all endpoints, HTTP methods, and Pydantic models
3. Shows how frontend and backend communicate
4. Generates ONLY Mermaid syntax (no explanations)

Create agents/api_architecture_agent.md with clear instructions.
Include example Mermaid diagrams (flowchart and class diagram formats).
```

3. **Test your agent:**

In Copilot Chat, reference your agent:

```text
@agents/api_architecture_agent.md
Diagram the API architecture showing:
- All endpoints (GET /transactions, POST /transactions, GET /summary/{id}, etc.)
- The Pydantic models and their relationships
- How frontend and backend communicate
```

Copilot should generate a Mermaid diagram.

### Expected Outcome
Your agent generates valid Mermaid diagram code documenting the API architecture.

---

## Phase 6: Embed Diagram in README (5 min)

### Goal
Add your generated diagram to the project README.

### Your Tasks

1. **Generate the final diagram:**

Use your agent to generate one final comprehensive diagram.

2. **Edit [README.md](README.md):**

Find the section:

```
## Project Diagrams

Paste your generated Mermaid diagram here:
```

Replace with your actual Mermaid code.

3. **Preview in VS Code:**

Install: [Markdown Preview Mermaid Support](https://marketplace.visualstudio.com/items?itemName=vstirbu.vscode-mermaid-preview)

Open README.md and verify your diagram displays correctly.

### Expected Outcome
README contains your Mermaid diagram rendering correctly.

---

## Verification Checklist

- [ ] Phase 1: Can explain the full-stack architecture clearly
- [ ] Phase 2: Bug fixed; API returns correct summary statistics
- [ ] Phase 3: Config created; models have validation; routes have docstrings
- [ ] Phase 4: New endpoints implemented; `pytest tests/test_summaries.py -v` passes
- [ ] Phase 5: Custom agent generates valid Mermaid code
- [ ] Phase 6: Diagram embedded in README and displays correctly

---

## Key Takeaways

- **Copilot Explain**: Use to understand request/response flow across files
- **Copilot Debug**: Use specific prompts describing the issue to find subtle bugs
- **Copilot Refactor**: Reference team instructions to automate quality improvements
- **Custom Prompts**: Save effective prompts for generating similar endpoints
- **Custom Agents**: Define agent behavior to automate architectural documentation

---

## Getting Stuck?

- Use **Copilot Explain** to trace a specific API call from frontend to backend
- Test endpoints via `http://localhost:8000/docs` (Swagger UI)
- Run tests with `-v` flag for detailed output
- Ask Copilot to "preserve existing test behavior while applying [standard]"

Happy learning!
