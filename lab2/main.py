from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from colorama import Fore, Style

def main():
    N = 5  # Замените на номер вашего варианта

    # Создание объектов
    rectangle = Rectangle(width=N, height=N, color_name="Синий")
    circle = Circle(radius=N, color_name="Зелёный")
    square = Square(side_length=N, color_name="Красный")

    # Вывод информации о фигурах
    print(Fore.BLUE + str(rectangle) + Style.RESET_ALL)
    print(Fore.GREEN + str(circle) + Style.RESET_ALL)
    print(Fore.RED + str(square) + Style.RESET_ALL)

    # Вызов метода внешнего пакета colorama
    print(Fore.YELLOW + "Это сообщение выделено с помощью внешнего пакета colorama." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
