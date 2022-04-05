def num_translate_adv(number):
    """
    Функция, по переводу числа (от 0 до 10) с английского на русский язык. При соответствии аргумента функции с ключом в словаре
    translation, выводится перевод на русский язык, при его отсутствии возвращается None. Функция также выводит перевод значения, исходя
    из регистра первой букый.
    :param number: вводится пользователем на английском языке.
    """
    first_letter = number[0]
    number = number.lower()
    if number in translation and first_letter.islower():
        print(f'Перевод с английского слова "{number}" - "{translation[number]}"')
    elif number in translation and first_letter.isupper():
        print(f'Перевод с английского слова "{number.title()}" - "{translation[number].title()}"')
    else:
        print(None)
        return None


translation = {
    'zero' : 'ноль',
	'one' : 'один',
    'two' : 'два',
    'three' : 'три',
    'four' : 'четыре',
    'five' : 'пять',
    'six' : 'шесть',
    'seven' : 'семь',
    'eight' : 'восемь',
    'nine' : 'девять',
    'ten' : 'десять',
}

text_number = str(input('Введите число прописью (на английском) языке - '))
num_translate_adv(text_number)
