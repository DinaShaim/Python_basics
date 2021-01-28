# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

print('Введите два целых числа')
a = int(input())
b = int(input())
print('Введите знак операции')
z = input()
flag = 1
result = None
if z == '+':
    result = a + b
elif z == '-':
    result = a - b
elif z == '*':
    result = a * b
elif z == '/':
    if b == 0:
        print("Деление на ноль не возможно")
        flag = 0
    else:
        result = a / b
else:
    print("Неизвестная введенная операция")
    flag = 0
if flag == 1:
    print(f"Рузьтат выражения {a} {z} {b} равен {result}")
