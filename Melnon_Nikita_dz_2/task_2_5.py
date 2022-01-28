# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
#
# [57.8, 46.51, 97, ...]
# a) Привести каждый элемент списка к виду <r> руб <kk> коп и собрать их в одну строку через запятую.
# Пример:
# 57 руб 80 коп, 46 руб 51 коп ...
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
#
# b) Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
#
# c) Создать новый список, содержащий те же цены, но отсортированные по убыванию.
#
# d) Вернуть цены пяти самых дорогих товаров.
# Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

from random import uniform
from sys import getsizeof


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    final_str = ''
    for i in list_in:
        r = int(i)
        kk = int(i * 100 % 100)
        final_str += (f"'{r} руб {kk} коп',")
    return final_str

my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(f'Преобразованная строка: {result_1}')

id_my_list = id(my_list)

def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_in.sort()
    return list_in


result_2 = sort_prices(my_list)
print(f'Отсортированный список по возрастанию: {result_2}')
id_sorted_my_list = id(result_2)
if id_sorted_my_list == id_my_list:
    print(f'id остался прежним: \n 1) id_sorted_my_list - {id_sorted_my_list} \n 2) id_my_list - {id_my_list}')

def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    list_out = sorted(list_in, reverse=True)
    return list_out


result_3 = sort_price_adv(my_list)
print(f'Отсортированный список по убыванию: {result_3}')


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    list_out = []
    sort_list = sort_price_adv(list_in)
    for i in range(5):
        list_out.append(sort_list[i])
    return list_out


result_4 = check_five_max_elements(my_list)
print(f'Пять максимальных значений: {result_4}')