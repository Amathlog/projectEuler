from utils.util import fibo

current_digits = 1
index = 1

for i in fibo():
    index += 1
    if i >= 10**current_digits:
        current_digits += 1
    if current_digits == 1000:
        print(index)
        break
