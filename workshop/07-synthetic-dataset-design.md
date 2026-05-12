# Synthetic Pandas Dataset Design

## Dataset: Financial Transactions

### File
`financial_transactions.csv` — ~10,000 rows of synthetic transaction data modeled after retail banking patterns.

---

## Schema

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `transaction_id` | string | Unique transaction identifier | `TXN_00000001` |
| `customer_id` | string | Customer identifier | `CUST_0042` |
| `amount` | float | Transaction amount (in original currency) | `1250.75` |
| `currency` | string | Transaction currency (ISO 4217) | `EUR`, `USD`, `GBP` |
| `transaction_type` | string | Type of transaction | `PURCHASE`, `TRANSFER`, `WITHDRAWAL`, `REFUND` |
| `merchant_category` | string | Merchant classification | `GROCERY`, `TRAVEL`, `ELECTRONICS`, `DINING`, `UTILITIES`, `HEALTHCARE` |
| `timestamp` | datetime | Transaction timestamp (UTC) | `2024-03-15 14:32:07` |
| `is_flagged` | bool | Whether transaction was flagged for review | `False` |
| `account_balance` | float | Account balance after transaction | `24530.00` |

---

## Data Characteristics

### Volume
- **Rows:** 10,000 transactions
- **Customers:** ~200 unique customers
- **Date range:** 2024-01-01 to 2024-12-31 (12 months)

### Distributions

| Column | Distribution |
|--------|-------------|
| `amount` | Log-normal (μ=5.5, σ=1.5), range: €0.50 – €450,000. Majority under €5,000 with tail of high-value transactions. |
| `currency` | Weighted: EUR (70%), USD (20%), GBP (10%) |
| `transaction_type` | Weighted: PURCHASE (60%), TRANSFER (20%), WITHDRAWAL (15%), REFUND (5%) |
| `merchant_category` | Roughly uniform with slight over-representation of GROCERY and DINING |
| `is_flagged` | ~3% True (realistic fraud flag rate) |
| `timestamp` | Higher frequency on weekdays and business hours, with realistic seasonal patterns (holiday spending spikes) |

### Built-in Data Quality Issues (for exploration demo)
- ~2% missing values in `merchant_category` (NaN)
- ~0.5% duplicate `transaction_id` values (intentional for cleaning demo)
- ~1% of timestamps have timezone inconsistencies (some naive, some UTC-aware)
- A few negative amounts (legitimate refunds but good for validation discussions)
- Some `account_balance` values that don't logically follow from transactions (simulates data pipeline issues)

---

## Sample Use Case: Transaction Monitoring Dashboard

**Business scenario:** You're a data engineer at a financial institution building a transaction monitoring pipeline. Your team needs to:

1. **Data quality:** Identify and resolve data issues before downstream analysis
2. **Feature engineering:** Create signals for the fraud detection ML model
3. **Reporting:** Generate monthly customer summaries for the risk team
4. **Monitoring:** Flag unusual spending patterns

This dataset enables demonstrating all four use cases with realistic complexity.

---

## Generation Script

