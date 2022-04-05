from random import randrange

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

def get_jokes(count, flag=True):
    """
    Функция, возвращает 'count' шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
    nouns, adverbs, adjectives. Второй аргумент функции - 'flag' (по умолчанию True, разрешает повторять слова из списков).
    Указав 'flag=False' при вызове функции генерация шуток будет осуществляться без повторения шуток. Для минимизации ошибок цикла
    реализовано условие проверяющее значение 'flag' и максимальное количество шуток (исходя из количества элементов списка).
    :param count: количество шуток (вводится пользователем) + flag=(по умолчанию True)
    :return:
    """
    maximum = min(len(nouns), len(adverbs), len(adjectives))
    if (count > len(nouns) or count > len(adverbs) or count > len(adjectives)) and flag == False:
        print(f'Невозможно сгенерировать {count} шуток. Уменьшите пожалуйста количество до {maximum}!')
    else:
        for joke in range(count):
            noun = nouns[randrange(len(nouns))]
            adverb = adverbs[randrange(0, len(adverbs))]
            adjective = adjectives[randrange(0, len(adjectives))]
            print(f'Шутка {joke + 1} - {noun.title()} {adverb} {adjective}.')
            if flag == False:
                nouns.remove(noun)
                adverbs.remove(adverb)
                adjectives.remove(adjective)
    return joke


jokes = int(input('Введите количество шуток - '))
get_jokes(jokes, flag=False)
