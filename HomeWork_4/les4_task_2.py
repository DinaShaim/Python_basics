# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Элементы, удовлетворяющие
# условию, оформить в виде списка. Для формирования списка использовать генератор.

import random

list_numbers = [round(random.random() * 10, 5) for i in range(random.randint(0, 10))]
print(list_numbers)
items_more_than = [list_numbers[i] for i in range(1, len(list_numbers)) if list_numbers[i] > list_numbers[i - 1]]
print(items_more_than)
