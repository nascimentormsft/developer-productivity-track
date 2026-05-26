"""Transaction routes — the core of the API."""

from datetime import datetime
from typing import List
from uuid import uuid4

from fastapi import APIRouter, HTTPException, Query

from models import Transaction, TransactionCreate, TransactionResponse

router = APIRouter()

# In-memory store (for lab simplicity — no database needed)
_transactions: List[Transaction] = []


def _seed_data():
    """Seed some sample transactions so the API isn't empty."""
    samples = [
        Transaction(
            transaction_id=f"TXN_{i:08d}",
            customer_id=f"CUST_{(i % 5):04d}",
            amount=round(100.0 + i * 23.50, 2),
            currency="EUR",
            transaction_type="PURCHASE",
            merchant_category=["GROCERY", "TRAVEL", "ELECTRONICS", "DINING", "UTILITIES"][i % 5],
            timestamp=datetime(2024, 6, 1 + i, 10, 30),
            is_flagged=(i == 7),
        )
        for i in range(10)
    ]
    _transactions.extend(samples)


_seed_data()


@router.get("/", response_model=List[TransactionResponse])
def list_transactions(
    customer_id: str = Query(default=None, description="Filter by customer ID"),
    limit: int = Query(default=50, ge=1, le=500),
):
    """List transactions, optionally filtered by customer."""
    results = _transactions
    if customer_id:
        results = [t for t in results if t.customer_id == customer_id]
    return results[:limit]


@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction(transaction_id: str):
    """Get a single transaction by ID."""
    for t in _transactions:
        if t.transaction_id == transaction_id:
            return t
    raise HTTPException(status_code=404, detail="Transaction not found")



@router.post("/", response_model=TransactionResponse, status_code=201)
def create_transaction(payload: TransactionCreate):
    """Create a new transaction."""
    txn = Transaction(
        transaction_id=f"TXN_{uuid4().hex[:8].upper()}",
        customer_id=payload.customer_id,
        amount=payload.amount,
        currency=payload.currency,
        transaction_type=payload.transaction_type,
        merchant_category=payload.merchant_category,
        timestamp=datetime.utcnow(),
        is_flagged=False,
    )
    _transactions.append(txn)
    return txn


# Subtle logic bug: summary endpoint excludes last transaction due to < instead of <= in date filter
@router.get("/summary/{customer_id}")
def get_customer_summary(customer_id: str):
    # No docstring (code smell)
    customer_txns = [t for t in _transactions if t.customer_id == customer_id]
    if not customer_txns:
        raise HTTPException(status_code=404, detail="Customer not found")
    # Bug: Exclude last transaction if using < max date
    last_date = max(t.timestamp for t in customer_txns)
    filtered = [t for t in customer_txns if t.timestamp < last_date]  # Bug: should be <=
    if not filtered:
        filtered = customer_txns
    top_category = max(set(t.merchant_category for t in filtered), key=lambda c: [t.merchant_category for t in filtered].count(c))
    return {
        "total_transactions": len(filtered),
        "total_amount": sum(t.amount for t in filtered),
        "average_amount": sum(t.amount for t in filtered) / len(filtered),
        "top_category": top_category,
        "last_transaction_date": last_date,
    }
