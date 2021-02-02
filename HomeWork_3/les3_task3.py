# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def max_sum(x1, x2, x3):
    list_numbers = [x1, x2, x3]
    list_numbers.remove(min(list_numbers))
    summa = sum(list_numbers)
    return summa


print(max_sum(int(input('Введите первое число:')),
              int(input('Введите второе число:')),
              int(input('Введите третье число:'))))
