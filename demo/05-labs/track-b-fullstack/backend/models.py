"""Pydantic models for the financial transactions API."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field



class Transaction(BaseModel):
    transaction_id: str
    customer_id: str
    amount: float
    currency: str = "EUR"
    transaction_type: str
    merchant_category: str
    timestamp: datetime
    is_flagged: bool = False
    # No field validation (code smell)



class TransactionCreate(BaseModel):
    customer_id: str
    amount: float
    currency: str = "EUR"
    transaction_type: str
    merchant_category: str
    # No field validation (code smell)



class TransactionResponse(BaseModel):
    transaction_id: str
    customer_id: str
    amount: float
    currency: str
    transaction_type: str
    merchant_category: str
    timestamp: datetime
    is_flagged: bool
    # No docstring (code smell)
