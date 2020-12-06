import time

res = set()
start = time.perf_counter()
for a in range(2, 101):
    for b in range(2, 101):
        res.add(a ** b)
end = time.perf_counter()

print(len(res))
print("Duration:", end - start, "s")