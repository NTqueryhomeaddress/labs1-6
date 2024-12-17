from lab_python_oop.geometric_figure import GeometricFigure
from lab_python_oop.color import Color

class Rectangle(GeometricFigure):
    figure_name = "Прямоугольник"

    def __init__(self, width, height, color_name):
        self.width = width
        self.height = height
        self.color = Color(color_name)

    def calculate_area(self):
        return self.width * self.height

    def __repr__(self):
        return "{name}: Ширина={width}, Высота={height}, Цвет={color}, Площадь={area}".format(
            name=self.figure_name,
            width=self.width,
            height=self.height,
            color=self.color.color_name,
            area=self.calculate_area()
        )
