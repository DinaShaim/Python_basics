# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.

from itertools import count
from itertools import cycle

# а) итератор, генерирующий целые числа, начиная с указанного

try:
    start = int(input('Введите начальное число последовательности: '))
    finish = int(input('Введите конечное число последовательности: '))
    if finish < start:
        print('Конечное значение меньше начального, невозможно построить последовательность')
    else:
        for item in count(start):
            if item > finish:
                break
            else:
                print(item)
except ValueError:
    print('Введено некорректное значение start и/или finish')

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
print('б) Итератор, повторяющий элементы некоторого списка, определенного заранее.')
list_numbers = [item for item in range(1, 6)]
list_numbers = [item for item in range(1, 6)]
print(f'Исходная последовательность: {list_numbers}')
try:
    end = int(input('Введите количество элементов новой последовательности: '))
    c = 0
    for item in cycle(list_numbers):
        if c >= end:
            break
        print(item)
        c += 1
except ValueError:
    print('Введено некорректное значение finish')
