# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
# со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

dict_firm = {}
summa = 0

with open("les5_js_7.json", "w", encoding='utf-8') as my_text_js:
    with open("les5_text_7.txt", "r", encoding='utf-8') as my_text_f:
        for line in my_text_f:
            firm_line = line.split()
            dict_firm.update({firm_line[0]: int(firm_line[2]) - int(firm_line[3])})
            average_sum = {"average_profit": sum([int(item) for item in dict_firm.values() if int(item) > 0]) /
                                             len([int(item) for item in dict_firm.values() if int(item) > 0])}
        result = [dict_firm, average_sum]
        print(result)
    json.dump(result, my_text_js, ensure_ascii=False)
