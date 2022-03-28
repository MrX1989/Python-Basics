#для диапазона значений от 1 до 100
for percent in range(1, 101):
#если значение равно 1 ИЛИ остаток при делении равен 1 И не равно 11, то вывод "процент"
    if percent == 1 or percent % 10 == 1 and percent != 11:
        print(f'{percent} процент')
#если значение равно 2 ИЛИ 3 ИЛИ 4 ИЛИ остаток при делении равен 2 И не равно 12 ИЛИ остаток при делении равен 3 И не равно 13 ИЛИ остаток при делении равен 4 И не равно 14, то вывод "процента"
    elif percent == 2 or percent == 3 or percent == 4 or percent % 10 == 2 and percent != 12 or percent % 10 == 3 and percent != 13 or percent % 10 == 4 and percent != 14:
        print(f'{percent} процента')
#иначе в остальных случаях, вывод "процентов"
    else:
        print(f'{percent} процентов')
