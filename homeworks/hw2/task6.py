'''Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента —
номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
характеристика товара, например название, а значение — список значений-характеристик,
например список названий товаров.'''

product = ()
product_list = []
result = {}
numeristic = int(input('Введите количество товара: \n'))
name_list = ['название', 'цена', 'количество', 'ед.']
for num in range(numeristic):
    price = {name: input(name + ': ') for name in name_list}
    product = (num + 1, price)
    product_list.append(product)
print(product_list)
for name in name_list:
    name_value = []
    for num in range(numeristic):
        name_value.append(product_list[num][1][name])
    result[name] = list(set(name_value))
print(result)