"""
Transaction Processor Module - Financial Services Core Logic.

Used in Patterns 1, 5, and 6. See GUIDE.md for exercises.
"""

import logging
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from typing import Optional

logger = logging.getLogger(__name__)

# Transaction status constants
STATUS_PENDING = "PENDING"
STATUS_COMPLETED = "COMPLETED"
STATUS_FAILED = "FAILED"
STATUS_FLAGGED = "FLAGGED"

# Risk thresholds
HIGH_VALUE_THRESHOLD = Decimal("50000.00")
VELOCITY_LIMIT = 10  # max transactions per hour per customer
DAILY_LIMIT = Decimal("250000.00")


class TransactionError(Exception):
    pass


class InsufficientFundsError(TransactionError):
    pass


class VelocityLimitError(TransactionError):
    pass


def process_batch_transactions(transactions, accounts, risk_rules=None, 
                                dry_run=False, settlement_date=None):
    results = []
    failed = []
    total_volume = Decimal("0")
    
    if settlement_date is None:
        settlement_date = datetime.now(timezone.utc).date()
    
    sorted_txns = sorted(transactions, key=lambda t: t.get("priority", 0), reverse=True)
    
    customer_velocity = {}
    
    for txn in sorted_txns:
        txn_id = txn["transaction_id"]
        customer_id = txn["customer_id"]
        amount = Decimal(str(txn["amount"]))
        currency = txn["currency"]
        txn_type = txn.get("transaction_type", "PURCHASE")
        
        # Velocity tracking
        current_hour = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)
        vel_key = f"{customer_id}_{current_hour.isoformat()}"
        customer_velocity[vel_key] = customer_velocity.get(vel_key, 0) + 1
        
        if customer_velocity[vel_key] > VELOCITY_LIMIT:
            failed.append({"transaction_id": txn_id, "reason": "velocity_limit_exceeded"})
            logger.warning(f"Velocity limit exceeded for {customer_id}")
            continue
        
        # Account validation
        account = accounts.get(customer_id)
        if not account:
            failed.append({"transaction_id": txn_id, "reason": "account_not_found"})
            continue
        
        if account.get("status") != "ACTIVE":
            failed.append({"transaction_id": txn_id, "reason": "account_inactive"})
            continue
        
        # Balance check for debits
        if txn_type in ("PURCHASE", "WITHDRAWAL", "TRANSFER"):
            available = Decimal(str(account.get("available_balance", 0)))
            if amount > available:
                failed.append({"transaction_id": txn_id, "reason": "insufficient_funds"})
                continue
        
        # Risk evaluation
        risk_score = _calculate_risk_score(txn, account, risk_rules)
        
        if risk_score > 0.85:
            status = STATUS_FLAGGED
            logger.info(f"Transaction {txn_id} flagged with risk score {risk_score:.2f}")
        elif risk_score > 0.95:
            failed.append({"transaction_id": txn_id, "reason": "risk_threshold_exceeded"})
            continue
        else:
            status = STATUS_PENDING
        
        # Currency conversion to EUR for volume tracking
        eur_amount = _convert_to_eur(amount, currency)
        total_volume += eur_amount
        
        # Check daily limit
        if total_volume > DAILY_LIMIT and not dry_run:
            logger.error(f"Daily volume limit reached at transaction {txn_id}")
            failed.append({"transaction_id": txn_id, "reason": "daily_limit_reached"})
            break
        
        if not dry_run:
            # Apply the transaction
            _update_account_balance(account, amount, txn_type)
        
        results.append({
            "transaction_id": txn_id,
            "status": status,
            "amount_eur": float(eur_amount),
            "risk_score": risk_score,
            "settlement_date": settlement_date.isoformat(),
            "processed_at": datetime.now(timezone.utc).isoformat(),
        })
    
    return {
        "processed": results,
        "failed": failed,
        "total_volume_eur": float(total_volume),
        "batch_size": len(transactions),
        "success_rate": len(results) / len(transactions) if transactions else 0,
    }


def _calculate_risk_score(transaction, account, risk_rules=None):
    score = 0.0
    amount = Decimal(str(transaction["amount"]))
    
    # High value check
    if amount > HIGH_VALUE_THRESHOLD:
        score += 0.3
    
    # New account check (less than 30 days)
    account_age = (datetime.now(timezone.utc) - 
                   datetime.fromisoformat(account.get("created_at", "2020-01-01T00:00:00+00:00"))).days
    if account_age < 30:
        score += 0.2
    
    # Cross-border check
    if transaction.get("currency") != account.get("home_currency", "EUR"):
        score += 0.15
    
    # Custom rules
    if risk_rules:
        for rule in risk_rules:
            if rule["condition"](transaction, account):
                score += rule["weight"]
    
    return min(score, 1.0)


def _convert_to_eur(amount, currency):
    rates = {"EUR": Decimal("1.0"), "USD": Decimal("0.92"), "GBP": Decimal("1.17")}
    rate = rates.get(currency, Decimal("1.0"))
    return (amount * rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def _update_account_balance(account, amount, txn_type):
    balance = Decimal(str(account["available_balance"]))
    if txn_type in ("PURCHASE", "WITHDRAWAL", "TRANSFER"):
        account["available_balance"] = float(balance - amount)
    elif txn_type == "REFUND":
        account["available_balance"] = float(balance + amount)
