# Hands-on Lab: Customer Spending Pattern Analysis

## Overview
- **Duration:** ~10 minutes (8 min working, 2 min debrief)
- **Difficulty:** Beginner-friendly with advanced stretch goals
- **Dataset:** Same `financial_transactions.csv` from the demo

---

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

## Exercise: Identify Top Spending Customers by Category

### Your Task

Using GitHub Copilot, write code that:

1. **Filters** the dataset to only completed transactions (exclude `is_flagged == True`)
2. **Groups** transactions by `customer_id` and `merchant_category`
3. **Calculates** total spending and transaction count per group
4. **Finds** the top 5 customers by total spending in each merchant category
5. **Creates** a summary DataFrame with columns: `customer_id`, `merchant_category`, `total_spent`, `num_transactions`, `avg_transaction`

### Instructions

1. Open Copilot Chat (Ctrl+Alt+I or click the chat icon)
2. Write a prompt that describes what you want—use the techniques from the session:
   - Be specific about the input DataFrame structure
   - State your constraints clearly
   - Specify the output format
3. Review the generated code
4. Run it and verify the output makes sense
5. If the output isn't right, **iterate on your prompt** (don't just fix the code manually)

### Hints (if you're stuck)

<details>
<summary>Hint 1: Starter prompt</summary>

```
I have a pandas DataFrame `df` with columns: customer_id, merchant_category, 
amount, is_flagged, timestamp.

Filter out flagged transactions, then find the top 5 customers by total 
spending in each merchant_category.
```
</details>

<details>
<summary>Hint 2: Better prompt with constraints</summary>

```
Using the transactions DataFrame `df`, create a spending analysis:
1. Filter: keep only rows where is_flagged == False
2. Group by customer_id and merchant_category
3. Aggregate: sum of amount (as total_spent), count (as num_transactions)
4. Calculate avg_transaction = total_spent / num_transactions
5. Rank customers within each merchant_category by total_spent
6. Keep only top 5 per category

Return a clean DataFrame sorted by merchant_category then rank.
Use pandas groupby and rank functions. Reset the index.
```
</details>

### Expected Output

Your result should look something like:

| customer_id | merchant_category | total_spent | num_transactions | avg_transaction |
|-------------|-------------------|-------------|------------------|-----------------|
| CUST_0042 | GROCERY | 45,230.50 | 156 | 290.00 |
| CUST_0118 | GROCERY | 38,910.25 | 142 | 274.01 |
| ... | ... | ... | ... | ... |
| CUST_0007 | TRAVEL | 89,450.00 | 23 | 3,889.13 |

(Exact values will differ based on synthetic data generation)

---

## Stretch Goals (Advanced Users)

If you finish early, try these additional challenges:

### Stretch 1: Add Time Intelligence
Add a column showing each customer's spending **trend** (increasing/decreasing/stable) based on comparing their last 30 days vs. prior 30 days.

*Prompt tip: specify the date comparison logic and how to classify the trend.*

### Stretch 2: Anomaly Detection
Flag customers whose average transaction in any category is more than 3 standard deviations above the category mean.

*Prompt tip: ask Copilot to calculate per-category statistics first, then compare.*

### Stretch 3: Refactor and Test
Take your working code and:
1. Ask Copilot to refactor it into a function with type hints
2. Ask Copilot to generate pytest tests for that function

*Prompt tip: specify edge cases like empty DataFrames or categories with fewer than 5 customers.*

---

## Debrief Questions (Group Discussion)

After the exercise:
- What prompting strategy worked best for you?
- Did you need to iterate? What did you change?
- What surprised you about Copilot's output?
- For advanced users: what would you do differently in production code?

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Copilot not suggesting anything | Check your Copilot extension is active (look for the icon in the status bar) |
| Output doesn't match expected | Review the filtering step—ensure `is_flagged == False` not `is_flagged != True` |
| Import errors | Run `pip install pandas numpy` in your terminal |
| Dataset not loading | Check file path; try absolute path to the CSV |
| Copilot gives irrelevant code | Add more context: mention the DataFrame name and column names explicitly |
