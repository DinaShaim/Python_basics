# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_text_f = open("les5_text_2.txt", "r", encoding='utf-8')
i = 0
words = []
for line in my_text_f:
    i += 1
    print(f'В {i} строке находится  {len(line.split())} слов')
print(f'Всего сток {i}')
my_text_f.close()
