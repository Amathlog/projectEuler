from utils.util import is_prime

sum_prime = 2
x = 2000000

for i in range(3, x+1, 2):
    if is_prime(i):
        sum_prime += i

print(sum_prime)