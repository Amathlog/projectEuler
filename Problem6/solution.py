first_sum = 0
second_sum = 0
n = 100
for i in range(n+1):
    first_sum += i**2
    second_sum += i

print(second_sum**2 - first_sum)