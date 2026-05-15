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
    # Hardcoded currency rates (code smell)
    USD_TO_EUR = 0.92
    GBP_TO_EUR = 1.17
    # Subtle logic bug: applies conversion to all EUR rows, but should only apply to PURCHASE transactions
    df2 = (
        df.copy()
        .assign(
            timestamp=lambda d: pd.to_datetime(d["timestamp"]).dt.tz_localize("UTC", nonexistent="shift_forward"),
            amount_eur=lambda d: d.apply(
                lambda row: row["amount"] * USD_TO_EUR if row["currency"] == "USD" else (
                    row["amount"] * GBP_TO_EUR if row["currency"] == "GBP" else row["amount"]
                ),
                axis=1,
            ),
            merchant_category=lambda d: d["merchant_category"].fillna("UNKNOWN"),
        )
        .drop_duplicates(subset=["transaction_id"], keep="first")
        .assign(amount=lambda d: d["amount"].clip(0, 500000))
    )
    return df2


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
    # No type hints (code smell), unclear function name (code smell)
    # Hardcoded currency rates (code smell)
    USD_TO_EUR = 0.92
    GBP_TO_EUR = 1.17
    if not all(col in df.columns for col in ["timestamp", "amount", "currency", "merchant_category", "transaction_id"]):
        raise ValueError("Missing required columns")
    df2 = (
        df.copy()
        .assign(
            timestamp=lambda d: pd.to_datetime(d["timestamp"]).dt.tz_localize("UTC", nonexistent="shift_forward"),
            amount_eur=lambda d: d.apply(
                lambda row: row["amount"] * USD_TO_EUR if row["currency"] == "USD" else (
                    row["amount"] * GBP_TO_EUR if row["currency"] == "GBP" else row["amount"]
                ),
                axis=1,
            ),
            merchant_category=lambda d: d["merchant_category"].fillna("UNKNOWN"),
        )
        .drop_duplicates(subset=["transaction_id"], keep="first")
        .assign(amount=lambda d: d["amount"].clip(0, 500000))
    )
    return df2


# =============================================================================
# Run all parts — uncomment each line as you complete it
# =============================================================================
if __name__ == "__main__":
    part_1_dataset_exploration(df)

    # df_clean = part_2_data_transformation(df)
    # print(df_clean.head())

    # summary = part_3_aggregation_and_analysis(df_clean)
    # print(summary.head())

    # df_features = transform_transactions(df_clean)
    # print(df_features.head())
