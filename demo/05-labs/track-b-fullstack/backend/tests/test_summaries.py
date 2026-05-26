from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_summary_by_customer():
    response = client.get('/transactions/summary/CUST_0000')
    assert response.status_code == 200
    data = response.json()
    assert 'total_transactions' in data
    assert 'total_amount' in data
    assert 'average_amount' in data
    assert 'top_category' in data
    assert 'last_transaction_date' in data


def test_summary_customer_not_found():
    response = client.get('/transactions/summary/CUST_DOES_NOT_EXIST')
    assert response.status_code == 404
