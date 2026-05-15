import pandas as pd

df = pd.read_csv("financial_transactions.csv", parse_dates=["timestamp"])

print(f"Dataset loaded: {len(df)} transactions")
print(f"Columns: {list(df.columns)}")
print(f"Date range: {df['timestamp'].min()} to {df['timestamp'].max()}")
print(f"Customers: {df['customer_id'].nunique()}")
print()


# =============================================================================
# Part 1: Dataset Exploration
# Goal: Summarize shape, data types, missing values, duplicates, and
#       statistical outliers. Format with clear section headers.
# =============================================================================
def part_1_dataset_exploration(df: pd.DataFrame) -> None:
    # TODO: implement dataset exploration here
    pass


# =============================================================================
# Part 2: Data Transformation
# Goal: Build a transformation pipeline using method chaining that returns a
#       new DataFrame with UTC timestamps, EUR amounts, filled categories,
#       deduplicated rows, and clipped amounts.
# =============================================================================
def part_2_data_transformation(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: implement transformation pipeline here
    pass


# =============================================================================
# Part 3: Aggregation and Analysis
# Goal: Return a monthly customer spending summary with total_amount,
#       transaction_count, unique_merchants, avg_transaction, max_transaction,
#       and month-over-month growth rate. Sort by customer_id and month.
# =============================================================================
def part_3_aggregation_and_analysis(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: implement aggregation and analysis here
    pass


# =============================================================================
# Part 4: Refactor and Tests
# Goal: Refactor the transformation from Part 2 into a reusable
#       transform_transactions function with type hints, Google-style
#       docstring, and input validation. See tests/test_transform.py.
# =============================================================================
def transform_transactions(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: implement reusable transform_transactions function here
    pass


# =============================================================================
# Stretch Goal 1: Fraud Feature Engineering  (optional)
# Goal: Engineer transaction_hour, amount_zscore per customer,
#       days_since_last_txn, and rolling_7d_avg. Return enriched DataFrame.
# =============================================================================
def stretch_goal_1_fraud_features(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: implement fraud feature engineering here
    pass


# =============================================================================
# Stretch Goal 2: Category Anomaly Detection  (optional)
# Goal: Flag customers whose average transaction in any merchant_category
#       is more than 3 standard deviations above that category mean.
# =============================================================================
def stretch_goal_2_category_anomaly(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: implement category anomaly detection here
    pass


# =============================================================================
# Run all parts — uncomment each line as you complete it
# =============================================================================
if __name__ == "__main__":
    part_1_dataset_exploration(df)

    # df_clean = part_2_data_transformation(df)
    # print(df_clean.head())

    # summary = part_3_aggregation_and_analysis(df_clean)
    # print(summary.head())

    # df_features = stretch_goal_1_fraud_features(df_clean)
    # print(df_features.head())

    # flagged = stretch_goal_2_category_anomaly(df_clean)
    # print(flagged)
