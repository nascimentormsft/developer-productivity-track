import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_summary_by_customer():
    response = client.get('/summary/by-customer/1001?start_date=2024-01-01&end_date=2024-01-31')
    assert response.status_code == 200
    assert 'total' in response.json()

def test_summary_by_merchant():
    response = client.get('/summary/by-merchant/2001')
    assert response.status_code == 200
    assert 'total' in response.json()
