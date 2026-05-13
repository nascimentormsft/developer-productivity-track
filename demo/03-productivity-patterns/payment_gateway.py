"""
Payment Gateway Module - Contains a Subtle Bug.

Used in Patterns 4 (Debugging) and 6 (Multi-step). See GUIDE.md for exercises.
"""

import logging
from datetime import datetime, timedelta
from typing import Optional
import time
import hashlib

logger = logging.getLogger(__name__)


class PaymentGatewayError(Exception):
    def __init__(self, message, status_code=None, transaction_id=None):
        super().__init__(message)
        self.status_code = status_code
        self.transaction_id = transaction_id


class TimeoutError(PaymentGatewayError):
    pass


class GatewayResponse:
    def __init__(self, success, transaction_id, settlement_date, amount, reference):
        self.success = success
        self.transaction_id = transaction_id
        self.settlement_date = settlement_date
        self.amount = amount
        self.reference = reference


def process_payment(amount: float, currency: str, recipient: str,
                    sender_account: str, reference: Optional[str] = None) -> GatewayResponse:
    """
    Process a payment through the external gateway.
    
    BUG: This function has a subtle timezone issue that causes incorrect
    settlement dates for transactions processed near midnight UTC.
    """
    # Generate transaction reference
    if reference is None:
        reference = _generate_reference(sender_account, amount)
    
    # Validate inputs
    if amount <= 0:
        raise PaymentGatewayError("Amount must be positive", status_code=400)
    if currency not in ("EUR", "USD", "GBP"):
        raise PaymentGatewayError(f"Unsupported currency: {currency}", status_code=400)
    
    # Simulate gateway call
    logger.info(f"Processing payment: {amount} {currency} to {recipient}")
    
    # ──── BUG IS HERE ────
    # Using naive datetime (no timezone) for settlement calculation.
    # When processed near midnight, date() can be off by one day depending
    # on the server's local timezone vs UTC.
    now = datetime.now()  # BUG: should be datetime.now(timezone.utc) or datetime.utcnow()
    
    # Settlement is T+1 for domestic, T+2 for cross-border
    if _is_domestic(sender_account, recipient):
        settlement_date = now.date() + timedelta(days=1)
    else:
        settlement_date = now.date() + timedelta(days=2)
    
    # Skip weekends for settlement
    while settlement_date.weekday() >= 5:  # Saturday = 5, Sunday = 6
        settlement_date += timedelta(days=1)
    # ──── END BUG AREA ────
    
    # Simulate processing time
    transaction_id = f"PAY_{hashlib.sha256(f'{sender_account}{amount}{time.time()}'.encode()).hexdigest()[:12].upper()}"
    
    logger.info(f"Payment processed: {transaction_id}, settlement: {settlement_date}")
    
    return GatewayResponse(
        success=True,
        transaction_id=transaction_id,
        settlement_date=settlement_date,
        amount=amount,
        reference=reference,
    )


def process_refund(original_transaction_id: str, amount: float, 
                   reason: str) -> GatewayResponse:
    """Process a refund for a previously completed transaction."""
    if amount <= 0:
        raise PaymentGatewayError("Refund amount must be positive")
    
    logger.info(f"Processing refund for {original_transaction_id}: {amount}")
    
    # BUG: Same timezone issue here
    now = datetime.now()
    settlement_date = now.date() + timedelta(days=1)
    
    while settlement_date.weekday() >= 5:
        settlement_date += timedelta(days=1)
    
    refund_id = f"REF_{hashlib.sha256(f'{original_transaction_id}{time.time()}'.encode()).hexdigest()[:12].upper()}"
    
    return GatewayResponse(
        success=True,
        transaction_id=refund_id,
        settlement_date=settlement_date,
        amount=-amount,
        reference=f"REFUND_{original_transaction_id}",
    )


def check_payment_status(transaction_id: str) -> dict:
    """Check status of a payment. Simulated for demo."""
    return {
        "transaction_id": transaction_id,
        "status": "COMPLETED",
        "last_updated": datetime.now().isoformat(),  # Also uses naive datetime
    }


def _generate_reference(account: str, amount: float) -> str:
    """Generate a unique payment reference."""
    timestamp = int(time.time())
    raw = f"{account}{amount}{timestamp}"
    return f"REF{hashlib.md5(raw.encode()).hexdigest()[:10].upper()}"


def _is_domestic(sender: str, recipient: str) -> bool:
    """Check if a transaction is domestic (same country prefix)."""
    sender_country = sender[:2].upper() if len(sender) >= 2 else ""
    recipient_country = recipient[:2].upper() if len(recipient) >= 2 else ""
    return sender_country == recipient_country
