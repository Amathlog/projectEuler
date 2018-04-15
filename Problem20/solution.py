from utils.util import factorielle

def digit_sum(n):
    res = 0
    while n != 0:
        res += n % 10
        n //= 10
    return res

print("Res:", digit_sum(factorielle(100)))