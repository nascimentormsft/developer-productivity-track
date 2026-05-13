# Pandas Financial Data Analysis Skill

## When to use
- Analyzing financial transaction DataFrames
- Building data quality reports
- Creating customer aggregations and summaries

## Domain rules
When analyzing financial transaction data:
- Always check for duplicate transaction IDs first
- Convert amounts to EUR using standard rates (USD: 0.92, GBP: 1.17)
- Flag transactions > EUR50,000 for regulatory review
- Use vectorized operations, never `iterrows()`
- Standard aggregation dimensions: customer, month, merchant category

## Data quality checks (always run first)
1. Missing values per column
2. Duplicate transaction_id values
3. Negative amounts (only valid for REFUND type)
4. Future timestamps (data error)
5. Orphan customer_ids (not in customer master)

## Standard output format
- Reset index on all GroupBy results
- Round monetary amounts to 2 decimal places
- Sort by primary grouping key, then by metric descending
- Use descriptive column names (e.g., `total_amount` not `sum`)
