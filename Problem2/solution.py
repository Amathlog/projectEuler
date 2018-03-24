def fibo(max_value=-1):
    a = 1
    b = 2
    yield a
    while True:
        a, b = b, a+b
        yield a
        if max_value != -1 and b > max_value:
            break

res = 0
for x in fibo(4000000):
    if x % 2 == 0:
        res += x

print(res)