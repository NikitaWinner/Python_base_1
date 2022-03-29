def list_cube_option_1(dataset: list):
    for num in range(1, 1001):
        if num % 2:
            dataset.append(num ** 3)


def list_cube_option_2(dataset: list):
    for i in range(1, 1001):
        if i % 2 != 0:
            cube = i ** 3
            dataset.append(cube)


my_list_option_1 = []  # Соберите нужный список по заданию
list_cube_option_1(my_list_option_1)
print("вариант 1", my_list_option_1)

my_list_option_2 = []  # Соберите нужный список по заданию
list_cube_option_2(my_list_option_2)
print("вариант 2", my_list_option_2)

my_list_option_3 = [i ** 3 for i in range(1, 1001, 2)]  # Соберите нужный список по заданию
print("вариант 3", my_list_option_3)


def sum_list_1_option_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    #count = 0
    #while count < 2:
        #if count == 1:
            #for i, num in enumerate(dataset):
            #    dataset[i] += 17
    summ_digit = 0
    for num in dataset:
        number_list = num
        number_summ = 0
        while num % 10 != 0:
            number_summ += num % 10
            num //= 10
        if number_summ % 7 == 0:
            #print(number_list)
            summ_digit += number_list
        #print(summ_digit)
        #count += 1
    return summ_digit

result_1 = sum_list_1_option_1(my_list_option_1)
print(result_1)


nums = []
for num in range(1, 1001):
    if num % 2:
        nums.append(num ** 3)

count = 0
while count < 2:
    if count == 1:
        for i, num in enumerate(nums):
            nums[i] += 17
    summ_digit = 0
    for num in nums:
        number_list = num
        number_summ = 0
        while num % 10 != 0:
            number_summ += num % 10
            num //= 10

        if number_summ % 7 == 0:
            #print(number_list)
            summ_digit += number_list
    #print(summ_digit)
    count += 1


def sum_list_2_option_1(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    count = 0
    while count < 2:
        if count == 1:
            for i, num in enumerate(dataset):
                dataset[i] += 17
        summ_digit = 0
        for num in dataset:
            number_list = num
            number_summ = 0
            while num % 10 != 0:
                number_summ += num % 10
                num //= 10
            if number_summ % 7 == 0:
                summ_digit += number_list
        count += 1
    return summ_digit

result_2 = sum_list_2_option_1(my_list_option_1)
print(result_2)