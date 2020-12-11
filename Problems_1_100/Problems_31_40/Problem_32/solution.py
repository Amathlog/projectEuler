# We know that (A * B) % C = ((A % C) * (B % C)) % C
# If we take C = 10, it means that the first digit
# of the first digit A multiplied by the first digit of B should be 
# equal to the first digit of A * B
# So this first digit can't be one, as 1 * x = 1.
#
# Also, 99 * 99 = 9801 => 8 digits (not enough)
# 99 * 999 = 98901 => 10 digits (too big)
# So A * B = C with either
# A = 2 digits, B = 3 digits, C = 4 digits or
# A = 1 digit, B = 4 digits, C = 4 digits

from itertools import permutations
from time import perf_counter

start = perf_counter()

def find_all_valid_pair_of_first_digits():
    res = []
    for i in range(2, 10):
        for j in range(i+1, 10):
            digit = (i * j) % 10
            if digit != i and digit != j and digit != 0:
                res.append((i, j, digit))
    return res

first_digits = find_all_valid_pair_of_first_digits()

res = set()

for digits in first_digits:
    for i, j, k in permutations(digits):
        remaining_digits = [n for n in range(1,10) if n != i and n != j and n != k]
        # Generate all permutations
        for perm in permutations(remaining_digits):
            # First case
            a = perm[0] * 10 + i
            b = perm[1] * 100 + perm[2] * 10 + j
            c = perm[3] * 1000 + perm[4] * 100 + perm[5] * 10 + k
            if a * b == c:
                res.add(c)

            # Second case
            a = i
            b = perm[0] * 1000 + perm[1] * 100 + perm[2] * 10 + j
            # c is same
            if a * b == c:
                res.add(c)

print(res)
print(sum(res))
print(f"Time: {perf_counter() - start}s")
