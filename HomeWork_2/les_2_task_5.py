# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

my_list = []
while True:
    print('Нужно вести новый элемент рейтинга (да/нет)?')
    entered_string = input()
    if entered_string.upper() == 'ДА':
        print('Введите новый элемент рейтинга:')
        element = int(input())
        if len(my_list) == 0:
            my_list.append(element)
        else:
            for i in range(len(my_list)):
                if element >= my_list[i]:
                    my_list.insert(i, element)
                    break
                elif element < my_list[len(my_list)-1]:
                    my_list.append(element)
                    break
        print(my_list)
    else:
        break

