# Задание 2
# Напишите программу, которая из 3 целых чисел выбирает и выводит одно наибольшее.
# Подсказка: Можете воспользоваться решением прошлой задачи и немного его модифицировать
#
num_a = int(input('Введите число а: '))
num_b = int(input('Введите число b: '))
num_c = int(input('Введите число c: '))
if num_a > num_b and num_a > num_c:
    print(f'Наибольшее - {num_a}')
elif num_b > num_a and num_b > num_c:
    print(f'Наибольшее - {num_b}')
elif num_c > num_a and num_c > num_b:
    print(f'Наибольшее - {num_c}')
else:
    print(f'Есть одинаковые числа')