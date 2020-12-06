from utils.util import get_divisors
from collections import Set

abundants = []

value_max = 28123

for i in range(value_max):
    divisors = get_divisors(i)[:-1]
    if sum(divisors) > i:
        abundants.append(i)

sum_abundants = set()

for i in range(len(abundants)):
    for other in abundants[i:]:
        if abundants[i] + other >= value_max:
            break
        sum_abundants.add(abundants[i] + other)

res = 0
for i in range(value_max):
    if i not in sum_abundants:
        res += i

print(res)
