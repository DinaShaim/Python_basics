# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

print('Введите строку из нескольких слов')
entered_string = input()
entered_string_list = entered_string.split()
i = 0
while i < len(entered_string_list):
    if len(entered_string_list[i]) <=10:
        print(f'{i + 1}. {entered_string_list[i]}')
    else:
        print(f'{i + 1}. {entered_string_list[i][:10]}')
    i += 1

