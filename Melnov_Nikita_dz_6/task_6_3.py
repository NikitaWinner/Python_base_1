import json
import sys
def prep_data(user_file: str, hobby_file: str) -> dict:
    """
    Считывает данные из файла и возвращает словарь, где ключ - фио, значение - хобби
    :param user_file: путть до файла с фио пользователей
    :param hobby_file: путь до файла с хобби пользователей
    :return: словарь - фио: хобби
    """
    user_list = []
    with open(user_file, 'r', encoding='utf-8') as fd:
        for str_ in fd:
            user_list.append(str_.replace(',', ' ').strip())

    hobby_list = []
    with open(hobby_file, 'r', encoding='utf-8') as fr:
        for str_ in fd:
            user_list.append(str_.strip())

    user_dict = {}
    if len(user_list) >= len(hobby_list):
        while len(user_list) > len(hobby_list):
            hobby_list.append(None)
        counter = 0
        for name in user_list:
            user_dict[name] = hobby_list[counter]
            counter += 1
    else:
        user_dict = sys.exit(1)

    return user_dict



