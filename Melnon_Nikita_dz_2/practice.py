def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    final_list = []
    for element in list_in:
        if element.isdigit():
            element = int(element)
            element = (f'"{element:02}"')
            final_list.append(element)
        elif element[0] == "-":
            element = int(element)
            element = (f'"{element:03}"')
            final_list.append(element)
        elif element[0] == "+":
            element = int(element)
            element = (f'"+{element:02}"')
            final_list.append(element)
        else:
            final_list.append(element)
    final_list = " ". join(final_list)
    str_out = final_list
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)

def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    final_list = []
    for element in list_in:
        new_list = element.split(' ')
        final_list.append(f'Привет, {(new_list[-1].title())}!')
    list_out = final_list
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)

from random import uniform

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
print(result_1)

