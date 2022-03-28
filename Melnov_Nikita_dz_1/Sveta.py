

def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    summ_digit = 0  # сумма цифр числа
    summ_num = 0  # сумма чисел
    for i in dataset:
        copy_i = i
        while copy_i > 0:
            digit = copy_i % 10  # находим последнюю цифру числа из списка
            summ_digit += digit  # сумма цифр числа
            copy_i //= 10  # отсекаем последнюю цифру
        if summ_digit % 7 == 0: # Проверяем сумму цифр числа на кратность 7
            summ_num += i  # общая сумма цифр
        summ_digit = 0
    return summ_num  # Верните значение полученной суммы


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    for i in range(len(dataset)):
        dataset[i] += 17
    summ_digit = 0
    summ_num = 0
    for i in dataset:
        copy_i = i
        while copy_i > 0:
            digit = copy_i % 10
            summ_digit += digit
            copy_i //= 10
        if summ_digit % 7 == 0:
            summ_num += i
        summ_digit = 0
    return summ_num  # Верните значение полученной суммы


my_list = [i ** 3 for i in range(1, 1001, 2)]  # Соберите нужный список по заданию
print(my_list)
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)