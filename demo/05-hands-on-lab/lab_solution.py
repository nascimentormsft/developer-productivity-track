"""
Lab Solution - For facilitator reference only.
DO NOT share with participants until after the exercise.
"""

import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("financial_transactions.csv", parse_dates=["timestamp"])


# ════════════════════════════════════════════════════════════════════════════
# MAIN TASK SOLUTION
# ════════════════════════════════════════════════════════════════════════════

def analyze_top_spenders(df: pd.DataFrame, top_n: int = 5) -> pd.DataFrame:
    """
    Identify top spending customers by merchant category.

    Args:
        df: Financial transactions DataFrame.
        top_n: Number of top customers to return per category.

    Returns:
        DataFrame with top spenders per category.
    """
    # Step 1: Filter out flagged transactions
    df_clean = df[df["is_flagged"] == False].copy()

    # Step 2 & 3: Group and aggregate
    spending = (
        df_clean
        .groupby(["customer_id", "merchant_category"])
        .agg(
            total_spent=("amount", "sum"),
            num_transactions=("amount", "count"),
        )
        .reset_index()
    )

    # Step 4: Calculate average transaction
    spending["avg_transaction"] = spending["total_spent"] / spending["num_transactions"]

    # Step 5: Rank within each category and keep top N
    spending["rank"] = (
        spending
        .groupby("merchant_category")["total_spent"]
        .rank(method="dense", ascending=False)
    )

    top_spenders = (
        spending[spending["rank"] <= top_n]
        .sort_values(["merchant_category", "rank"])
        .drop(columns=["rank"])
        .reset_index(drop=True)
    )

    return top_spenders


# ════════════════════════════════════════════════════════════════════════════
# STRETCH GOAL 1 SOLUTION: Time Intelligence
# ════════════════════════════════════════════════════════════════════════════

def classify_spending_trend(df: pd.DataFrame, threshold: float = 0.1) -> pd.DataFrame:
    """
    Classify customer spending trend based on last 30 days vs prior 30 days.

    Args:
        df: Financial transactions DataFrame with timestamp column.
        threshold: Minimum change ratio to classify as increasing/decreasing.

    Returns:
        DataFrame with customer_id and spending_trend columns.
    """
    max_date = df["timestamp"].max()
    last_30 = df[df["timestamp"] >= max_date - pd.Timedelta(days=30)]
    prior_30 = df[
        (df["timestamp"] >= max_date - pd.Timedelta(days=60)) &
        (df["timestamp"] < max_date - pd.Timedelta(days=30))
    ]

    last_30_spend = last_30.groupby("customer_id")["amount"].sum()
    prior_30_spend = prior_30.groupby("customer_id")["amount"].sum()

    comparison = pd.DataFrame({
        "last_30_total": last_30_spend,
        "prior_30_total": prior_30_spend,
    }).fillna(0)

    comparison["change_ratio"] = (
        (comparison["last_30_total"] - comparison["prior_30_total"])
        / comparison["prior_30_total"].replace(0, np.nan)
    )

    def classify(ratio):
        if pd.isna(ratio):
            return "NEW"
        elif ratio > threshold:
            return "INCREASING"
        elif ratio < -threshold:
            return "DECREASING"
        else:
            return "STABLE"

    comparison["spending_trend"] = comparison["change_ratio"].apply(classify)

    return comparison[["spending_trend"]].reset_index()


# ════════════════════════════════════════════════════════════════════════════
# STRETCH GOAL 2 SOLUTION: Anomaly Detection
# ════════════════════════════════════════════════════════════════════════════

def detect_anomalous_customers(df: pd.DataFrame, std_threshold: float = 3.0) -> pd.DataFrame:
    """
    Flag customers whose avg transaction is >3 std deviations above category mean.

    Args:
        df: Financial transactions DataFrame.
        std_threshold: Number of standard deviations for anomaly threshold.

    Returns:
        DataFrame with flagged customer-category pairs.
    """
    # Calculate per-customer-category average
    customer_avg = (
        df.groupby(["customer_id", "merchant_category"])["amount"]
        .mean()
        .reset_index(name="customer_avg_amount")
    )

    # Calculate per-category statistics
    category_stats = (
        df.groupby("merchant_category")["amount"]
        .agg(["mean", "std"])
        .reset_index()
        .rename(columns={"mean": "category_mean", "std": "category_std"})
    )

    # Merge and flag
    merged = customer_avg.merge(category_stats, on="merchant_category")
    merged["z_score"] = (
        (merged["customer_avg_amount"] - merged["category_mean"]) / merged["category_std"]
    )
    merged["is_anomalous"] = merged["z_score"] > std_threshold

    anomalies = merged[merged["is_anomalous"]].sort_values("z_score", ascending=False)

    return anomalies


# ════════════════════════════════════════════════════════════════════════════
# RUN ALL SOLUTIONS
# ════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("MAIN TASK: Top Spenders by Category")
    print("=" * 60)
    top_spenders = analyze_top_spenders(df)
    print(top_spenders.to_string(index=False))

    print("\n" + "=" * 60)
    print("STRETCH 1: Spending Trends")
    print("=" * 60)
    trends = classify_spending_trend(df)
    print(trends["spending_trend"].value_counts().to_string())

    print("\n" + "=" * 60)
    print("STRETCH 2: Anomalous Customers")
    print("=" * 60)
    anomalies = detect_anomalous_customers(df)
    print(f"Found {len(anomalies)} anomalous customer-category pairs")
    if len(anomalies) > 0:
        print(anomalies.head(10).to_string(index=False))
