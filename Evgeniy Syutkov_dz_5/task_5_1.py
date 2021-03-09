
def odd_nums(n):
    for num in range(1, n + 1, 2):
        yield num


n = int(input("Введите число: "))
odd_to_n = odd_nums(n)
for i in range(1, n + 1, 2):
    print(next(odd_to_n))