import pytest
import pandas as pd
from lab_exercise import calculate_monthly_savings_by_category, calculate_yearly_category_trend

def test_monthly_savings_by_category():
    df = pd.DataFrame({
        'date': ['2024-01-01', '2024-01-15', '2024-02-01'],
        'category': ['groceries', 'groceries', 'utilities'],
        'amount': [100, 150, 200]
    })
    result = calculate_monthly_savings_by_category(df, 2024, 1)
    assert result['groceries'] == 250

def test_yearly_category_trend():
    df = pd.DataFrame({
        'date': ['2024-01-01', '2024-02-01', '2024-03-01'],
        'category': ['groceries', 'groceries', 'utilities'],
        'amount': [100, 150, 200]
    })
    result = calculate_yearly_category_trend(df, 2024)
    assert result['groceries'] == 250
    assert result['utilities'] == 200
