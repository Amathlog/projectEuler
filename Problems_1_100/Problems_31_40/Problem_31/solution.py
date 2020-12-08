pool = [200, 100, 50, 20, 10, 5, 2, 1]

def get_possibilities(_target, previous_factors = tuple()):
    pointer = len(previous_factors)
    if pointer >= len(pool):
        if _target != 0:
            return []
        else:
            return [previous_factors]

    res = []
    coef = _target // pool[pointer]
    for i in range(coef + 1):
        new_target = _target - i * pool[pointer]
        new_factors = previous_factors + (i, )
        res += get_possibilities(new_target, new_factors)
    
    return res

for i in range(len(pool)):
    target = pool[-i-1]
    print(f"{target}: {len(get_possibilities(target))}")
