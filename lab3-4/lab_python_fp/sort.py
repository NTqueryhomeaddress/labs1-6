data = [4, -30, 100, -100, 123, 1, 0, -1, -4, 30]

if __name__ == "__main__":
    #lambda-функция
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print("С использованием lambda-функции:")
    print(result_with_lambda)
    
    #Без lambda-функции
    def abs_key(x):
        return abs(x)
    
    result_without_lambda = sorted(data, key=abs_key, reverse=True)
    print("\nБез использования lambda-функции:")
    print(result_without_lambda)
