from typing import List

power = 5
all_powers = [i**power for i in range(10)]

final_res = []

def get_sum(n: int, powers: List[int]):
    res = 0
    while n > 0:
        res += powers[(n % 10)]
        n = n // 10
    return res

for i in range(2, 1000000):
    if i == get_sum(i, all_powers):
        final_res.append(i)

print(sum(final_res))