from utils.util import fibo

res = 0
for x in fibo(4000000):
    if x % 2 == 0:
        res += x

print(res)