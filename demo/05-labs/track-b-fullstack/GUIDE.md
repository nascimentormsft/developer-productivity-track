
# Track B: Full-Stack API Lab

Welcome to the Full-Stack API Lab! This lab is designed to mirror the learning flow in Track A while keeping the full-stack API experience: code exploration, debugging, refactoring, prompt engineering, and documentation automation with Copilot.

## Quick Reference: The 6 Phases

| Phase | Goal | Time | Key Activity |
|-------|------|------|--------------|
| 1 | Explore backend & frontend | 5 min | Trace request/response flow and explain what is implemented vs. TODO |
| 2 | Find & fix the bug | 8-12 min | Debug and fix a subtle logic error in summary calculation |
| 3 | Refactor code smells | 10-15 min | Apply team instructions to improve code quality |
| 4 | Implement repetitive features | 12-18 min | Build a reusable prompt template for similar endpoints |
| 5 | Create documentation agent | 10-15 min | Build a Mermaid diagram agent for the API architecture |
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
Understand the full-stack architecture, trace the data flow, and identify what is missing or unclear.

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
You understand the full-stack architecture, the request/response flow, and what each layer contributes.

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
The summary endpoint returns correct statistics. All relevant transactions are included. Tests pass.

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
python -m pytest -v tests/test_transactions.py
python -m pytest -v tests/test_summaries.py
```

### Expected Outcome
Models have validation. Config values are centralized. Routes have clear docstrings. Tests pass.

---

## Phase 4: Implement Repetitive Features Using Custom Prompt (12-18 min)

### Goal
Use prompt engineering to automate repetitive endpoint creation.

### Your Tasks

1. **Spot the repeated pattern:**

The `get_customer_summary` endpoint follows the same shape as the Track A aggregation exercise:
- Filter by a specific criterion
- Group and aggregate data
- Return a structured summary
- Handle empty results consistently

Before writing the prompt, separate what stays the same from what changes:
- What stays the same: summary shape, error handling, validation, docstrings, tests
- What changes: route name, grouping field, query parameters, and return schema

2. **Create a parameterized prompt in [prompts/api-summary-endpoints.md](prompts/api-summary-endpoints.md):**

Use placeholders so the same template can generate multiple endpoints with only configuration changes.

```text
---
description: "Generate a FastAPI endpoint for transaction summary aggregation"
---
Implement a Python endpoint in backend/routes/transactions.py using this configuration:

- Endpoint name: {endpoint_name}
- Route: {route}
- Input parameters: {input_parameters}
- Filter logic: {filter_logic}
- Group-by field: {group_by_field}
- Aggregate fields: {aggregate_fields}
- Return type: {return_type}
- Output schema: {output_schema}
- Error handling: {error_handling}

Requirements:
- Use FastAPI and Pydantic idioms
- Add complete type hints for parameters and return values
- Add a Google-style docstring
- Preserve existing behavior unless the config explicitly changes it
- Keep output deterministic and testable
- Follow team standards in track-b-instructions.md
```

Then call the template with different configurations for the three new endpoints.

If participants want a faster path, give them these copy/paste-ready samples to use with the template.

**Sample 1: Summary by transaction type for a customer**

```text
Implement a Python endpoint in backend/routes/transactions.py using this configuration:

- Endpoint name: get_customer_transaction_type_summary
- Route: /summary/{customer_id}/by-transaction-type
- Input parameters: customer_id: str
- Filter logic: Select transactions where t.customer_id == customer_id
- Group-by field: transaction_type
- Aggregate fields: count of transactions, sum of amount, average of amount
- Return type: dict
- Output schema: {
  "customer_id": str,
  "summary": [
    {
      "transaction_type": str,
      "total_transactions": int,
      "total_amount": float,
      "average_amount": float
    }
  ]
}
- Error handling: Return 404 if the customer has no transactions

Requirements:
- Use FastAPI and Pydantic idioms
- Add complete type hints for parameters and return values
- Add a Google-style docstring
- Preserve existing behavior unless the config explicitly changes it
- Keep output deterministic and testable
- Follow team standards in track-b-instructions.md
```

**Sample 2: Summary by merchant category for a customer**

```text
Implement a Python endpoint in backend/routes/transactions.py using this configuration:

- Endpoint name: get_customer_merchant_category_summary
- Route: /summary/{customer_id}/by-merchant-category
- Input parameters: customer_id: str
- Filter logic: Select transactions where t.customer_id == customer_id
- Group-by field: merchant_category
- Aggregate fields: count of transactions, sum of amount
- Return type: dict
- Output schema: {
  "customer_id": str,
  "summary": [
    {
      "merchant_category": str,
      "total_transactions": int,
      "total_amount": float
    }
  ]
}
- Error handling: Return 404 if the customer has no transactions

Requirements:
- Use FastAPI and Pydantic idioms
- Add complete type hints for parameters and return values
- Add a Google-style docstring
- Preserve existing behavior unless the config explicitly changes it
- Keep output deterministic and testable
- Follow team standards in track-b-instructions.md
```

**Sample 3: Summary by currency across all transactions**

```text
Implement a Python endpoint in backend/routes/transactions.py using this configuration:

- Endpoint name: get_currency_summary
- Route: /summary/by-currency
- Input parameters: none
- Filter logic: Use all transactions in memory
- Group-by field: currency
- Aggregate fields: count of transactions, sum of amount
- Return type: dict
- Output schema: {
  "summary": [
    {
      "currency": str,
      "total_transactions": int,
      "total_amount": float
    }
  ]
}
- Error handling: Return an empty summary list if there are no transactions

Requirements:
- Use FastAPI and Pydantic idioms
- Add complete type hints for parameters and return values
- Add a Google-style docstring
- Preserve existing behavior unless the config explicitly changes it
- Keep output deterministic and testable
- Follow team standards in track-b-instructions.md
```

3. **Use your custom prompt in Copilot:**

Copy the template from [prompts/api-summary-endpoints.md](prompts/api-summary-endpoints.md) and paste it into Copilot Chat with the configuration you want to generate.

4. **Test the implementation:**

```bash
cd backend
python -m pytest -v tests/test_summaries.py
```

Or manually test via `http://localhost:8000/docs`.

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

- [ ] Phase 1: Can explain the code structure clearly and trace a request end to end
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
