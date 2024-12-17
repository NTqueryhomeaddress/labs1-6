from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    figure_name = "Квадрат"

    def __init__(self, side_length, color_name):
        super().__init__(width=side_length, height=side_length, color_name=color_name)
        self.side_length = side_length  # Дополнительный атрибут для удобства

    def __repr__(self):
        return "{name}: Сторона={side}, Цвет={color}, Площадь={area}".format(
            name=self.figure_name,
            side=self.side_length,
            color=self.color.color_name,
            area=self.calculate_area()
        )
