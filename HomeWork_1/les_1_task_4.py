# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

print('Введите целое положительное число')
x = int(input('Число =  '))
max_el = 0
while True:
    if (x % 10) > max_el:
        max_el = x % 10
    x = x // 10
    if not x != 0:
        break
print(f"Максимальный элемент равен {max_el}")