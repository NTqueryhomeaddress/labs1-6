from unittest.mock import Mock
from payment_adapter import PaymentAdapter

def test_payment_adapter():
    mock_gateway = Mock()
    mock_gateway.make_payment.return_value = "Paid 100 using Mock Gateway."

    adapter = PaymentAdapter(mock_gateway)
    result = adapter.pay(100)

    assert result == "Paid 100 using Mock Gateway."
    mock_gateway.make_payment.assert_called_with(100)

if __name__ == "__main__":
    test_payment_adapter()
    print("Payment adapter test passed.")