import sys
from utils import is_valid_number

def get_coefficients(args):
    coefficients = []
    for i, coef_name in enumerate(['A', 'B', 'C']):
        coef = None
        if len(args) > i + 1:
            try:
                coef = float(args[i + 1])
            except ValueError:
                print(f"Некорректное значение для коэффициента {coef_name}. Требуется повторный ввод.")
        while coef is None:
            user_input = input(f"Введите коэффициент {coef_name}: ")
            if is_valid_number(user_input):
                coef = float(user_input)
            else:
                print(f"Некорректный ввод для коэффициента {coef_name}. Попробуйте снова.")
        coefficients.append(coef)
    return coefficients
