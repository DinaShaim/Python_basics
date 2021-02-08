# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

total_salary = 0
i = 0

with open("les5_text_3.txt", "r", encoding='utf-8') as my_text_f:
    print("Сотрудники, имеющие оклад менее 20 тыс.:")
    for line in my_text_f:
        i += 1
        salary = float(line.split()[1])
        if salary < 20_000:
            print(line, end='')
        total_salary += salary
    average_salary = round(total_salary / i, 2)
print(f'Средняя величина дохода сотрудников {average_salary}')

