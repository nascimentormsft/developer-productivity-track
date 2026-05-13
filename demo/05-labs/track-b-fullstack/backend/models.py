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


class TransactionCreate(BaseModel):
    customer_id: str = Field(..., min_length=1)
    amount: float = Field(..., gt=0)
    currency: str = Field(default="EUR", pattern="^(EUR|USD|GBP)$")
    transaction_type: str = Field(..., pattern="^(PURCHASE|TRANSFER|WITHDRAWAL|REFUND)$")
    merchant_category: str = Field(..., min_length=1)


class TransactionResponse(BaseModel):
    transaction_id: str
    customer_id: str
    amount: float
    currency: str
    transaction_type: str
    merchant_category: str
    timestamp: datetime
    is_flagged: bool
