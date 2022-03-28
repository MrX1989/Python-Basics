duration = int(input('Введите длительность периода, в секундах - '))
days = duration // 86400
hour = (duration - days * 86400) // 3600
min = (duration - days * 86400 - hour * 3600) // 60
sec = duration - days * 86400 - hour * 3600 - min * 60
if days == 0 and hour == 0 and min == 0:
    print(f'Длительность периода составляет {sec} сек.')
elif days == 0 and hour == 0:
    print(f'Длительность периода составляет {min} мин {sec} сек.')
elif days == 0:
    print(f'Длительность периода составляет {hour} час {min} мин {sec} сек.')
else:
    print(f'Длительность периода составляет {days} дн {hour} час {min} мин {sec} сек.')
