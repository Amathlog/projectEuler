import math

def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False
    if n == 2:
        return True
    for i in range(3, int(math.sqrt(n)+1), 2):
        if n % i == 0:
            return False
    return True

def is_palindrome(x):
    x = str(x)
    max_len = len(x)
    for i in range(max_len):
        if x[i] != x[-(i+1)]:
            return False
    return True

def fibo(max_value=-1):
    a = 1
    b = 2
    yield a
    while True:
        a, b = b, a+b
        yield a
        if max_value != -1 and b > max_value:
            break