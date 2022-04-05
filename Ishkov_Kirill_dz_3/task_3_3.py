def thesaurus(*names):
    """
    Функция, по генерации словаря из списка имен, в котором ключ это первая буква имени, а значением является само имя.
    :param names: вводится необходимое кол-во имен (элементов)
    :return: возвращает значение словаря my_dict
    """
    my_dict = {}
    for name in names:
        first_letter = name[0].capitalize()
        if first_letter not in my_dict:
            my_dict[first_letter] = []
        my_dict[first_letter].append(name)
    print(my_dict)
    return my_dict


thesaurus('Иван', 'Мария', 'Петр', 'Илья')
