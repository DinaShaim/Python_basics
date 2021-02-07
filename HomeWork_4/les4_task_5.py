# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

list_numbers = [item for item in range(100, 1001) if item % 2 == 0]
print(list_numbers)

sum_list = reduce(lambda x, y: x * y, list_numbers)
print(f'Произведения всех элементов списка равно: {sum_list}')


