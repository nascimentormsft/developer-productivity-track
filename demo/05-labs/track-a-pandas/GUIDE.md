# Hands-on Lab Track A: Pandas and Financial Data

**Time:** ~25 min  
**Goal:** Practice prompt progression on realistic data engineering tasks using Pandas.

---

## Setup

1. Open [lab_exercise.py](lab_exercise.py).
2. Confirm [financial_transactions.csv](financial_transactions.csv) exists in the same folder.
3. If you need to regenerate the dataset, run [generate_dataset.py](generate_dataset.py).
4. Run the exercise file:

```bash
python lab_exercise.py
```

5. Use Copilot Chat (`Ctrl+Alt+B`), make sure it is in agent mode.

---

## Part 1: Dataset Exploration (5 min)

Use prompt progression with the loaded `df` DataFrame in [lab_exercise.py](lab_exercise.py):

1. Start with this vague prompt:

```text
explore this dataset
```

2. Then use this contextual prompt:

```text
I have a financial transactions DataFrame `df` with columns:
transaction_id, customer_id, amount, currency, transaction_type,
merchant_category, timestamp, is_flagged, account_balance.
Summarize this dataset: shape, data types, missing values, distributions.
```

3. Then use this constrained prompt:

```text
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

Implement this inside the `part_1_dataset_exploration` function in lab_exercise.py,
replacing the `pass` statement.
```

What to compare:

1. How specific and actionable each response is.
2. Whether the final output can be used as a real quality report.

---

## Part 2: Data Transformation (7 min)

Prompt Copilot to produce a transformation pipeline that:

1. Converts `timestamp` to UTC-aware datetime.
2. Creates `amount_eur` from currency conversion rules.
3. Fills missing `merchant_category` with `UNKNOWN`.
4. Deduplicates by `transaction_id` keeping first.
5. Clips `amount` to `[0, 500000]`.

Constraints to include:

1. Use method chaining.
2. Return a new DataFrame.
3. Add brief inline comments.

Copy/paste prompt:

```text
Transform the transactions DataFrame `df` with these requirements:
1. Convert timestamp to datetime, localize to UTC
2. Create amount_eur column (convert USD at 0.92, GBP at 1.17)
3. Fill missing merchant_category with 'UNKNOWN' (do not drop rows)
4. Remove exact duplicate transaction_ids (keep first)
5. Clip amount to [0, 500000] range (regulatory cap)
Use method chaining. Return a new DataFrame.

Implement this inside the `part_2_data_transformation` function in lab_exercise.py,
replacing the `pass` statement.
```

---

## Part 3: Aggregation and Analysis (5 min)

Generate a monthly customer summary with:

1. Grouping by `customer_id` and month.
2. Metrics: `total_amount`, `transaction_count`, `unique_merchants`, `avg_transaction`, `max_transaction`.
3. Month-over-month growth rate.
4. Sorting by customer and month.

Copy/paste prompt:

```text
Create a monthly customer spending summary from DataFrame `df`.
Requirements:
- Group by customer_id and month
- Include metrics: total_amount, transaction_count, unique_merchants,
  avg_transaction, max_transaction
- Add month-over-month growth rate for total_amount per customer
- Sort by customer_id and month
Return a DataFrame.

Implement this inside the `part_3_aggregation_and_analysis` function in lab_exercise.py,
replacing the `pass` statement.
```

Expected outcome:

1. A clean analytic output you could pass to BI/reporting.

---

## Part 4: Refactor and Test (5 min)

Refactor the transformation logic into a reusable function and generate tests.

1. Function name: `transform_transactions`.
2. Include type hints and Google-style docstring.
3. Validate required columns and raise `ValueError` when missing.
4. Generate pytest tests for happy path, conversions, missing values, dedupe, clipping, and empty input.

Refactor prompt:

```text
Refactor the data transformation into a function:
- Name: transform_transactions
- Input: pd.DataFrame
- Output: pd.DataFrame
- Add type hints and Google-style docstring
- Add input validation
- Raise ValueError if required columns are missing

Implement this inside the `transform_transactions` function in lab_exercise.py,
replacing the `pass` statement.
```

Test generation prompt:

```text
Generate pytest tests for transform_transactions:
- Happy path with valid data
- Currency conversion accuracy
- Missing merchant_category is filled
- Duplicates removed (keep first)
- Amount clipping at boundaries
- Empty DataFrame returns empty (no error)
Use pytest fixtures for sample data.
```

Paste your code in `part_4_refactor_and_tests` inside [lab_exercise.py](lab_exercise.py).

---

## Stretch Goals

1. Engineer fraud features (`transaction_hour`, per-customer z-score, time-since-last transaction, rolling average).
2. Build an anomaly rule for category-level outliers.
3. Try Track B in [../track-b-fullstack](../track-b-fullstack).

Optional stretch prompt 1:

```text
Create fraud detection features from `df`:
- transaction_hour (hour of day)
- amount_zscore per customer
- days_since_last_txn per customer
- rolling_7d_avg amount per customer
Return an enriched DataFrame.
```

Optional stretch prompt 2:

```text
Flag customers whose average transaction in any merchant_category is more than
3 standard deviations above that category mean. Return flagged customers.
```

---

## Key Takeaway

Prompt quality directly impacts data quality and implementation speed.

Use this sequence for repeatable results:

1. Intent
2. Context
3. Constraints
