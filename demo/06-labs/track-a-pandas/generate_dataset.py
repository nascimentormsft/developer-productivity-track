"""
Generate synthetic financial transactions dataset for Track A lab.
Run this script once to create financial_transactions.csv.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

N_TRANSACTIONS = 10_000
N_CUSTOMERS = 200

customers = [f"CUST_{i:04d}" for i in range(N_CUSTOMERS)]

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
date_range_days = (end_date - start_date).days

timestamps = []
for _ in range(N_TRANSACTIONS):
    day_offset = np.random.randint(0, date_range_days)
    hour = int(np.random.normal(13, 4))
    hour = max(0, min(23, hour))
    minute = np.random.randint(0, 60)
    second = np.random.randint(0, 60)
    ts = start_date + timedelta(days=day_offset, hours=hour, minutes=minute, seconds=second)
    timestamps.append(ts)

amounts = np.random.lognormal(mean=5.5, sigma=1.5, size=N_TRANSACTIONS)
amounts = np.round(amounts, 2)
amounts = np.clip(amounts, 0.50, 450_000)

currencies = np.random.choice(["EUR", "USD", "GBP"], size=N_TRANSACTIONS, p=[0.70, 0.20, 0.10])
transaction_types = np.random.choice(
    ["PURCHASE", "TRANSFER", "WITHDRAWAL", "REFUND"],
    size=N_TRANSACTIONS, p=[0.60, 0.20, 0.15, 0.05]
)
categories = ["GROCERY", "TRAVEL", "ELECTRONICS", "DINING", "UTILITIES", "HEALTHCARE"]
merchant_categories = np.random.choice(categories, size=N_TRANSACTIONS)
is_flagged = np.random.random(N_TRANSACTIONS) < 0.03
account_balances = np.random.uniform(500, 100_000, size=N_TRANSACTIONS).round(2)

df = pd.DataFrame({
    "transaction_id": [f"TXN_{i:08d}" for i in range(N_TRANSACTIONS)],
    "customer_id": np.random.choice(customers, size=N_TRANSACTIONS),
    "amount": amounts,
    "currency": currencies,
    "transaction_type": transaction_types,
    "merchant_category": merchant_categories,
    "timestamp": timestamps,
    "is_flagged": is_flagged,
    "account_balance": account_balances,
})

# Inject data quality issues
missing_mask = np.random.random(N_TRANSACTIONS) < 0.02
df.loc[missing_mask, "merchant_category"] = np.nan

n_dupes = int(N_TRANSACTIONS * 0.005)
dupe_indices = np.random.choice(N_TRANSACTIONS, size=n_dupes, replace=False)
source_indices = np.random.choice(N_TRANSACTIONS, size=n_dupes, replace=False)
df.loc[dupe_indices, "transaction_id"] = df.loc[source_indices, "transaction_id"].values

refund_mask = df["transaction_type"] == "REFUND"
df.loc[refund_mask, "amount"] = -df.loc[refund_mask, "amount"].abs()

df = df.sort_values("timestamp").reset_index(drop=True)
df.to_csv("financial_transactions.csv", index=False)

print(f"Generated {len(df)} transactions for {N_CUSTOMERS} customers")
print(f"  Date range: {df['timestamp'].min()} to {df['timestamp'].max()}")
print(f"  Missing merchant_category: {df['merchant_category'].isna().sum()}")
print(f"  Duplicate transaction_ids: {df['transaction_id'].duplicated().sum()}")
print(f"  Flagged transactions: {df['is_flagged'].sum()}")
