"""
Hands-on Lab: Customer Spending Pattern Analysis

INSTRUCTIONS FOR PARTICIPANTS:
──────────────────────────────────────────────────────────────────

Welcome! In this exercise you'll use GitHub Copilot to analyze
customer spending patterns in a financial transactions dataset.

TIME: ~8 minutes
GOAL: Use Copilot Chat to write pandas code that identifies
      top spending customers by merchant category.

──────────────────────────────────────────────────────────────────

YOUR TASK:
1. Filter the dataset to only completed transactions (exclude flagged ones)
2. Group transactions by customer_id and merchant_category
3. Calculate total spending and transaction count per group
4. Find the top 5 customers by total spending in each category
5. Create a summary DataFrame with columns:
   customer_id, merchant_category, total_spent, num_transactions, avg_transaction

──────────────────────────────────────────────────────────────────

HOW TO USE COPILOT:
- Open Copilot Chat: Ctrl+Alt+I (or click the chat icon)
- Write a prompt describing what you want
- Remember: Intent + Context + Constraints = Better Results
- If the output isn't right, ITERATE on your prompt

──────────────────────────────────────────────────────────────────
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
# YOUR CODE HERE - Use Copilot to help you write the analysis!
# ════════════════════════════════════════════════════════════════════════════




# ════════════════════════════════════════════════════════════════════════════
# STRETCH GOAL 1: Add Time Intelligence
# ────────────────────────────────────────────────────────────────────────────
# Add a column showing each customer's spending TREND:
# - Compare last 30 days vs. prior 30 days
# - Classify as: "INCREASING", "DECREASING", or "STABLE"
# ════════════════════════════════════════════════════════════════════════════




# ════════════════════════════════════════════════════════════════════════════
# STRETCH GOAL 2: Anomaly Detection
# ────────────────────────────────────────────────────────────────────────────
# Flag customers whose average transaction in any category is more than
# 3 standard deviations above the category mean.
# ════════════════════════════════════════════════════════════════════════════




# ════════════════════════════════════════════════════════════════════════════
# STRETCH GOAL 3: Refactor and Test
# ────────────────────────────────────────────────────────────────────────────
# 1. Ask Copilot to refactor your code into a function with type hints
# 2. Ask Copilot to generate pytest tests for that function
# ════════════════════════════════════════════════════════════════════════════


