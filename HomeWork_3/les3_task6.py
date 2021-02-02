# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее
# функцию int_func().


def int_func(word):
    flag = False
    for symbol in list(word):
        if ord(symbol) not in range(97, 123):
            flag = True
    if flag:
        return word
    else:
        return word.title()


print('Введите строку из слов, состоящих из латинских букв в нижнем регистре и разделенных пробелом:')
entered_string = input()
entered_string_list = entered_string.split()
entered_string_new = []
for item in entered_string_list:
    entered_string_new.append(int_func(item))
entered_string_new = ' '.join(entered_string_new)

print(entered_string_new)
