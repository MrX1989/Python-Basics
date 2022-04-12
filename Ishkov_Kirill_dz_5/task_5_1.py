def odd_number(number):
    """
    Генератор нечетных чисел от 1 до n (включительно)
    """
    for num in range(1, number+1, 2):
        yield num


n = int(input(f'Введить максимальное число - '))
for num in odd_number(n):
    print(num)
