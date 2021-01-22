# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль —это выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

print('Введите значение выручки фирмы')
revenue = float(input())
print('Введите значение издержек фирмы')
costs = float(input())

if revenue - costs < 0:
    print('Фирма отработала с убытком')
elif revenue - costs == 0:
    print('Полученная выручка покрыла лишь издежки, прибыли нет, убытка тоже нет')
elif revenue - costs > 0:
    print(f'Фирма отработала с прибылью, прибыль составила {(revenue - costs):.2f}')
    profit = (revenue - costs) / revenue
    print(f'Рентабельность равна {profit:.2f}')
    print('Введите численность сотрудников фирмы')
    number_employees = int(input())
    profit_employee = profit / number_employees
    print(f'прибыль фирмы в расчете на одного сотрудника равна {profit_employee:.2f}')