"""
Backup tests for the pandas scenario - Test Generation demo (Step 6).

INSTRUCTIONS FOR PRESENTER:
These are the expected tests Copilot should generate.
Use these as backup if the live generation produces something unexpected.
You can also open this file AFTER the test generation prompt to compare.
"""

import pytest
import pandas as pd
import numpy as np
from datetime import datetime, timezone


# Import the function under test
# from pandas_demo import transform_transactions


# ─── Fixtures ────────────────────────────────────────────────────────────────

@pytest.fixture
def sample_transactions():
    """Create a minimal valid transactions DataFrame."""
    return pd.DataFrame({
        "transaction_id": ["TXN_001", "TXN_002", "TXN_003", "TXN_004"],
        "customer_id": ["CUST_01", "CUST_01", "CUST_02", "CUST_02"],
        "amount": [100.0, 250.50, 1000.0, 50.0],
        "currency": ["EUR", "USD", "GBP", "EUR"],
        "transaction_type": ["PURCHASE", "TRANSFER", "PURCHASE", "REFUND"],
        "merchant_category": ["GROCERY", None, "TRAVEL", "DINING"],
        "timestamp": pd.to_datetime([
            "2024-03-01 10:00:00",
            "2024-03-01 14:30:00",
            "2024-03-02 09:15:00",
            "2024-03-02 16:45:00",
        ]),
        "is_flagged": [False, False, True, False],
        "account_balance": [5000.0, 4749.50, 25000.0, 25050.0],
    })


@pytest.fixture
def sample_with_duplicates():
    """DataFrame with duplicate transaction_ids."""
    return pd.DataFrame({
        "transaction_id": ["TXN_001", "TXN_001", "TXN_002"],
        "customer_id": ["CUST_01", "CUST_01", "CUST_02"],
        "amount": [100.0, 200.0, 300.0],
        "currency": ["EUR", "EUR", "EUR"],
        "transaction_type": ["PURCHASE", "PURCHASE", "PURCHASE"],
        "merchant_category": ["GROCERY", "GROCERY", "TRAVEL"],
        "timestamp": pd.to_datetime([
            "2024-03-01 10:00:00",
            "2024-03-01 11:00:00",
            "2024-03-02 09:00:00",
        ]),
        "is_flagged": [False, False, False],
        "account_balance": [5000.0, 4900.0, 8000.0],
    })


@pytest.fixture
def empty_transactions():
    """Empty DataFrame with correct schema."""
    return pd.DataFrame({
        "transaction_id": pd.Series([], dtype="str"),
        "customer_id": pd.Series([], dtype="str"),
        "amount": pd.Series([], dtype="float64"),
        "currency": pd.Series([], dtype="str"),
        "transaction_type": pd.Series([], dtype="str"),
        "merchant_category": pd.Series([], dtype="str"),
        "timestamp": pd.Series([], dtype="datetime64[ns]"),
        "is_flagged": pd.Series([], dtype="bool"),
        "account_balance": pd.Series([], dtype="float64"),
    })


# ─── Happy Path ──────────────────────────────────────────────────────────────

class TestTransformTransactionsHappyPath:
    def test_returns_dataframe(self, sample_transactions):
        from pandas_demo import transform_transactions
        result = transform_transactions(sample_transactions)
        assert isinstance(result, pd.DataFrame)

    def test_adds_amount_eur_column(self, sample_transactions):
        from pandas_demo import transform_transactions
        result = transform_transactions(sample_transactions)
        assert "amount_eur" in result.columns

    def test_does_not_modify_input(self, sample_transactions):
        from pandas_demo import transform_transactions
        original = sample_transactions.copy()
        transform_transactions(sample_transactions)
        pd.testing.assert_frame_equal(sample_transactions, original)


# ─── Currency Conversion ─────────────────────────────────────────────────────

