import math
from lab_python_oop.geometric_figure import GeometricFigure
from lab_python_oop.color import Color

class Circle(GeometricFigure):
    figure_name = "Круг"

    def __init__(self, radius, color_name):
        self.radius = radius
        self.color = Color(color_name)

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return "{name}: Радиус={radius}, Цвет={color}, Площадь={area:.2f}".format(
            name=self.figure_name,
            radius=self.radius,
            color=self.color.color_name,
            area=self.calculate_area()
        )
