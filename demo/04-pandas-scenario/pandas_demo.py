"""
Demo 4: Core Pandas Scenario - Financial Transaction Analysis

INSTRUCTIONS FOR PRESENTER:
Walk through each section sequentially. For each step:
1. Show the NAIVE prompt first (demonstrates poor results)
2. Then show the IMPROVED prompt (demonstrates quality output)
3. Paste/generate the code with Copilot

The prompts are written as comments. Use them in Copilot Chat.
The code sections below each prompt show the EXPECTED output
(for backup if Copilot gives unexpected results).
"""

import pandas as pd
import numpy as np
from datetime import datetime, timezone

# ============================================================================
# STEP 1: DATASET EXPLORATION
# ============================================================================

# Load the dataset
df = pd.read_csv("financial_transactions.csv", parse_dates=["timestamp"])

# ────────────────────────────────────────────────────────────────────────────
# NAIVE PROMPT (use in Copilot Chat):
# "explore this dataset"
# ────────────────────────────────────────────────────────────────────────────

# Expected naive output: just df.head(), df.describe() — generic, not actionable


# ────────────────────────────────────────────────────────────────────────────
# IMPROVED PROMPT (use in Copilot Chat):
# 
# I have a financial transactions DataFrame `df` with columns:
# transaction_id, customer_id, amount, currency, transaction_type,
# merchant_category, timestamp, is_flagged, account_balance.
# 
# Give me a comprehensive data quality report including:
# - Missing values per column (count and percentage)
# - Data type validation
# - Statistical outliers in amount (IQR method)
# - Date range coverage
# - Distribution of categorical fields
# - Duplicate transaction_id check
#
# Format as a printed report with clear section headers.
# ────────────────────────────────────────────────────────────────────────────

# Expected improved output (backup):
def explore_data_quality(df: pd.DataFrame) -> None:
    """Comprehensive data quality assessment for financial transactions."""
    print("=" * 60)
    print("DATA QUALITY REPORT")
    print("=" * 60)

    # Missing values
    print("\n📋 MISSING VALUES")
    print("-" * 40)
    missing = df.isnull().sum()
    missing_pct = (missing / len(df) * 100).round(2)
    missing_report = pd.DataFrame({"count": missing, "percentage": missing_pct})
    print(missing_report[missing_report["count"] > 0].to_string())

    # Data types
    print("\n📋 DATA TYPES")
    print("-" * 40)
    print(df.dtypes.to_string())

    # Outliers in amount (IQR method)
    print("\n📋 AMOUNT OUTLIERS (IQR)")
    print("-" * 40)
    q1 = df["amount"].quantile(0.25)
    q3 = df["amount"].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = df[(df["amount"] < lower) | (df["amount"] > upper)]
    print(f"  Q1: {q1:.2f}, Q3: {q3:.2f}, IQR: {iqr:.2f}")
    print(f"  Bounds: [{lower:.2f}, {upper:.2f}]")
    print(f"  Outliers: {len(outliers)} ({len(outliers)/len(df)*100:.1f}%)")

    # Date range
    print("\n📋 DATE RANGE")
    print("-" * 40)
    print(f"  Start: {df['timestamp'].min()}")
    print(f"  End:   {df['timestamp'].max()}")
    print(f"  Span:  {(df['timestamp'].max() - df['timestamp'].min()).days} days")

    # Categorical distributions
    print("\n📋 CATEGORICAL DISTRIBUTIONS")
    print("-" * 40)
    for col in ["currency", "transaction_type", "merchant_category"]:
        print(f"\n  {col}:")
        print(df[col].value_counts().to_string(header=False))

    # Duplicates
    print("\n📋 DUPLICATE CHECK")
    print("-" * 40)
    dupes = df["transaction_id"].duplicated().sum()
    print(f"  Duplicate transaction_ids: {dupes}")

    print("\n" + "=" * 60)


# ============================================================================
# STEP 2: DATA TRANSFORMATION
# ============================================================================

