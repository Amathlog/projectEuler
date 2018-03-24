import math

number = 600851475143
# number = 13195

def is_prime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

prime_numbers = [2]

def find_next_prime(x):
    while True:
        x += 1
        if is_prime(x):
            return x

while number != 1:
    i = 0
    while True:
        if i == len(prime_numbers):
            prime_numbers.append(find_next_prime(prime_numbers[-1]))
        if number % prime_numbers[i] == 0:
            number /= prime_numbers[i]
            break
        i += 1    

print(prime_numbers[-1])