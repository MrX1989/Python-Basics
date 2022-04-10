from task_4_4_prog import currency_rates

if '__main__' == __name__:
    letter_code = str(input('Введите буквенный код валюты (на английском языке) - ')).upper()
    #для проверки ввести USD, EUR. В "task_4_4_prog" функция выполняется только с аргументом "AMD"
    currency_rates(letter_code)
