def is_palindrome(x):
    x = str(x)
    max_len = len(x)
    for i in range(max_len):
        if x[i] != x[-(i+1)]:
            return False
    return True

# nb_digits = 2
nb_digits = 3

max_val = 0
i_max = j_max = 0
for i in range(10**(nb_digits-1), 10**nb_digits):
    for j in range(i+1, 10**nb_digits):
        aux = i * j
        if is_palindrome(aux) and aux > max_val:
            max_val = aux
            i_max = i
            j_max = j

print(i_max, j_max, max_val)