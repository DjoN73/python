from random import choice, randrange

def get_jokes(n, repeat=True):
    """
    Функция возвразает случайные шутки, из собранных слов из трех списков
    :param n: количество шуток
    :param repeat: уникальность/неуникальность
    :return: списко случайных шуток
    """

    jokes = []
    while n and len(nouns):
        num = randrange(len(nouns))
        if repeat:
            jokes.append(f"{nouns.pop(num)} {adverbs.pop(num)} {adjectives.pop(num)}")
        else:
            jokes.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        n -= 1
    return jokes


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

n = int(input('Введите количество шуток: '))
print(get_jokes(n))
