# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

import random

# list_numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

list_numbers = [random.randint(0, 10) for i in range(random.randint(0, 10))]
print(list_numbers)
new_list = [item for item in list_numbers if list_numbers.count(item) == 1]
print(new_list)
