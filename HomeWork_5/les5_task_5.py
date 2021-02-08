# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

summa_number = 0
with open("les5_text_5.txt", "+w", encoding='utf-8') as my_text_f:
    number_list = [randint(0, 50) for item in range(10)]
    line = ' '.join(map(str, number_list))
    my_text_f.write(line)
    summa_number = sum(number_list)
    my_text_f.seek(0)
    for line in my_text_f:
        print(line)
    print(f'Сумма чисел равна {summa_number}')
