# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня,
# на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения
# параметров a и b и выводить одно натуральное число — номер дня.

print('Введите сколько километров спортсмен пробежал в первый день:')
start = float(input())
print('Введите значение сколько километров требуется пробежать:')
finish = float(input())

if start > finish:
    print('Введены некорректные начальные значения')
elif start == finish:
    print('В первый день спортсмен достигнет требуемого результата')
else:
    i = 1
    while start < finish:
        start *= 1.1
        i += 1
    print(f'На {i}-й день спортсмен достигнет результата — не менее {finish} км')
