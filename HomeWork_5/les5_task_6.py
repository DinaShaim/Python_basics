# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
#
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

dict_subject = {}
with open("les5_text_6.txt", "r", encoding='utf-8') as my_text_f:
    for line in my_text_f:
        name_subject, watch = line.split(':')
        result_watch = []
        for item in watch:
            if item == ' ' or 48 <= ord(str(item)) <= 57:
                result_watch.append(item)
        str_watch = ''.join(result_watch)
        summa_watch = 0
        for item in str_watch.split():
            if item != ' ':
                summa_watch += int(item)
        dict_subject.update({name_subject: summa_watch})
    print(dict_subject)
