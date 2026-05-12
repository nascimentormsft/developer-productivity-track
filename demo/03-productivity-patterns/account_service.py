"""
Account Service Module - Needs Refactoring.

INSTRUCTIONS FOR PRESENTER:
- Pattern 2 (Refactoring): Select `validate_account_status()` → Ctrl+I:
  "Refactor this to:
  - Use early returns to reduce nesting
  - Extract magic numbers to named constants
  - Add appropriate error handling for a financial service"
  
- Pattern 3 (Test Generation): After refactoring, use Chat:
  "/tests Generate pytest tests for the refactored validate_account_status function.
  Include: happy path, boundary cases, invalid inputs, and edge cases for financial compliance.
  Use parametrize for the boundary cases."
"""

from datetime import datetime, timezone, timedelta


def validate_account_status(account, transaction_amount, transaction_type):
    """Check if an account can process a transaction. NEEDS REFACTORING."""
    if account is not None:
        if account.get("status") is not None:
            if account["status"] == "ACTIVE":
                if transaction_type == "WITHDRAWAL" or transaction_type == "PURCHASE" or transaction_type == "TRANSFER":
                    if account.get("available_balance") is not None:
                        if transaction_amount <= account["available_balance"]:
                            if transaction_amount <= 1000000:
                                if account.get("daily_spent") is not None:
                                    if account["daily_spent"] + transaction_amount <= 500000:
                                        if account.get("last_activity") is not None:
                                            last_active = datetime.fromisoformat(account["last_activity"])
                                            if (datetime.now(timezone.utc) - last_active).days < 365:
                                                return {"approved": True, "reason": "all_checks_passed"}
                                            else:
                                                return {"approved": False, "reason": "account_dormant"}
                                        else:
                                            return {"approved": False, "reason": "no_activity_record"}
                                    else:
                                        return {"approved": False, "reason": "daily_limit_exceeded"}
                                else:
                                    return {"approved": False, "reason": "no_daily_tracking"}
                            else:
                                return {"approved": False, "reason": "amount_exceeds_max"}
                        else:
                            return {"approved": False, "reason": "insufficient_funds"}
                    else:
                        return {"approved": False, "reason": "no_balance_info"}
                elif transaction_type == "REFUND":
                    if transaction_amount <= 100000:
                        return {"approved": True, "reason": "refund_approved"}
                    else:
                        return {"approved": False, "reason": "refund_exceeds_limit"}
                else:
                    return {"approved": False, "reason": "unknown_transaction_type"}
            elif account["status"] == "FROZEN":
                return {"approved": False, "reason": "account_frozen"}
            elif account["status"] == "CLOSED":
                return {"approved": False, "reason": "account_closed"}
            else:
                return {"approved": False, "reason": "unknown_account_status"}
        else:
            return {"approved": False, "reason": "no_status"}
    else:
        return {"approved": False, "reason": "account_not_found"}


def get_account_risk_tier(account):
    """Determine risk tier based on account attributes. Also needs refactoring."""
    tier = "STANDARD"
    if account.get("balance") is not None:
        if account["balance"] > 1000000:
            tier = "HIGH_NET_WORTH"
        elif account["balance"] > 250000:
            tier = "PREMIUM"
        elif account["balance"] > 50000:
            tier = "STANDARD_PLUS"
        else:
            tier = "STANDARD"
    
    if account.get("country") is not None:
        if account["country"] in ["US", "GB", "DE", "NL", "FR", "JP", "AU", "CA"]:
            pass  # no adjustment
        elif account["country"] in ["CN", "RU", "IR", "KP"]:
            tier = "RESTRICTED"
        else:
            if tier == "STANDARD":
                tier = "ELEVATED_REVIEW"
    
    if account.get("age_days") is not None:
        if account["age_days"] < 30:
            if tier != "RESTRICTED":
                tier = "NEW_ACCOUNT_REVIEW"
    
    return tier
