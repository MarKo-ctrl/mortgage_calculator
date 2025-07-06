import pytest
from m_calc.mortgage_calc import monthly_payment_amount


def test_monthly_payment_amount():
    # Arrange
    principal = 250000
    rate = 4
    term = 30

    # Act
    payment = monthly_payment_amount(principal,rate,term)

    # Assert
    assert payment == 1193.54