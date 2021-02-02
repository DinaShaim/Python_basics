# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
# ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел
# будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


flag = False
summa = 0


def sum_numbers(list_numbers):
    global flag
    summa_numbers = 0
    for item in list_numbers:
        if item == "*":
            flag = True
            break
        else:
            summa_numbers += int(item)
    return summa_numbers


while True:
    if flag:
        break
    else:
        print('Введите строку из чисел, разделенных пробелом, для завершения введите *')
        entered_string = input()
        if entered_string == '*':
            break
        else:
            entered_string_list = entered_string.split()
            try:
                summa += sum_numbers(entered_string_list)
                print(f'Сумма чисел равна {summa}')
            except ValueError:
                print('Для выхода нвжмите *, для продолжения вводите только числа')
