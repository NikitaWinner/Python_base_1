def odd_nums(number: int) -> int:
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    x = (i for i in range(1, number + 1, 2))
    return x

n = 15
generator = odd_nums(n)
print(*generator)


