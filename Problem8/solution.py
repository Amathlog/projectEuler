s = []
with open("number") as f:
    while True:
        try:
            c = f.read(1)
        except EOFError:
            break
        if c == '\n':
            continue
        if c == '':
            break

        s.append(int(c))

n = 13
count = 0
max_prod = 0
curr = 1
i = 0

while i < len(s) - n:
    if s[i] == 0:
        i += 1
        curr = 1
        count = 0
        continue

    curr *= s[i]
    count += 1
    if count < n:
        i+=1
        continue
    if count > n:
        count -= 1
        curr //= s[i - n]
    if curr > max_prod:
        max_prod = curr
    i += 1

print(max_prod)
