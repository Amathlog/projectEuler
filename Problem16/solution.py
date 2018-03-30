# To know how many digits has 2^1000, we need to compute the log
# log_10(2^1000) = 1000 * log_10(2) = 301.02999566398114
# Therefore, there is 301 digits.

import math
power = 1000
nb_digits = int(power * math.log(2, 10)) + 1

res = [1] + [0] * (nb_digits - 1)

# Let's multiply by 2, 1000 times
for _ in range(power):
    retenue = 0
    i = 0
    while i < nb_digits:
        res[i] = res[i] * 2 + retenue
        if res[i] >= 10:
            retenue = 1
            res[i] = res[i] % 10
        else:
            retenue = 0
        i += 1

res_str = "".join([str(c) for c in res[::-1]])
# Since it is python, we an check that the 
# built-in power gives the same results (too easy)
assert(res_str == str(2**power))

print("Sum of all digits:", sum(res))