numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
           'four': 'четыре', 'five': 'пять',
           'six': 'шесть', 'seven': 'семь',
           'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_tranlate(word):
    in_word = word.lower()
    if word.istitle() and in_word in numbers:
        return numbers.get(in_word).title()
    return numbers.get(word)


print(num_tranlate(input('Введите число: ')))