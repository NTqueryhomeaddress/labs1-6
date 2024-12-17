import unittest
from order_factory import PhysicalOrderFactory, DigitalOrderFactory

class TestOrderFactory(unittest.TestCase):
    def test_physical_order(self):
        factory = PhysicalOrderFactory()
        order = factory.create_order()
        self.assertEqual(order.process(), "Processing physical order. Packaging and shipping.")

    def test_digital_order(self):
        factory = DigitalOrderFactory()
        order = factory.create_order()
        self.assertEqual(order.process(), "Processing digital order. Sending download link.")

if __name__ == "__main__":
    unittest.main()