# ────────────────────────────────────────────────────────────────────────────
# NAIVE PROMPT (use in Copilot Chat):
# "clean the data"
# ────────────────────────────────────────────────────────────────────────────

# Expected naive output: drops rows with NaN, maybe resets index — too aggressive


# ────────────────────────────────────────────────────────────────────────────
# IMPROVED PROMPT (use in Copilot Chat):
#
# Transform the transactions DataFrame `df` with these requirements:
# 1. Convert timestamp to datetime, localize to UTC
# 2. Create amount_eur column (convert USD at 0.92, GBP at 1.17)
# 3. Fill missing merchant_category with 'UNKNOWN' (don't drop rows)
# 4. Remove exact duplicate transaction_ids (keep first)
# 5. Clip amount to [0, 500000] range (regulatory cap)
#
# Use method chaining. Add inline comments explaining each step.
# Return a new DataFrame, don't modify in place.
# ────────────────────────────────────────────────────────────────────────────

# Expected improved output (backup):
def transform_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """Apply business-rule transformations to raw transaction data."""
    fx_rates = {"EUR": 1.0, "USD": 0.92, "GBP": 1.17}

    transformed = (
        df
        # Ensure timestamp is UTC-aware
        .assign(
            timestamp=lambda x: pd.to_datetime(x["timestamp"], utc=True)
        )
        # Convert amount to EUR using fx rates
        .assign(
            amount_eur=lambda x: x.apply(
                lambda row: row["amount"] * fx_rates.get(row["currency"], 1.0),
                axis=1
            )
        )
        # Fill missing merchant categories
        .assign(
            merchant_category=lambda x: x["merchant_category"].fillna("UNKNOWN")
        )
        # Remove duplicate transaction IDs (keep first occurrence)
        .drop_duplicates(subset=["transaction_id"], keep="first")
        # Apply regulatory cap on amount
        .assign(
            amount=lambda x: x["amount"].clip(lower=0, upper=500_000)
        )
        # Reset index after dropping duplicates
        .reset_index(drop=True)
    )

    return transformed


# ============================================================================
# STEP 3: FEATURE ENGINEERING
# ============================================================================

# ────────────────────────────────────────────────────────────────────────────
# PROMPT (use in Copilot Chat):
#
# Create these features from the transactions DataFrame for fraud detection:
# 1. transaction_hour: hour of day from timestamp
# 2. amount_zscore: z-score of amount within each customer_id group
# 3. days_since_last_txn: days since customer's previous transaction
# 4. rolling_7d_avg: 7-day rolling average amount per customer
# 5. is_high_value: boolean, True if amount > 95th percentile for that
#    merchant_category
#
# Ensure the code handles edge cases:
# - First transaction for a customer (days_since_last_txn = NaN is OK)
# - Customers with fewer than 7 days of history
#
# Use vectorized pandas operations (no iterrows). Include type hints.
# ────────────────────────────────────────────────────────────────────────────

