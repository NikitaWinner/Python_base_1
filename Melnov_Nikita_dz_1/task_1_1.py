# не успел изучить, как работают функции def, return, поэтому пока без них(

# ========= Первый вариант реализации с переприсваиванием значения в переменную duration ==============================

while True:
    duration = int(input('Введите кол-во секунд: '))
    days = duration//86400  # нахожу кол-во дней
    duration -= days * 86400  # вычитаю использованные секунды, что бы далее работать с остатком
    hours = duration//3600
    duration -= hours * 3600
    minutes = duration//60
    duration -= minutes * 60
    seconds = duration
    print(f"{days} дн {hours} час {minutes} мин {seconds} сек")

# ================ Второй вариант реализации с инициализацией дополнительных переменных =======================
seconds_in_minute = 60
seconds_in_hour = 3600
seconds_in_day = 86400
hours_in_day = one_day // one_hour
while True:
    duration = int(input('Введите кол-во секунд: '))
    total_days = (duration // second_in_day)
    total_hours = (duration // second_in_hour - hours_in_day * total_days)
    total_minutes = (duration // seconds_in_minute % seconds_in_minute)
    total_seconds = duration % seconds_in_minute
    print(f"{total_days} дн {total_hours} час {total_minutes} мин {total_seconds} сек")

