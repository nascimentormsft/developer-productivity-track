# Hands-on Labs: Choose Your Adventure

## Overview
- **Duration:** ~25 minutes (22 min working, 3 min joint debrief)
- **Format:** Choose one track — or do both if you finish early
- **Difficulty:** Beginner-friendly core task with advanced stretch goals

Pick the lab that best matches your daily work:

| Track | Best for | Focus |
|-------|----------|-------|
| **A: Pandas & Financial Data** | Data engineers, analysts, Python developers | Prompt progression on data tasks |
| **B: Full-Stack Application** | App developers, full-stack engineers | Agent mode for multi-file changes |

---

---

# Track A: Pandas & Financial Data

## Scenario
You're a data engineer analyzing synthetic financial transactions. Use Copilot to explore, transform, and analyze the data — practicing prompt progression throughout.

## Setup Confirmation

Before you begin, confirm:
- [ ] VS Code is open with Copilot Chat available
- [ ] You have `financial_transactions.csv` loaded
- [ ] Python environment with pandas is active

Start with this code in a new file or notebook cell:

```python
import pandas as pd
import numpy as np

df = pd.read_csv("financial_transactions.csv", parse_dates=["timestamp"])
```

---

## Part 1: Dataset Exploration (5 min)

### Your Task
Use Copilot to understand the dataset: its shape, quality issues, and distributions.

### The Prompt Progression Exercise

**Step 1 — Naive prompt (try this first):**
```
explore this dataset
```
→ Observe what you get. Is it useful? Probably generic `.head()`, `.describe()`.

**Step 2 — Contextual prompt (add information):**
```
I have a financial transactions DataFrame `df` with columns:
transaction_id, customer_id, amount, currency, transaction_type, 
merchant_category, timestamp, is_flagged, account_balance.

Summarize this dataset: shape, data types, missing values, and value distributions.
```

**Step 3 — Constrained prompt (add requirements):**
```
I have a financial transactions DataFrame `df` with columns:
transaction_id, customer_id, amount, currency, transaction_type, 
merchant_category, timestamp, is_flagged, account_balance.

Provide a data quality report:
- Missing values per column (count and percentage)
- Duplicate transaction_id check
- Statistical outliers in amount (IQR method)
- Date range coverage
- Distribution of categorical fields (value counts)

Format as printed output with clear section headers.
```

Notice how each iteration produces dramatically better results.

---

## Part 2: Data Transformation (7 min)

### Your Task
Clean and transform the data into an analysis-ready state.

