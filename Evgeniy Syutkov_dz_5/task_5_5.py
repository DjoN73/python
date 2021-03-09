from sys import getsizeof
from  time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

start = perf_counter()
result = [i for i in range(len(src)) if src.count(i) == 1]
print(result, getsizeof(result), perf_counter() - start)

result = []
start = perf_counter()
for i in range(len(src)):
    if src.count(i) == 1:
        result.append(i)

print(result, getsizeof(result), perf_counter() - start)
