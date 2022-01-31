#  Задание 1
# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.

def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    translator = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if value in translator:
        str_out = translator.get(value)
    else:
        str_out = "None"
    return str_out


print(num_translate("two"))
print(num_translate("eight"))