"""Part C skill context demo.

This file gives workshop participants a concrete baseline dataset and starter code.
Use it to demonstrate how the pandas skill changes Copilot output quality.
"""

from pathlib import Path

import pandas as pd


def load_demo_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load synthetic transactions and customer master data for the demo.

    Returns:
        Tuple with transactions dataframe and customer master dataframe.
    """
    data_dir = Path(__file__).parent
    transactions_df = pd.read_csv(data_dir / "financial_transactions_sample.csv")
    customer_master_df = pd.read_csv(data_dir / "customer_master_sample.csv")
    return transactions_df, customer_master_df


def main() -> None:
    """Run the setup and print context for the Part C exercise."""
    df, customer_master = load_demo_data()
    print(f"Loaded {len(df)} transactions and {len(customer_master)} customers")
    print(df.head(5).to_string(index=False))

    # Workshop prompt 1 (baseline):
    # "Using df, create a customer summary with total amount and transaction count."
    #
    # Workshop prompt 2 (skill-aware improvement):
    # "Refactor the summary to follow the pandas-analysis skill exactly:
    # - check duplicates first
    # - convert USD/GBP to EUR (USD 0.92, GBP 1.17)
    # - flag > EUR 50,000
    # - avoid iterrows and use vectorized operations
    # - aggregate by customer, month, merchant category"


if __name__ == "__main__":
    main()