```python
"""
Generate synthetic financial transactions dataset.
Run once to create financial_transactions.csv for the workshop.
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

N_TRANSACTIONS = 10_000
N_CUSTOMERS = 200

# Customer IDs
customers = [f"CUST_{i:04d}" for i in range(N_CUSTOMERS)]

# Transaction timestamps (2024, weighted toward business hours/weekdays)
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
date_range_days = (end_date - start_date).days

timestamps = []
for _ in range(N_TRANSACTIONS):
    day_offset = np.random.randint(0, date_range_days)
    # Weight toward business hours
    hour = int(np.random.normal(13, 4))
    hour = max(0, min(23, hour))
    minute = np.random.randint(0, 60)
    second = np.random.randint(0, 60)
    ts = start_date + timedelta(days=day_offset, hours=hour, minutes=minute, seconds=second)
    timestamps.append(ts)

# Amounts (log-normal)
amounts = np.random.lognormal(mean=5.5, sigma=1.5, size=N_TRANSACTIONS)
amounts = np.round(amounts, 2)
amounts = np.clip(amounts, 0.50, 450_000)

# Currencies (weighted)
currencies = np.random.choice(
    ["EUR", "USD", "GBP"],
    size=N_TRANSACTIONS,
    p=[0.70, 0.20, 0.10]
)

# Transaction types (weighted)
transaction_types = np.random.choice(
    ["PURCHASE", "TRANSFER", "WITHDRAWAL", "REFUND"],
    size=N_TRANSACTIONS,
    p=[0.60, 0.20, 0.15, 0.05]
)

# Merchant categories
categories = ["GROCERY", "TRAVEL", "ELECTRONICS", "DINING", "UTILITIES", "HEALTHCARE"]
merchant_categories = np.random.choice(categories, size=N_TRANSACTIONS)

# Flag ~3%
is_flagged = np.random.random(N_TRANSACTIONS) < 0.03

# Account balances (somewhat realistic)
account_balances = np.random.uniform(500, 100_000, size=N_TRANSACTIONS).round(2)

# Build DataFrame
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

# --- Inject data quality issues ---

# 1. Missing merchant_category (~2%)
missing_mask = np.random.random(N_TRANSACTIONS) < 0.02
df.loc[missing_mask, "merchant_category"] = np.nan

# 2. Duplicate transaction_ids (~0.5%)
n_dupes = int(N_TRANSACTIONS * 0.005)
dupe_indices = np.random.choice(N_TRANSACTIONS, size=n_dupes, replace=False)
source_indices = np.random.choice(N_TRANSACTIONS, size=n_dupes, replace=False)
df.loc[dupe_indices, "transaction_id"] = df.loc[source_indices, "transaction_id"].values

# 3. Make some amounts negative (refunds)
refund_mask = df["transaction_type"] == "REFUND"
df.loc[refund_mask, "amount"] = -df.loc[refund_mask, "amount"].abs()

# Sort by timestamp
df = df.sort_values("timestamp").reset_index(drop=True)

# Save
df.to_csv("financial_transactions.csv", index=False)
print(f"Generated {len(df)} transactions for {N_CUSTOMERS} customers")
print(f"Date range: {df['timestamp'].min()} to {df['timestamp'].max()}")
print(f"Missing merchant_category: {df['merchant_category'].isna().sum()}")
print(f"Duplicate transaction_ids: {df['transaction_id'].duplicated().sum()}")
print(f"Flagged transactions: {df['is_flagged'].sum()}")
```

---

## Sample Data (First 5 Rows)

| transaction_id | customer_id | amount | currency | transaction_type | merchant_category | timestamp | is_flagged | account_balance |
|---|---|---|---|---|---|---|---|---|
| TXN_00004721 | CUST_0118 | 45.23 | EUR | PURCHASE | GROCERY | 2024-01-01 08:15:33 | False | 12450.00 |
| TXN_00002893 | CUST_0042 | 1250.75 | EUR | TRANSFER | NaN | 2024-01-01 09:02:11 | False | 34200.50 |
| TXN_00008156 | CUST_0007 | 89.99 | USD | PURCHASE | ELECTRONICS | 2024-01-01 10:44:02 | False | 8930.25 |
| TXN_00001547 | CUST_0195 | -32.50 | EUR | REFUND | DINING | 2024-01-01 11:23:45 | False | 5620.00 |
| TXN_00006234 | CUST_0088 | 15420.00 | GBP | PURCHASE | TRAVEL | 2024-01-01 12:01:58 | True | 92100.00 |

---

## Why This Dataset Works for the Workshop

1. **Realistic complexity:** Multiple data types, business rules, quality issues
2. **Financial services context:** Directly relevant to the audience
3. **Gradual difficulty:** Exploration is easy, feature engineering is challenging
4. **Demonstrates prompt value:** Vague prompts produce poor transformations; specific prompts produce production-ready code
5. **Testable outputs:** Every transformation has verifiable expected results
6. **Safe:** Fully synthetic, no PII, no real transaction patterns
