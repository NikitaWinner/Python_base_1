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