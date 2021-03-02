
def num_translate(key):
    return numbers.get(key)


numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
           'four': 'четыре', 'five': 'пять',
           'six': 'шесть', 'seven': 'семь',
           'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

print(num_translate(input('Введите число на английском: ')))

