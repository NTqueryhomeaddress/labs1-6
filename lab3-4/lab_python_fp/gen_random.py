import random

def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield random.randint(begin, end)

if __name__ == "__main__":
    print("Случайные числа от 1 до 3:")
    for num in gen_random(5, 1, 3):
        print(num)
