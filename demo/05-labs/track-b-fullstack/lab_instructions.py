"""
Track B: Full-Stack Application — Hands-on Lab

═══════════════════════════════════════════════════════════════════
TIME: ~25 minutes
GOAL: Use Agent mode to add features across backend + frontend
AUDIENCE: App developers, full-stack engineers
═══════════════════════════════════════════════════════════════════

PROJECT STRUCTURE:
  backend/
  ├── main.py              ← FastAPI application entry point
  ├── models.py            ← Pydantic data models
  ├── routes/
  │   └── transactions.py  ← Transaction CRUD endpoints
  └── tests/
      └── test_transactions.py

  frontend/
  ├── index.html           ← Dashboard page
  ├── app.js               ← Frontend logic (fetch + render)
  └── styles.css

SETUP:
  1. Open this folder in VS Code
  2. Install dependencies:  pip install -r requirements.txt
  3. Start the backend:     cd backend && uvicorn main:app --reload
  4. Open frontend/index.html in a browser (or use Live Server extension)

═══════════════════════════════════════════════════════════════════

PART 1: UNDERSTAND THE EXISTING CODE (5 min)
─────────────────────────────────────────────
  1. Open backend/main.py and backend/routes/transactions.py
  2. Select all code, use /explain in Copilot Chat
  3. Ask: "What endpoints does this API expose? List as a table 
     with: method, path, description, request body, response format."
  
  Goal: Understand the API in < 2 minutes.

PART 2: ADD A NEW BACKEND ENDPOINT (8 min)
─────────────────────────────────────────────
  Switch to AGENT MODE and use this prompt:
  
  "Add a new endpoint GET /transactions/summary/{customer_id} 
   to the transactions router.
   
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
   - Add a basic test in tests/test_transactions.py"

  Watch Agent modify multiple files automatically!

PART 3: CONNECT THE FRONTEND (7 min)
─────────────────────────────────────────────
  Continue in AGENT MODE:
  
  "Update the frontend to add a Customer Summary feature:
   
   In app.js:
   - Add fetchCustomerSummary(customerId) calling 
     GET /transactions/summary/{customerId}
   - Display result in a card format
   
   In index.html:
   - Add input field for customer ID + Get Summary button
   - Add a div#customer-summary for results
   
   In styles.css:
   - Style the summary card with border, padding, readable layout
   
   Use fetch API. Show 'Customer not found' on 404."

PART 4: GENERATE INTEGRATION TESTS (5 min)
─────────────────────────────────────────────
  "Generate tests/test_integration.py that:
   - Uses pytest and httpx (async client for FastAPI)
   - Tests full flow: create transactions → get summary → verify
   - Tests 404 for non-existent customer
   - Uses a fixture that seeds known data
   - Marks tests with @pytest.mark.integration"

═══════════════════════════════════════════════════════════════════
STRETCH GOALS:
  1. Add comprehensive error handling (input validation, rate limiting)
  2. Add GET /transactions/trends/{customer_id} showing monthly trends
  3. Try Track A (Pandas lab)!
═══════════════════════════════════════════════════════════════════
"""
