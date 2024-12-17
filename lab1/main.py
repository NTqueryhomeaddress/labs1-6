import sys
from input import get_coefficients
from solve import solve_quadratic_or_biquadratic

def main():
    print("Решение уравнения вида Ax^4 + Bx^2 + C = 0")
    coefficients = get_coefficients(sys.argv)
    A, B, C = coefficients
    roots = solve_quadratic_or_biquadratic(A, B, C)
    0
    if roots is None:
        print("Уравнение не имеет действительных корней.")
    else:
        print("Действительные корни уравнения:")
        for root in roots:
            print(f"x = {root}")

if __name__ == "__main__":
    main()
