import math

def solve_quadratic_or_biquadratic(A, B, C):
    if A == 0:
        print("Решение квадратного уравнения Bx^2 + C = 0")
        return solve_quadratic(B, C)
    else:
        print("Решение биквадратного уравнения Ax^4 + Bx^2 + C = 0")
        return solve_biquadratic(A, B, C)

def solve_quadratic(B, C):
    if B == 0:
        if C == 0:
            return [0]  
        else:
            return None  
    discriminant = -C / B
    if discriminant < 0:
        return None  
    elif discriminant == 0:
        return [0]
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        return [-sqrt_discriminant, sqrt_discriminant]

def solve_biquadratic(A, B, C):
    discriminant = B**2 - 4*A*C
    print(f"Дискриминант D = {discriminant}")
    
    if discriminant < 0:
        return None
    elif discriminant == 0:
        y = -B / (2*A)
        if y < 0:
            return None
        elif y == 0:
            return [0]
        else:
            sqrt_y = math.sqrt(y)
            return [-sqrt_y, sqrt_y]
    else:
        sqrt_D = math.sqrt(discriminant)
        y1 = (-B + sqrt_D) / (2*A)
        y2 = (-B - sqrt_D) / (2*A)
        roots = []
        for y in [y1, y2]:
            if y > 0:
                sqrt_y = math.sqrt(y)
                roots.extend([-sqrt_y, sqrt_y])
            elif y == 0:
                roots.append(0)
        return sorted(list(set(roots)))
