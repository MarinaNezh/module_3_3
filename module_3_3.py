def print_params(a=1, b='кошка', c=True):
    print(f"a: {a}, b: {b}, c: {c}")

# Вызовы функции с разным количеством аргументов
print_params()  # без аргументов
print_params(10)  # только a
print_params(b=25)  # только b
print_params(c=[1, 2, 3])  # только c
print_params(10, 'dog', False)  # все аргументы

# Список
values_list = [42, 'текст', False]

# Словарь
values_dict = {'a': 3.14,'b': 'пример','c': [1, 2]}

# Передаем список и словарь в функцию с распаковкой
print_params(*values_list)
print_params(**values_dict)

# Список 2
values_list_2 = ['строка', 100]

# Проверка
print_params(*values_list_2, 42)  # распаковка списка и передача отдельного параметра
