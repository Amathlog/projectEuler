from utils.util import get_divisors

abundants = []

value_max = 28123
value_max = 28300

for i in range(value_max):
    divisors = get_divisors(i)[:-1]
    if sum(divisors) > i:
        abundants.append(i)

print(abundants)