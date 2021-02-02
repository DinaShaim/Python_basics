# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в
# виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции
# возведения числа в степень.


def exponentiation(x, y):
    if y > -1 or x < 0:
        return 'Введено неудовлетворяющее условию значение x и/или y'
    else:
        a = 1/x
        x = a
        for i in range(1, abs(y)):
            x = x*a
    return round(x, 5)


def exponentiation_2(x, y):
    if y > -1:
        return 'Введено некорректное значение y'
    else:
        return round(x**y, 5)


try:
    xx = float(input('Введите действительное положительное число x:'))
    yy = int(input('Введите целое отрицательное число y:'))
    print(exponentiation(xx, yy))
    print(exponentiation_2(xx, yy))
except ValueError:
    print('Некорректное значение, для ввода требуются числа')