class TestCurrencyConversion:
    @pytest.mark.parametrize("currency,amount,expected_eur", [
        ("EUR", 100.0, 100.0),     # EUR → EUR: rate 1.0
        ("USD", 100.0, 92.0),      # USD → EUR: rate 0.92
        ("GBP", 100.0, 117.0),     # GBP → EUR: rate 1.17
    ])
    def test_conversion_rates(self, currency, amount, expected_eur):
        from pandas_demo import transform_transactions
        df = pd.DataFrame({
            "transaction_id": ["TXN_001"],
            "customer_id": ["CUST_01"],
            "amount": [amount],
            "currency": [currency],
            "transaction_type": ["PURCHASE"],
            "merchant_category": ["GROCERY"],
            "timestamp": pd.to_datetime(["2024-03-01 10:00:00"]),
            "is_flagged": [False],
            "account_balance": [5000.0],
        })
        result = transform_transactions(df)
        assert result["amount_eur"].iloc[0] == pytest.approx(expected_eur, rel=1e-2)


# ─── Missing Merchant Category ───────────────────────────────────────────────

class TestMissingMerchantCategory:
    def test_fills_with_unknown(self, sample_transactions):
        from pandas_demo import transform_transactions
        result = transform_transactions(sample_transactions)
        assert result["merchant_category"].isna().sum() == 0
        assert "UNKNOWN" in result["merchant_category"].values

    def test_preserves_existing_categories(self, sample_transactions):
        from pandas_demo import transform_transactions
        result = transform_transactions(sample_transactions)
        assert "GROCERY" in result["merchant_category"].values
        assert "TRAVEL" in result["merchant_category"].values


# ─── Duplicate Removal ───────────────────────────────────────────────────────

class TestDuplicateRemoval:
    def test_removes_duplicate_transaction_ids(self, sample_with_duplicates):
        from pandas_demo import transform_transactions
        result = transform_transactions(sample_with_duplicates)
        assert result["transaction_id"].is_unique

    def test_keeps_first_occurrence(self, sample_with_duplicates):
        from pandas_demo import transform_transactions
        result = transform_transactions(sample_with_duplicates)
        # First TXN_001 had amount 100.0
        txn_001 = result[result["transaction_id"] == "TXN_001"]
        assert txn_001["amount"].iloc[0] == 100.0


# ─── Amount Clipping ─────────────────────────────────────────────────────────

class TestAmountClipping:
    def test_clips_negative_to_zero(self):
        from pandas_demo import transform_transactions
        df = pd.DataFrame({
            "transaction_id": ["TXN_001"],
            "customer_id": ["CUST_01"],
            "amount": [-50.0],
            "currency": ["EUR"],
            "transaction_type": ["REFUND"],
            "merchant_category": ["GROCERY"],
            "timestamp": pd.to_datetime(["2024-03-01 10:00:00"]),
            "is_flagged": [False],
            "account_balance": [5000.0],
        })
        result = transform_transactions(df)
        assert result["amount"].iloc[0] == 0.0

    def test_clips_above_500k(self):
        from pandas_demo import transform_transactions
        df = pd.DataFrame({
            "transaction_id": ["TXN_001"],
            "customer_id": ["CUST_01"],
            "amount": [750_000.0],
            "currency": ["EUR"],
            "transaction_type": ["PURCHASE"],
            "merchant_category": ["TRAVEL"],
            "timestamp": pd.to_datetime(["2024-03-01 10:00:00"]),
            "is_flagged": [False],
            "account_balance": [1_000_000.0],
        })
        result = transform_transactions(df)
        assert result["amount"].iloc[0] == 500_000.0

    def test_boundary_at_500k_unchanged(self):
        from pandas_demo import transform_transactions
        df = pd.DataFrame({
            "transaction_id": ["TXN_001"],
            "customer_id": ["CUST_01"],
            "amount": [500_000.0],
            "currency": ["EUR"],
            "transaction_type": ["PURCHASE"],
            "merchant_category": ["TRAVEL"],
            "timestamp": pd.to_datetime(["2024-03-01 10:00:00"]),
            "is_flagged": [False],
            "account_balance": [1_000_000.0],
        })
        result = transform_transactions(df)
        assert result["amount"].iloc[0] == 500_000.0


# ─── Empty DataFrame ─────────────────────────────────────────────────────────

class TestEmptyDataFrame:
    def test_returns_empty_dataframe(self, empty_transactions):
        from pandas_demo import transform_transactions
        result = transform_transactions(empty_transactions)
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 0

    def test_has_expected_columns(self, empty_transactions):
        from pandas_demo import transform_transactions
        result = transform_transactions(empty_transactions)
        assert "amount_eur" in result.columns
