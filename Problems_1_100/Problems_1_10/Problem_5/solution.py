"""
2520 is the smallest number that can be divided by
all numbers between 1 and 10.
This number is equal to 5*7*8*9
If we look closely, we find that this list contains
only prime numbers OR powered prime numbers (8 = 2^3 ; 9 = 3^2)

Therefore the method is to generate the list of prime
numbers that are contained between 1 and N. (For the example N=10),
and find the biggest power p for each prime number x that satify
the condition x^p <= N, and replace x by x^p

For N=20, the list is [1, 5, 7, 9, 11, 13, 16, 17, 19]
"""

import math 
from utils.util import is_prime

def list_to_prime(x):
    res = []
    for i in range(1, x+1):
        if is_prime(i):
            res.append(i)
    for i in range(1, len(res)):
        p = int(math.log(x, res[i]))
        res[i] **= p

    return sorted(res) 

# max_n = 10
max_n = 20

prime_list = list_to_prime(max_n)
print(prime_list)
res = 1
for x in prime_list:
    res *= x
print(res)
