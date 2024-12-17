import unittest
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

class TestGeometricFigures(unittest.TestCase):

    def test_rectangle_area(self):
        rect = Rectangle(width=4, height=5, color_name="Красный")
        self.assertEqual(rect.calculate_area(), 20)

    def test_circle_area(self):
        circle = Circle(radius=3, color_name="Зелёный")
        self.assertAlmostEqual(circle.calculate_area(), 28.274333882308138)

    def test_square_area(self):
        square = Square(side_length=4, color_name="Синий")
        self.assertEqual(square.calculate_area(), 16)

    def test_square_inheritance(self):
        square = Square(side_length=4, color_name="Синий")
        self.assertIsInstance(square, Rectangle)
        self.assertIsInstance(square, Square)

    def test_color_property(self):
        rect = Rectangle(width=2, height=3, color_name="Жёлтый")
        self.assertEqual(rect.color.color_name, "Жёлтый")
        rect.color.color_name = "Фиолетовый"
        self.assertEqual(rect.color.color_name, "Фиолетовый")

if __name__ == '__main__':
    unittest.main()
