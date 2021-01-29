# * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж
# хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с
# параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно
# сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.


list_products = []
tuple_products = {'Название': '', 'Цена': '', 'Количество': '', 'Единица измерения': ''}
analytics_products = {'Название': [], 'Цена': [], 'Количество': [], 'Единица измерения': []}
while True:
    print('ВВести данные нового товара (да/нет)?')
    entered_string = input()
    if entered_string.upper() == 'ДА':
        print('Введите номер товара:')
        number = input()
        for item in tuple_products:
            print(f'Введите характеристику {item}:')
            characteristics = input()
            if item == 'Цена' or item == 'Количество':
                characteristics = int(characteristics)
            tuple_products[item] = characteristics
            analytics_products[item].append(tuple_products[item])
        list_products.append((number, tuple_products))
        print(list_products)
        print(analytics_products)
    else:
        break
