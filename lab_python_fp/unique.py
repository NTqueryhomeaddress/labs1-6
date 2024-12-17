class Unique:
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            current = next(self.items)
            comparison_value = current
            if self.ignore_case and isinstance(current, str):
                comparison_value = current.lower()
            if comparison_value not in self.seen:
                self.seen.add(comparison_value)
                return current


if __name__ == "__main__":
    print("Пример с числами:")
    data_numbers = [1, 1, 2, 2, 3, 3, 3]
    for item in Unique(data_numbers):
        print(item)
    
    print("\nПример со строками без игнорирования регистра:")
    data_strings = ['a', 'A', 'b', 'B', 'a', 'A']
    for item in Unique(data_strings):
        print(item)
    
    print("\nПример со строками с игнорированием регистра:")
    for item in Unique(data_strings, ignore_case=True):
        print(item)
