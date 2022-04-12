n = int(input(f'Введить максимальное число - '))
gen_odd_number = (number for number in range(1, n+1, 2))
for i in gen_odd_number:
    print(next(gen_odd_number))
