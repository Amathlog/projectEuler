from collections import defaultdict
temp = defaultdict(list)

res = []

for i in range(10, 100):
    for j in range(i, 100):
        division = i / j
        a = i // 10
        b = i % 10
        c = j // 10
        d = j % 10
        
        if b != 0 and c != 0 and division == a / c and a < c and b == d:
            print(f"{i}/{j} == {a}/{c}")
            res.append((i,j))
        if b != 0 and d != 0 and division == a / d and a < d and b == c:
            print(f"{i}/{j} == {a}/{d}")
            res.append((i,j))
        if a != 0 and c != 0 and division == b / c and b < c and a == d:
            print(f"{i}/{j} == {b}/{c}")
            res.append((i,j))
        if a != 0 and d != 0 and division == b / d and b < d and a == c:
            print(f"{i}/{j} == {b}/{d}")
            res.append((i,j))

a = b = 1
for x, y in res:
    a *= x
    b *= y

print(a / b)
