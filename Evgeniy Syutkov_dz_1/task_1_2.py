coub_number = []
summ = 0

for i in range(1, 1000, 2):
    number = i ** 3
    coub_number.append(number)

for i in range(len(coub_number)):
    num = coub_number[i]
    result = 0
    while num != 0:
        result += num % 10
        num = num // 10
    if result % 7 == 0:
        summ += coub_number[i]

print(coub_number)
print(summ)

for i in range(len(coub_number)):
    coub_number[i] += 17
    num = coub_number[i]
    result = 0
    while num > 0:
        result += num % 10
        num = num // 10
    if result % 7 == 0:
        summ += coub_number[i]


print(coub_number)
print(summ)
