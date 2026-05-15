import pandas as pd

df = pd.read_csv("financial_transactions.csv", parse_dates=["timestamp"])

print(f"Dataset loaded: {len(df)} transactions")
print(f"Columns: {list(df.columns)}")
print(f"Date range: {df['timestamp'].min()} to {df['timestamp'].max()}")
print(f"Customers: {df['customer_id'].nunique()}")
print()


def part_1_dataset_exploration(df_input: pd.DataFrame) -> None:
    """Participant solution placeholder for Part 1."""
    raise NotImplementedError("Replace with your Part 1 solution.")


def part_2_data_transformation(df_input: pd.DataFrame) -> pd.DataFrame:
    """Participant solution placeholder for Part 2."""
    raise NotImplementedError("Replace with your Part 2 solution.")


def part_3_aggregation_and_analysis(df_input: pd.DataFrame) -> pd.DataFrame:
    """Participant solution placeholder for Part 3."""
    raise NotImplementedError("Replace with your Part 3 solution.")


def part_4_refactor_and_tests(df_input: pd.DataFrame) -> pd.DataFrame:
    """Participant solution placeholder for Part 4."""
    raise NotImplementedError("Replace with your Part 4 solution.")


def stretch_goal_1(df_input: pd.DataFrame) -> pd.DataFrame:
    """Participant solution placeholder for Stretch Goal 1."""
    raise NotImplementedError("Optional stretch goal placeholder.")


def stretch_goal_2(df_input: pd.DataFrame) -> pd.DataFrame:
    """Participant solution placeholder for Stretch Goal 2."""
    raise NotImplementedError("Optional stretch goal placeholder.")
