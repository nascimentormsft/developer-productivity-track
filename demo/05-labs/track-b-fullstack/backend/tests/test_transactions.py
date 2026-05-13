"""Basic tests for the transactions API."""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_list_transactions():
    response = client.get("/transactions/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_list_transactions_filter_by_customer():
    response = client.get("/transactions/?customer_id=CUST_0000")
    assert response.status_code == 200
    data = response.json()
    assert all(t["customer_id"] == "CUST_0000" for t in data)


def test_get_transaction_by_id():
    response = client.get("/transactions/TXN_00000000")
    assert response.status_code == 200
    assert response.json()["transaction_id"] == "TXN_00000000"


def test_get_transaction_not_found():
    response = client.get("/transactions/TXN_NONEXISTENT")
    assert response.status_code == 404


def test_create_transaction():
    payload = {
        "customer_id": "CUST_9999",
        "amount": 42.50,
        "currency": "EUR",
        "transaction_type": "PURCHASE",
        "merchant_category": "GROCERY",
    }
    response = client.post("/transactions/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["customer_id"] == "CUST_9999"
    assert data["amount"] == 42.50
