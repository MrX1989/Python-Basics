counter = int(input('Введите количество значений для проверки - '))
time = []
#создаем цикл по созданию списка значений для проверки, генерация в пределах значения counter
for count in range(counter):
    duration = int(input('Введите длительность периода, в секундах - '))
    time.append(duration)
#создаем цикл по созданию списков [дн, час, мин, сек] в пределах списка time
for count in time:
    timelist = []
    timelist.append(count // 86400)
    timelist.append((count - timelist[0] * 86400) // 3600)
    timelist.append((count - timelist[0] * 86400 - timelist[1] * 3600) // 60)
    timelist.append(count - timelist[0] * 86400 - timelist[1] * 3600 - timelist[2] * 60)
    if timelist[0] == 0 and timelist[1] == 0 and timelist[2] == 0:
        print(f'Длительность периода составляет {timelist[3]} сек.')
    elif timelist[0] == 0 and timelist[1] == 0:
        print(f'Длительность периода составляет {timelist[2]} мин {timelist[3]} сек.')
    elif timelist[0] == 0:
        print(f'Длительность периода составляет {timelist[1]} час {timelist[2]} мин {timelist[3]} сек.')
    else:
        print(f'Длительность периода составляет {timelist[0]} дн {timelist[1]} час {timelist[2]} мин {timelist[3]} сек.')
