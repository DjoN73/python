prices = [54.60, 43, 17.05, 108.25, 12.30, 27, 99.90, 74, 445.90, 3.19]

for i in prices:
    price = str(i)
    rub_kop = price.split('.')
    if price.count('.'):
        print(f'{rub_kop[0]} руб {int(rub_kop[1])} коп', end=', ')
    else:
        rub_kop.append('00')
        print(f'{rub_kop[0]} руб {rub_kop[1]} коп', end=', ')

print(prices, id(prices))

prices.sort()
print(prices, id(prices))

n = sorted(prices, reverse=True)
print(sorted(prices, reverse=True), id(n))

print(n[:5][::-1])