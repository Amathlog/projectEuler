import math 
from utils.util import is_prime

n = 10001
prime_list = []
i = 2
while len(prime_list) < n:
    if is_prime(i):
        prime_list.append(i)
    i += 1

print(prime_list[-1])