# Expected output (backup):
def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create fraud-detection features from transaction data."""
    result = df.copy()

    # 1. Transaction hour
    result["transaction_hour"] = result["timestamp"].dt.hour

    # 2. Amount z-score within customer group
    customer_stats = result.groupby("customer_id")["amount"].transform
    result["amount_zscore"] = (
        (result["amount"] - customer_stats("mean")) / customer_stats("std")
    )

    # 3. Days since last transaction per customer
    result = result.sort_values(["customer_id", "timestamp"])
    result["days_since_last_txn"] = (
        result.groupby("customer_id")["timestamp"]
        .diff()
        .dt.total_seconds() / 86400  # Convert to days
    )

    # 4. Rolling 7-day average amount per customer
    result = result.set_index("timestamp").sort_index()
    result["rolling_7d_avg"] = (
        result.groupby("customer_id")["amount"]
        .transform(lambda x: x.rolling("7D", min_periods=1).mean())
    )
    result = result.reset_index()

    # 5. High value flag (> 95th percentile per merchant category)
    category_p95 = result.groupby("merchant_category")["amount"].transform(
        lambda x: x.quantile(0.95)
    )
    result["is_high_value"] = result["amount"] > category_p95

    return result


# ============================================================================
# STEP 4: AGGREGATION & BUSINESS METRICS
# ============================================================================

# ────────────────────────────────────────────────────────────────────────────
# PROMPT (use in Copilot Chat):
#
# Create a monthly customer summary from the transactions DataFrame:
# - Group by customer_id and month (from timestamp)
# - Calculate: total_amount, transaction_count, unique_merchants,
#   avg_transaction, max_transaction
# - Add month-over-month growth rate for total_amount
# - Sort by customer_id and month
#
# Output as a clean DataFrame with a MultiIndex reset.
# ────────────────────────────────────────────────────────────────────────────

# Expected output (backup):
def build_customer_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Build monthly customer summary with growth metrics."""
    # Create month period for grouping
    df_with_month = df.assign(month=df["timestamp"].dt.to_period("M"))

    # Aggregate
    summary = (
        df_with_month
        .groupby(["customer_id", "month"])
        .agg(
            total_amount=("amount", "sum"),
            transaction_count=("amount", "count"),
            unique_merchants=("merchant_category", "nunique"),
            avg_transaction=("amount", "mean"),
            max_transaction=("amount", "max"),
        )
        .reset_index()
    )

    # Month-over-month growth rate
    summary = summary.sort_values(["customer_id", "month"])
    summary["mom_growth"] = (
        summary.groupby("customer_id")["total_amount"]
        .pct_change()
    )

    return summary


# ============================================================================
# STEP 5: REFACTORING (already shown above as clean functions)
# ============================================================================

# ────────────────────────────────────────────────────────────────────────────
# PROMPT (use in Copilot Chat):
#
# Refactor the data transformation code from above into a production-ready
# module:
# - Create a function `transform_transactions(df: pd.DataFrame) -> pd.DataFrame`
# - Create a function `engineer_features(df: pd.DataFrame) -> pd.DataFrame`
# - Create a function `build_customer_summary(df: pd.DataFrame) -> pd.DataFrame`
# - Add type hints, docstrings, and input validation
# - Each function should raise ValueError with a descriptive message if
#   input is invalid
# - Follow the single responsibility principle
# ────────────────────────────────────────────────────────────────────────────

# (The functions above already demonstrate the refactored output)


# ============================================================================
# STEP 6: TEST GENERATION
# ============================================================================

# ────────────────────────────────────────────────────────────────────────────
# PROMPT (use in Copilot Chat):
#
# Generate pytest tests for the transform_transactions function:
# - Test with valid input (happy path)
# - Test currency conversion accuracy (USD, GBP → EUR)
# - Test that missing merchant_category is filled
# - Test that duplicates are removed (keep first)
# - Test amount clipping at boundaries (0 and 500000)
# - Test with empty DataFrame (should return empty, not error)
# - Use pytest fixtures for sample data
# - Include parametrize for currency conversion rates
# ────────────────────────────────────────────────────────────────────────────

# (Tests will be generated live by Copilot. See backup in test file.)


# ============================================================================
# MAIN - Run the full pipeline (for testing purposes)
# ============================================================================

if __name__ == "__main__":
    print("Loading data...")
    df = pd.read_csv("financial_transactions.csv", parse_dates=["timestamp"])
    print(f"Loaded {len(df)} transactions\n")

    print("Step 1: Data Quality Report")
    explore_data_quality(df)

    print("\nStep 2: Transforming...")
    df_clean = transform_transactions(df)
    print(f"After transform: {len(df_clean)} rows")

    print("\nStep 3: Feature Engineering...")
    df_features = engineer_features(df_clean)
    print(f"New columns: {[c for c in df_features.columns if c not in df_clean.columns]}")

    print("\nStep 4: Monthly Summary...")
    summary = build_customer_summary(df_clean)
    print(f"Summary shape: {summary.shape}")
    print(summary.head(10))

    print("\n✅ Pipeline complete!")
