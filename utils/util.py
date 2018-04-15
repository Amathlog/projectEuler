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

def get_divisors(n):
    if n == 1:
        return [1]
    res = [1, n]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            res.append(i)
            if n // i != i:
                res.append(n // i)
    return sorted(res)

computed_factorielles = {0: 1}

def factorielle(n):
    if n in computed_factorielles:
        return computed_factorielles[n]
    computed_factorielles[n] = n * factorielle(n-1)
    return computed_factorielles[n]

if __name__ == "__main__":
    for i in range(1, 10):
        print(i, ":", get_divisors(i))
