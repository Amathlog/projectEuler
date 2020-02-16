from utils.util import get_divisors

memory = {}
amicables = []

for i in range(10001):
    # Remove the last one (which is i)
    temp = sum(get_divisors(i)[:-1])
    memory[temp] = i
    if i in memory and memory[i] == temp and i != temp:
        amicables.append((i, temp))

res = 0
for pairs in amicables:
    print(pairs)
    res += sum(pairs)

print(res)