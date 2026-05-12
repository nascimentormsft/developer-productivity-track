# Demo Plan

## Demo 1: Quick Win (Section 1 – Fundamentals)

### Objective
Show Copilot's value in under 3 minutes with two simple, relatable tasks.

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

### Step-by-Step

**Pattern 1: Code Explanation (3 min)**
1. Open `transaction_processor.py`
2. Select `process_batch_transactions()` (lines 42–137)
3. Open Copilot Chat, type: `/explain`
4. Show structured explanation with identified concerns

**Pattern 2: Refactoring (3 min)**
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

**Pattern 3: Test Generation (3 min)**
1. With the refactored function still visible
2. Copilot Chat:
   ```
   /tests Generate pytest tests for the refactored validate_account_status function.
   Include: happy path, boundary cases, invalid inputs, and edge cases for financial compliance.
   Use parametrize for the boundary cases.
   ```
3. Show generated tests with meaningful test names

**Pattern 4: Debugging (3 min)**
1. Open `payment_gateway.py` which has a subtle timezone bug
2. Copilot Chat:
   ```
   This function is returning incorrect timestamps for transactions processed
   near midnight UTC. The amounts are correct but settlement_date is sometimes
   one day off. Can you identify the bug and suggest a fix?
   ```
3. Show Copilot identifying the naive vs. aware datetime issue

**Pattern 5: Documentation (3 min)**
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

## Demo 4: Core Pandas Scenario (Section 4)

### Objective
End-to-end data engineering workflow demonstrating prompt progression throughout.

### Setup
- Jupyter notebook or Python script
- Synthetic dataset: `financial_transactions.csv` (pre-generated, ~10K rows)
- pandas, numpy imported

### Step-by-Step

**Step 1: Dataset Exploration (4 min)**

*Naive prompt:*
```
explore this dataset
```
→ Shows generic `.head()`, `.describe()` — not very useful

*Improved prompt:*
```
I have a financial transactions dataset loaded as `df` with columns:
transaction_id, customer_id, amount, currency, transaction_type, 
merchant_category, timestamp, is_flagged, account_balance.

Give me a comprehensive data quality report including:
- Missing values per column
- Data type validation
- Statistical outliers in amount
- Date range coverage
- Distribution of categorical fields
- Duplicate transaction_id check
```
→ Shows targeted, actionable exploration

**Step 2: Data Transformation (5 min)**

*Naive prompt:*
```
clean the data
```
→ Generic, removes rows — not what we want

*Constrained prompt:*
```
Transform the transactions DataFrame with these requirements:
1. Convert timestamp to datetime, localize to UTC
2. Create amount_eur column (convert USD at 0.92, GBP at 1.17)
3. Fill missing merchant_category with 'UNKNOWN' (don't drop rows)
4. Remove exact duplicate transaction_ids (keep first)
5. Clip amount to [0, 500000] range (regulatory cap)

Use method chaining. Add inline comments explaining each step.
Return a new DataFrame, don't modify in place.
```
→ Precise, production-ready transformation code

**Step 3: Feature Engineering (5 min)**

*Prompt:*
```
Create these features from the transactions DataFrame for fraud detection:
1. transaction_hour: hour of day from timestamp
2. amount_zscore: z-score of amount within each customer_id group
3. days_since_last_txn: days since customer's previous transaction
4. rolling_7d_avg: 7-day rolling average amount per customer
5. is_high_value: boolean, True if amount > 95th percentile for that merchant_category

Ensure the code handles edge cases:
- First transaction for a customer (days_since_last_txn = NaN is OK)
- Customers with fewer than 7 days of history
```
→ Demonstrates constrained prompting with edge case handling

**Step 4: Aggregation (4 min)**

*Prompt:*
```
Create a monthly customer summary from the transactions DataFrame:
- Group by customer_id and month (from timestamp)
- Calculate: total_amount, transaction_count, unique_merchants, avg_transaction, max_transaction
- Add month-over-month growth rate for total_amount
- Sort by customer_id and month

Output as a clean DataFrame with a MultiIndex reset.
```
→ Shows business-relevant aggregation

**Step 5: Refactoring (4 min)**

*Prompt:*
```
Refactor the data transformation code from above into a production-ready module:
- Create a function `transform_transactions(df: pd.DataFrame) -> pd.DataFrame`
- Create a function `engineer_features(df: pd.DataFrame) -> pd.DataFrame`  
- Create a function `build_customer_summary(df: pd.DataFrame) -> pd.DataFrame`
- Add type hints, docstrings, and input validation
- Each function should raise ValueError with a descriptive message if input is invalid
- Follow the single responsibility principle
```
→ From notebook exploration to production code

**Step 6: Test Generation (3 min)**

*Prompt:*
```
Generate pytest tests for the transform_transactions function:
- Test with valid input (happy path)
- Test currency conversion accuracy (USD, GBP → EUR)
- Test that missing merchant_category is filled
- Test that duplicates are removed (keep first)
- Test amount clipping at boundaries (0 and 500000)
- Test with empty DataFrame (should return empty, not error)
- Use pytest fixtures for sample data
- Include parametrize for currency conversion rates
```
→ Comprehensive test suite for data pipeline

### Key Talking Points
- "Notice how each step builds on the last—this is how real data work flows."
- "The prompt progression isn't just pedagogical—it's how you should actually work."
- "Start vague when exploring, get precise when building."

---

## Demo Environment Checklist

| Item | Status |
|------|--------|
| VS Code with Copilot extension (latest) | ☐ |
| Python 3.9+ environment | ☐ |
| pandas, numpy, pytest installed | ☐ |
| Synthetic dataset generated and accessible | ☐ |
| Demo files pre-prepared and tested | ☐ |
| Backup screenshots of all demo outputs | ☐ |
| Font size set to 16+ for visibility | ☐ |
| Dark theme for projector readability | ☐ |
| Copilot Chat panel visible | ☐ |
| Second monitor for speaker notes | ☐ |
