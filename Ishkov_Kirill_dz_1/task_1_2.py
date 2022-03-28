numbers = []
sum_numbers = 0
sum_numbers_17 = 0
#функция по расчету суммы цифр каждого элемента списка
def sum_digits(element):
    sum = 0
    while element > 0:
        sum += element % 10
        element //= 10
    return sum
#генерация списка нечетных чисел в промежутке от 1 до 1000
for number in range(1, 1001):
    if number % 2 != 0:
        numbers.append(number ** 3)
#в цикле для всех элементов списка определяется сумма цифр (с использованием функции), по условию проверяется деление без остатка (на 7) и суммирование элементов списка, удовлетворяющих условию
for number in numbers:
    if sum_digits(number) % 7 == 0:
        sum_numbers += number
#к каждому элементу списка прибавляется "17" и определяется сумма цифр (с использованием функции), по условию проверяется деление без остатка (на 7) и суммирование увеличенных элементов списка, удовлетворяющих условию
    number = number + 17
    if sum_digits(number) % 7 == 0:
        sum_numbers_17 += number
print(sum_numbers)
print(sum_numbers_17)
