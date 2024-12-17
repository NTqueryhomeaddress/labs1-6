def field(items, *args):
    assert len(args) > 0, "Необходимо указать хотя бы одно поле"
    if len(args) == 1:
        field_name = args[0]
        for item in items:
            value = item.get(field_name)
            if value is not None:
                yield value
    else:
        for item in items:
            result = {field_name: item.get(field_name) for field_name in args if item.get(field_name) is not None}
            if result:
                yield result

if __name__ == "__main__":
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]
    
    print("Вывод одного поля 'title':")
    for value in field(goods, 'title'):
        print(value)
    
    print("\nВывод полей 'title' и 'price':")
    for value in field(goods, 'title', 'price'):
        print(value)
