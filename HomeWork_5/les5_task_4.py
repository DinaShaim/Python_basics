# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.


from translate import Translator


translator = Translator(from_lang="english", to_lang="russian")
with open("les5_text_4_translation.txt", "w", encoding='utf-8') as my_text_f_translation:
    with open("les5_text_4.txt", "r", encoding='utf-8') as my_text_f:
        for line in my_text_f:
            translation = translator.translate(line.split()[0])
            my_text_f_translation.write(f"{translation} {line.split()[1]} {line.split()[2]} \n")

