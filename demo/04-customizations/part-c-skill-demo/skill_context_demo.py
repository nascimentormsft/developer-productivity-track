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


def write_demo_artifacts(
    customer_summary: pd.DataFrame,
    output_dir: Path,
) -> None:
    """Write baseline artifact for the no-skill run.

    Args:
        customer_summary: Baseline summary dataframe.
        output_dir: Directory where artifacts will be written.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    baseline_file = output_dir / "without_skill_customer_summary.csv"
    customer_summary.to_csv(baseline_file, index=False)


def main() -> None:
    """Run the setup and print context for the Part C exercise."""
    df, customer_master = load_demo_data()
    print(f"Loaded {len(df)} transactions and {len(customer_master)} customers")
    print(df.head(5).to_string(index=False))

    # Workshop prompt 1 (baseline):
    # Create a customer summary with total amount and transaction count.
    customer_summary = (
        df.groupby("customer_id")
        .agg(
            transaction_count=("transaction_id", "count"),
            total_amount=("amount", "sum"),
        )
        .reset_index()
    )
    print("\nCustomer summary (transaction count and total amount):")
    print(customer_summary.to_string(index=False))

    # Workshop prompt 2 (skill-aware improvement) is intentionally not implemented
    # in this starter. Participants will use the prompt from GUIDE.md to update
    # this file and add the skill-aware output generation.

    output_dir = Path(__file__).parent / "outputs"
    write_demo_artifacts(
        customer_summary=customer_summary,
        output_dir=output_dir,
    )
    print("\nBaseline artifact written:")
    print(f"- {output_dir / 'without_skill_customer_summary.csv'}")


if __name__ == "__main__":
    main()
