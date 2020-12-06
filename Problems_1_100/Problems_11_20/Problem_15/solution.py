def generate_grid(n):
    res = []
    for i in range(n):
        res.append([])
        for j in range(n):
            if i == 0 or j == 0:
                res[i].append(1)
            else:
                res[i].append(res[i-1][j] + res[i][j-1])
    return res

grid = generate_grid(21)
print(grid[-1][-1])

# It is also the Pascal triangle. Therefore, it is equal
# to binomial(2*n, n).

def factorielle(x):
    if x == 1:
        return 1
    else:
        return factorielle(x-1) * x

def binomial(n, k):
    n, k = sorted((n,k),reverse=True)
    return factorielle(n) // (factorielle(k) * factorielle(n-k))

print(binomial(40, 20))
