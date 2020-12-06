# For this problem, b needs to be a prime number, because for
# n = 0, f(n) = n^2 + a*n + b = b
# Also if b is negative, f(0) would be negative.
# So b is positive and a prime number
# I don't have proof yet, but I have the impression that a
# should be negative.
# Let's try that

from utils.util import get_primes, is_prime

def f(n, a, b):
    return n * n + a * n + b

max_n = 0
res_a = 0
res_b = 0

for b in get_primes(1000):
    for a in range(-1000, 1):
        n = 1
        value = f(n, a, b)
        while value > 0 and is_prime(value):
            n += 1
            value = f(n, a, b)
        
        if n - 1 > max_n:
            max_n = n - 1
            res_a = a
            res_b = b

print(f"Found a={res_a} and b={res_b}. Yield {max_n} consecutive primes")
        
