unique_num = set()
tmp = set()


def get_uniq_numbers(src: list):
    """
    Генератор, выводящий уникальные элементы списка
    :param src: список с повторяющимися значениями
    :return: список без повторений
    """
    for el in src:
        if el not in tmp:
            unique_num.add(el)
        else:
            unique_num.discard(el)
        tmp.add(el)
    res = [i for i in src if i in unique_num]
    return res

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(get_uniq_numbers(src))