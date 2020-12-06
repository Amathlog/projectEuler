s = []

with open("number") as f:
    data = f.readlines()

for line in data:
    line = line[:-1] # Remove "\n"
    s.append(int(line))
print(s)
res = str(sum(s))
print(res[:10])
