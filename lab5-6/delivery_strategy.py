from abc import ABC, abstractmethod

# Стратегия доставки
class DeliveryStrategy(ABC):
    @abstractmethod
    def deliver(self):
        pass

class CourierDelivery(DeliveryStrategy):
    def deliver(self):
        return "Delivered via Courier."

class PostDelivery(DeliveryStrategy):
    def deliver(self):
        return "Delivered via Post Office."

class DeliveryContext:
    def __init__(self, strategy: DeliveryStrategy):
        self.strategy = strategy

    def execute_delivery(self):
        return self.strategy.deliver()