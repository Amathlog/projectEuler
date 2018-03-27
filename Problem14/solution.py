already_seen = {1: 1}

def get_collatz_chain_len(x):
    if x in already_seen:
        return already_seen[x]
    
    y = x / 2 if x % 2 == 0 else 3 * x + 1
    already_seen[x] = get_collatz_chain_len(y) + 1
    return already_seen[x]

max_val = 0
i_ = 0

for i in range(1, 1000001):
    aux = get_collatz_chain_len(i)
    if aux > max_val:
        max_val = aux
        i_ = i

print(i_)