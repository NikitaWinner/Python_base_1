# ================================= Первый вариант реализации c наставником ================================================

def list_cube_option_1(dataset: list):
    for num in range(1, 1001):
        if num % 2:
            dataset.append(num**3)


def sum_list_1_option_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    summa_digit = 0
    for num in dataset:
        number_list = num
        number_summ = 0
        while num % 10 != 0:
            number_summ += num % 10
            num //= 10
        if number_summ % 7 == 0:
            summa_digit += number_list
    return summa_digit


def sum_list_2_option_1(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    count = 0
    summa_digit = 0
    while count < 2:
        if count == 1:
            for i, num in enumerate(dataset):
                dataset[i] += 17
        summa_digit = 0
        for num in dataset:
            number_list = num
            number_summ = 0
            while num % 10 != 0:
                number_summ += num % 10
                num //= 10
            if number_summ % 7 == 0:
                summa_digit += number_list
        count += 1
    return summa_digit


# ================================= Второй вариант реализации (Помогал Иван Горуцкий) ===========================================


def list_cube_option_2(dataset: list):
    for i in range(1, 1001):
        if i % 2 != 0:
            cube = i ** 3
            dataset.append(cube)


def sum_list_1_option_2(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    digit_summ = 0
    number_plus = 0
    for number in dataset:  # мы берём число из списка датасет
        string_numbers = str(number) # преобразуем в строку
        for string_digit in string_numbers:  # берём цифру от числа
            digit_summ += int(string_digit) # мы превращаем в число
        if digit_summ % 7 == 0: # проверяем на кратность 7
            number_plus += number
        digit_summ = 0

    return number_plus


# ================================= Второй вариант реализации (Помогал Иван Горуцкий и Светлана Львовская) ==================================


def sum_list_1_option_3(dataset: list) -> int:
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
    return summ_num


def sum_list_2_option_3(dataset: list) -> int:
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
    return summ_num



my_list_option_1 = []  # инициализация списка для первого варианта реализации
list_cube_option_1(my_list_option_1)
print("Вариант 1 \n", my_list_option_1)
result_1_1 = sum_list_1_option_1(my_list_option_1)
print(result_1_1)
result_1_2 = sum_list_2_option_1(my_list_option_1)
print(result_1_2)

my_list_option_2 = []  # инициализация списка для второго варианта реализации
list_cube_option_2(my_list_option_2)
print('\n'"Вариант 2 \n", my_list_option_2)
result_2_1 = sum_list_1_option_2(my_list_option_2)
print(result_2_1)


my_list_option_3 = [i ** 3 for i in range(1, 1001, 2)]  # инициализация списка для третьего варианта реализации
print('\n'"Вариант 3 \n", my_list_option_3)
result_3_1 = sum_list_1_option_3(my_list_option_3)
print(result_3_1)
result_3_2 = sum_list_2_option_3(my_list_option_3)
print(result_3_2)



