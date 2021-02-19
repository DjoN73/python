number = int(input('Введите число: '))

if number == 1:
    print(number, 'процент')
elif 1 < number < 5:
    print(number, 'процента')
elif number <= 20 or number == 0:
    print(number, 'процентов')
