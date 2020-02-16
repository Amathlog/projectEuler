from pathlib import Path

with Path('p022_names.txt').open() as f:
    data = [i[1:-1] for i in f.read().split(',')]

data = sorted(data)

def string_value(s):
    res = 0
    for c in s:
        res += ord(c) - ord('A') + 1
    return res

final_res = 0
for i, s in enumerate(data):
    final_res += (i+1) * string_value(s)

print(final_res) 
