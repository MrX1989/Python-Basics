def num_translate(number):
    """
    Функция, по переводу числа (от 0 до 10) с английского на русский язык. При соответствии аргумента функции с ключом в словаре
    translation, выводится перевод на русский язык, при его отсутствии возвращается None.
    :param number: вводится пользователем на английском языке, и приводится к значению в нижнем регистре.
    """
    if number in translation:
        print(f'Перевод с английского слова "{text_number}" - "{translation[text_number]}"')
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

text_number = str(input('Введите число прописью (на английском) языке - ')).lower()
num_translate(text_number)
