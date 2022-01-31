# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
#
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
#
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int, not_repeat: bool=False) -> list:
    """Возвращает список шуток в количестве count
    not_repeat возвращает список, содержащий count строк, полученный из 3-х заданных списков.
    При этом каждая строка содержит по одному элементу каждого списка.
    Если not_repeat передаётся со значением True, то возвращается список строк без повторов,
    но при этом count не может быть больше длины заданных списков, в противном случаи возвращается предупреждение"""
    if not_repeat:
        if count <= len(nouns):
            nouns_2 = nouns.copy()
            adverbs_2 = adverbs.copy()
            adjectives_2 = adjectives.copy()
            list_out = []
            for i in range(count):
                list_out.append(nouns_2.pop(random.randrange(len(nouns_2))) + " " +
                             adverbs_2.pop(random.randrange(len(adverbs_2))) + " " +
                             adjectives_2.pop(random.randrange(len(adjectives_2))))
            return list_out
        else:
            return 'Хватит уже шутить, а то начнёшь повторяться :)'
    list_out = []
    for i in range(count):
        list_out.append(random.choice(nouns) + " " +  random.choice(adverbs) + " " +  random.choice(adjectives))
    return list_out

print(get_jokes(3))
print(get_jokes(10))


# Раскомментируйте для реализации подзаданий: документирование, флаг и именованные аргументы
# def get_jokes_adv(...) -> list:
#     # пишите реализацию здесь
#     return []