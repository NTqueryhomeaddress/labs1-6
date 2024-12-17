from abc import ABC, abstractmethod

# Абстрактный класс заказа
class Order(ABC):
    @abstractmethod
    def process(self):
        pass

# Конкретные типы заказов
class PhysicalOrder(Order):
    def process(self):
        return "Processing physical order. Packaging and shipping."

class DigitalOrder(Order):
    def process(self):
        return "Processing digital order. Sending download link."

# Фабрика для создания заказов
class OrderFactory(ABC):
    @abstractmethod
    def create_order(self):
        pass

class PhysicalOrderFactory(OrderFactory):
    def create_order(self):
        return PhysicalOrder()

class DigitalOrderFactory(OrderFactory):
    def create_order(self):
        return DigitalOrder()