"""
Track A: Pandas & Financial Data — Hands-on Lab

═══════════════════════════════════════════════════════════════════
TIME: ~25 minutes
GOAL: Practice prompt progression on real data engineering tasks
AUDIENCE: Data engineers, analysts, Python developers
═══════════════════════════════════════════════════════════════════

WHAT YOU'LL DO:
  Part 1: Dataset Exploration (5 min) — practice naive → constrained prompts
  Part 2: Data Transformation (7 min) — clean and enrich data
  Part 3: Aggregation & Analysis (5 min) — business metrics
  Part 4: Refactor & Test (5 min) — production-ready code + tests
  
  Stretch goals available if you finish early!

HOW TO USE COPILOT:
  - Open Copilot Chat: Ctrl+Alt+B (or click the chat icon)
  - Remember: Intent + Context + Constraints = Better Results
  - If the output isn't right, ITERATE on your prompt (don't fix manually!)

═══════════════════════════════════════════════════════════════════
"""

import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("financial_transactions.csv", parse_dates=["timestamp"])

print(f"Dataset loaded: {len(df)} transactions")
print(f"Columns: {list(df.columns)}")
print(f"Date range: {df['timestamp'].min()} to {df['timestamp'].max()}")
print(f"Customers: {df['customer_id'].nunique()}")
print()


# ════════════════════════════════════════════════════════════════════════════
# PART 1: DATASET EXPLORATION (5 min)
# ════════════════════════════════════════════════════════════════════════════
#
# EXERCISE: Try the PROMPT PROGRESSION technique.
#
# Step 1 — Type this NAIVE prompt in Copilot Chat:
#     "explore this dataset"
#   → Observe: is the result useful? (Probably just .head(), .describe())
#
# Step 2 — Now try a CONTEXTUAL prompt:
#     "I have a financial transactions DataFrame `df` with columns:
#      transaction_id, customer_id, amount, currency, transaction_type,
#      merchant_category, timestamp, is_flagged, account_balance.
#      Summarize this dataset: shape, data types, missing values, distributions."
#
# Step 3 — Now try a CONSTRAINED prompt:
#     "I have a financial transactions DataFrame `df` with columns:
#      transaction_id, customer_id, amount, currency, transaction_type,
#      merchant_category, timestamp, is_flagged, account_balance.
#
#      Provide a data quality report:
#      - Missing values per column (count and percentage)
#      - Duplicate transaction_id check
#      - Statistical outliers in amount (IQR method)
#      - Date range coverage
#      - Distribution of categorical fields (value counts)
#      Format as printed output with clear section headers."
#
# ═══ YOUR CODE HERE (paste Copilot's output below) ═══




# ════════════════════════════════════════════════════════════════════════════
# PART 2: DATA TRANSFORMATION (7 min)
# ════════════════════════════════════════════════════════════════════════════
#
# EXERCISE: Write a CONSTRAINED prompt that asks Copilot to:
#   1. Convert timestamp to datetime, localize to UTC
#   2. Create amount_eur column (convert USD at 0.92, GBP at 1.17)
#   3. Fill missing merchant_category with 'UNKNOWN' (don't drop rows)
#   4. Remove duplicate transaction_ids (keep first)
#   5. Clip amount to [0, 500000] range (regulatory cap)
#
# TIPS:
#   - Specify: use method chaining
#   - Specify: return a new DataFrame (don't modify in place)
#   - Specify: add inline comments
#
# HINT (if stuck, expand in the lab guide):
#   "Transform the transactions DataFrame `df` with these requirements:
#    1. Convert timestamp to datetime, localize to UTC
#    2. Create amount_eur column (convert USD at 0.92, GBP at 1.17)
#    3. Fill missing merchant_category with 'UNKNOWN' (don't drop rows)
#    4. Remove exact duplicate transaction_ids (keep first)
#    5. Clip amount to [0, 500000] range (regulatory cap)
#    Use method chaining. Add inline comments. Return a new DataFrame."
#
# ═══ YOUR CODE HERE ═══




# ════════════════════════════════════════════════════════════════════════════
# PART 3: AGGREGATION & ANALYSIS (5 min)
# ════════════════════════════════════════════════════════════════════════════
#
# EXERCISE: Create a monthly customer spending summary.
#
# Your prompt should produce:
#   - Group by customer_id and month
#   - Metrics: total_amount, transaction_count, unique_merchants,
#              avg_transaction, max_transaction
#   - Month-over-month growth rate for total_amount
#   - Sorted by customer_id and month
#
# ═══ YOUR CODE HERE ═══




# ════════════════════════════════════════════════════════════════════════════
# PART 4: REFACTOR & TEST (5 min)
# ════════════════════════════════════════════════════════════════════════════
#
# EXERCISE:
#   1. Ask Copilot to refactor your transformation code into a function
#      with type hints, docstring, and input validation
#   2. Ask Copilot to generate pytest tests for that function
#
# HINT for refactoring:
#   "Refactor the data transformation into a function:
#    - Name: transform_transactions
#    - Input: pd.DataFrame
#    - Output: pd.DataFrame
#    - Add type hints, Google-style docstring, input validation
#    - Raise ValueError if required columns are missing"
#
# HINT for tests:
#   "Generate pytest tests for transform_transactions:
#    - Happy path with valid data
#    - Currency conversion accuracy
#    - Missing merchant_category is filled
#    - Duplicates removed (keep first)
#    - Amount clipping at boundaries
#    - Empty DataFrame (should return empty, not error)
#    Use pytest fixtures for sample data."
#
# ═══ YOUR CODE HERE ═══




# ════════════════════════════════════════════════════════════════════════════
# STRETCH GOALS (if you finish early)
# ════════════════════════════════════════════════════════════════════════════

# STRETCH 1: Feature Engineering
# Create fraud detection features:
#   - transaction_hour: hour of day
#   - amount_zscore: z-score per customer group
#   - days_since_last_txn: days since customer's previous transaction
#   - rolling_7d_avg: 7-day rolling average per customer


# STRETCH 2: Anomaly Detection
# Flag customers whose average transaction in any category is > 3 std devs
# above the category mean.


# STRETCH 3: Try Track B!
# Switch to the Full-Stack lab for a different Copilot workflow.
