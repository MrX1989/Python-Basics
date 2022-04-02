def compare_id():
    if id_base == id_new:
        print(f'ID списков совпадают, т.к новый ID = {id_new}. Объекты списков не изменены.')
    else:
        print(f'ID списков различаются, т.к новый ID = {id_new}. Объекты списков изменены.')
    return id_new

prices = [7.07, 18.4, 17.02, 67.14, 8.99, 96.1, 65, 11.22, 8, 10, 13.11, 98.1, 0.14, 76.1, 17.17]
id_base = id(prices)
print(f'ID списка (исходный) = {id_base}')

#A. Вывод на экран цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Добавлены нули, до сотых.
print('Задание A')
for price in prices:
    price = ('%.2f' % price)
    price = price.split('.')
    print(f'{price[0]} руб {price[1]} коп', end=', ')
print()

#B. Вывод цен, отсортированных по возрастанию (без создания нового списка)
print('Задание B')
prices.sort()
print(prices)
id_new = id(prices)
compare_id()

#C. Создание нового списка, содержащего те же цены, но отсортированные по убыванию.
print('Задание C, вариант 1')
price_up_to_down_1 = sorted(prices, reverse = True)
print(price_up_to_down_1)
id_new = id(price_up_to_down_1)
compare_id()

print('Задание C, вариант 2')
price_up_to_down_2 = list(reversed(prices))
print(price_up_to_down_2)
id_new = id(price_up_to_down_2)
compare_id()

#D. Вывод цен пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
print('Задание D')
print(f'Пять самых дорогих товаров (сортировка по возрастанию) - {sorted(prices)[-5:]}')
