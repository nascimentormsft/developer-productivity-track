
# Track B: Full-Stack API Lab

Welcome to the Full-Stack API Lab! This lab will help you practice code exploration, debugging, refactoring, prompt engineering, and documentation automation using Copilot.

## Lab Phases

1. **Explore the codebase**: Use Copilot to explain the backend and frontend code, and identify what is missing.
2. **Find and fix the bug**: There is a subtle logic bug in the code that affects the results. Use Copilot to help you debug and fix it.
3. **Refactor code smells**: Use the provided team instructions to refactor the code for clarity and maintainability.
4. **Implement a repetitive feature**: Use prompt engineering to automate repetitive endpoint creation.
5. **Create a documentation agent**: Build your own Copilot agent to generate a Mermaid diagram of the API architecture.
6. **Embed your diagram in the README**: Use the VS Code Mermaid extension to preview your diagram, then paste the Mermaid code in the README under the Project Diagrams section.

---

## Setup

1. Install dependencies from [requirements.txt](requirements.txt).

```bash
pip install -r requirements.txt
```

2. Start backend API from [backend/main.py](backend/main.py):

```bash
cd backend
uvicorn main:app --reload
```

3. Open [frontend/index.html](frontend/index.html) in a browser (or Live Server).
4. Confirm the API health endpoint responds at `http://localhost:8000/health`.
5. Optional baseline test run:

```bash
cd backend
pytest -q
```

---

## Part 1: Explore the Codebase (5 min)

Use Copilot to explain the backend and frontend code, and identify what is missing.

---

## Part 2: Find and Fix the Bug (8 min)

There is a subtle logic bug in the code that affects the results. Use Copilot to help you debug and fix it.

---

## Part 3: Refactor Code Smells (7 min)

Use the provided team instructions to refactor the code for clarity and maintainability.

---

## Part 4: Implement a Repetitive Feature (10 min)

Use prompt engineering to automate repetitive endpoint creation. See the provided prompt template in the prompts directory.

---

## Part 5: Create a Documentation Agent (10 min)

Build your own Copilot agent to generate a Mermaid diagram of the API architecture. No starter agent is provided. Use Copilot and the README instructions to guide your implementation.

---

## Part 6: Embed Your Diagram in the README

Use the VS Code Mermaid extension to preview your diagram, then paste the Mermaid code in the README under the Project Diagrams section.

---

Happy learning!

Use Agent mode to implement `GET /transactions/summary/{customer_id}` with:

1. `total_transactions`
2. `total_amount`
3. `average_amount`
4. `top_category`
5. `last_transaction_date`

Requirements:

1. Add a response model in [backend/models.py](backend/models.py).
2. Add route logic in [backend/routes/transactions.py](backend/routes/transactions.py).
3. Return `404` when customer has no transactions.
4. Add at least one targeted test in [backend/tests/test_transactions.py](backend/tests/test_transactions.py).

Copy/paste prompt:

```text
Add a new endpoint GET /transactions/summary/{customer_id} to the transactions router.

It should return:
- total_transactions: int
- total_amount: float
- average_amount: float
- top_category: str (most frequent merchant_category)
- last_transaction_date: datetime

Requirements:
- Add a Pydantic response model in backend/models.py
- Add the route in backend/routes/transactions.py
- Return 404 if customer_id has no transactions
- Add a basic test in backend/tests/test_transactions.py
```

---

## Part 3: Connect Frontend (7 min)

Use Agent mode to wire UI to the new endpoint:

1. In [frontend/app.js](frontend/app.js), add `fetchCustomerSummary(customerId)`.
2. In [frontend/index.html](frontend/index.html), add customer input, action button, and `#customer-summary` container.
3. In [frontend/styles.css](frontend/styles.css), style a readable summary card.
4. Handle `404` with a clear `Customer not found` message.

Copy/paste prompt:

```text
Update the frontend to add a Customer Summary feature.

In frontend/app.js:
- Add fetchCustomerSummary(customerId) calling GET /transactions/summary/{customerId}
- Display result in a card format

In frontend/index.html:
- Add input field for customer ID and Get Summary button
- Add a div with id customer-summary for results

In frontend/styles.css:
- Style the summary card with border, padding, and readable layout

Use fetch API. Show "Customer not found" on 404.
```

Expected outcome:

1. You can enter a customer ID and see a rendered summary card.

---

## Part 4: Generate Integration Tests (5 min)

Ask Copilot to create [backend/tests/test_integration.py](backend/tests/test_integration.py) using `pytest` + `httpx`:

1. Seed known transactions in a fixture.
2. Test create flow then summary retrieval.
3. Test `404` for missing customer.
4. Mark tests with `@pytest.mark.integration`.

Copy/paste prompt:

```text
Generate backend/tests/test_integration.py that:
- Uses pytest and httpx async client for FastAPI
- Tests full flow: create transactions, get summary, verify values
- Tests 404 for non-existent customer
- Uses a fixture that seeds known data
- Marks tests with @pytest.mark.integration
```

Run tests from [backend](backend):

```bash
pytest -q
```

---

## Stretch Goals

1. Add request validation and centralized error handling.
2. Implement monthly trends endpoint: `GET /transactions/trends/{customer_id}`.
3. Add simple frontend loading/error states.

---

## Key Takeaway

Agent mode is most valuable when work spans multiple files and layers.

For reliable outcomes, prompt with:

1. Exact endpoint or feature name
2. File-level change targets
3. Validation and test requirements
