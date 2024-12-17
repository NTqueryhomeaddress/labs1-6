# Сторонний платежный интерфейс
class ThirdPartyPaymentGateway:
    def make_payment(self, amount):
        return f"Paid {amount} using Third Party Payment Gateway."

# Адаптер для приведения интерфейса в удобный вид
class PaymentAdapter:
    def __init__(self, gateway):
        self.gateway = gateway

    def pay(self, amount):
        return self.gateway.make_payment(amount)