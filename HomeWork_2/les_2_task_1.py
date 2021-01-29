# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно
# не запрашивать у пользователя, а указать явно, в программе.

my_list = [5, 'text', None, False, 4.5, 5+6j, [1, 2], (1, 2), {1, 2}, {1: 'a', 2: 'b'}]
print(my_list)

for item in my_list:
    print(f'Тип элемента {item} - {type(item)}')