### Instructions
Write a constrained prompt that asks Copilot to:
1. Convert `timestamp` to datetime, localize to UTC
2. Create `amount_eur` column (convert USD at 0.92, GBP at 1.17)
3. Fill missing `merchant_category` with `'UNKNOWN'` (don't drop rows)
4. Remove duplicate `transaction_id` values (keep first)
5. Clip `amount` to [0, 500000] (regulatory cap)

**Tips:**
- Specify: use method chaining
- Specify: return a new DataFrame (don't modify in place)
- Specify: add inline comments

<details>
<summary>Hint: Full prompt</summary>

```
Transform the transactions DataFrame `df` with these requirements:
1. Convert timestamp to datetime, localize to UTC
2. Create amount_eur column (convert USD at 0.92, GBP at 1.17)
3. Fill missing merchant_category with 'UNKNOWN' (don't drop rows)
4. Remove exact duplicate transaction_ids (keep first)
5. Clip amount to [0, 500000] range (regulatory cap)

Use method chaining. Add inline comments explaining each step.
Return a new DataFrame, don't modify in place.
```
</details>

---

## Part 3: Aggregation & Analysis (5 min)

### Your Task
Create a monthly customer spending summary.

Write a prompt that produces:
- Group by `customer_id` and month
- Metrics: `total_amount`, `transaction_count`, `unique_merchants`, `avg_transaction`, `max_transaction`
- Month-over-month growth rate for `total_amount`
- Sorted by customer_id and month

<details>
<summary>Hint: Full prompt</summary>

```
Create a monthly customer summary from the transactions DataFrame:
- Group by customer_id and month (from timestamp)
- Calculate: total_amount, transaction_count, unique_merchants, avg_transaction, max_transaction
- Add month-over-month growth rate for total_amount
- Sort by customer_id and month

Output as a clean DataFrame with a reset index.
```
</details>

---

## Part 4: Refactor & Test (5 min)

### Your Task
Take your transformation code and make it production-ready.

1. Ask Copilot to refactor into a function with type hints and docstring
2. Ask Copilot to generate pytest tests for that function

<details>
<summary>Hint: Refactoring prompt</summary>

```
Refactor the data transformation code into a production-ready function:
- Function name: transform_transactions
- Input: pd.DataFrame
- Output: pd.DataFrame
- Add type hints, Google-style docstring, and input validation
- Raise ValueError if required columns are missing
```
</details>

<details>
<summary>Hint: Test generation prompt</summary>

```
Generate pytest tests for transform_transactions:
- Happy path with valid data
- Currency conversion accuracy
- Missing merchant_category is filled
- Duplicates are removed (keep first)
- Amount clipping at boundaries (0 and 500000)
- Empty DataFrame (should return empty, not error)
Use pytest fixtures for sample data.
```
</details>

---

## Stretch Goals (if you finish early)

### Stretch 1: Feature Engineering
Create fraud detection features: transaction_hour, amount_zscore per customer, days_since_last_txn, rolling_7d_avg.

### Stretch 2: Anomaly Detection
Flag customers whose average transaction in any category is > 3 standard deviations above the category mean.

### Stretch 3: Try Track B!
Switch to the Full-Stack lab for a completely different Copilot workflow.

---

---

# Track B: Full-Stack Application (Frontend + Backend)

## Scenario
You're working on a two-layer application: a Python backend API (FastAPI) and a frontend that consumes it. You need to add a new feature that spans both layers — using Agent mode to make multi-file changes efficiently.

## Setup Confirmation

Before you begin, confirm:
- [ ] VS Code is open with Copilot Chat available
- [ ] The lab project folder is open (contains `backend/` and `frontend/` directories)
- [ ] Python environment is active with FastAPI installed

The project structure:
```
lab-fullstack/
├── backend/
│   ├── main.py          # FastAPI application
│   ├── models.py        # Pydantic models
│   ├── routes/
│   │   └── transactions.py  # Transaction endpoints
│   └── tests/
│       └── test_transactions.py
└── frontend/
    ├── index.html
    ├── app.js           # Frontend logic
    └── styles.css
```

---

## Part 1: Understand the Existing Code (5 min)

### Your Task
Use Copilot to understand the backend API without reading every line.

### Instructions
1. Open `backend/main.py` and `backend/routes/transactions.py`
2. Select the code and ask Copilot:
   ```
   /explain
   ```
3. Then ask a follow-up:
   ```
   What endpoints does this API expose? What are the request/response formats?
   List them as a table with: method, path, description, request body, response format.
   ```

**Goal:** Understand the API surface in under 2 minutes (vs. 10+ minutes reading manually).

---

## Part 2: Add a New Backend Endpoint (8 min)

### Your Task
Add a new endpoint: `GET /transactions/summary/{customer_id}` that returns a spending summary for a specific customer.

### Instructions — Use Agent Mode

1. Switch to **Agent mode** in Copilot Chat
2. Prompt:
   ```
   Add a new endpoint GET /transactions/summary/{customer_id} to the transactions router.
   
   It should return:
   - total_transactions: int
   - total_amount: float
   - average_amount: float
   - top_category: str (most frequent merchant_category)
   - last_transaction_date: datetime
   
   Requirements:
   - Add a Pydantic response model in models.py
   - Add the route in routes/transactions.py
   - Return 404 if customer_id has no transactions
   - Add a basic test in tests/test_transactions.py
   ```
3. Watch Agent mode create/edit multiple files
4. Review the changes — do they look correct?

<details>
<summary>Hint: If Agent doesn't modify all files</summary>

Follow up with:
```
Also update the test file to include a test for the new endpoint 
with a mock customer that has 3 transactions.
```
</details>

---

## Part 3: Connect the Frontend (7 min)

### Your Task
Update the frontend to display the customer summary from your new endpoint.

### Instructions — Continue in Agent Mode

1. Prompt:
   ```
   Update the frontend to add a "Customer Summary" feature:
   
   In app.js:
   - Add a function fetchCustomerSummary(customerId) that calls 
     GET /transactions/summary/{customerId}
   - Display the result in a card format on the page
   
   In index.html:
   - Add an input field for customer ID and a "Get Summary" button
   - Add a div#customer-summary to display results
   
   In styles.css:
   - Style the summary card with a border, padding, and readable layout
   
   Use fetch API. Handle errors (show "Customer not found" for 404).
   ```
2. Review the multi-file changes Agent produces
3. If you have the backend running: test it in the browser!

---

## Part 4: Generate Integration Tests (5 min)

### Your Task
Ask Copilot to generate tests that verify the frontend-backend integration.

### Instructions
```
Generate a test file tests/test_integration.py that:
- Uses pytest and httpx (async client for FastAPI)
- Tests the full flow: create transactions → get summary → verify values
- Tests the 404 case for a non-existent customer
- Uses a test fixture that seeds the database with known data
- Marks tests with @pytest.mark.integration
```

---

## Stretch Goals (if you finish early)

### Stretch 1: Error Handling
Ask Agent to add comprehensive error handling: input validation, rate limiting hints, and meaningful error messages.

### Stretch 2: Add a Second Feature
Add a `GET /transactions/trends/{customer_id}` endpoint showing monthly spending trends, and display it as a simple list in the frontend.

### Stretch 3: Try Track A!
Switch to the Pandas lab for a data engineering perspective.

---

---

# Joint Debrief (Both Tracks)

## Discussion Questions

After the lab time:
- **Track A attendees:** What prompting strategy produced the best pandas code? Did iterating help?
- **Track B attendees:** How did Agent mode change your workflow vs. doing it manually? What did you need to review/fix?
- **Both:** What will you use first thing tomorrow at work?
- **Advanced users:** What guardrails would you add before using Agent mode on production code?

---

## Troubleshooting (Both Tracks)

| Issue | Solution |
|-------|----------|
| Copilot not suggesting anything | Check your Copilot extension is active (status bar icon) |
| Agent mode not available | Ensure you're using the latest Copilot Chat extension; switch model if needed |
| Import errors | Run `pip install pandas numpy fastapi httpx pytest` |
| Dataset not loading (Track A) | Check file path; try absolute path to the CSV |
| Backend won't start (Track B) | Check Python env is active; run `pip install -r requirements.txt` |
| Copilot gives irrelevant code | Add more context: mention file names, function names, and column names explicitly |
| Agent modifies wrong files | Be more specific about file paths in your prompt |
