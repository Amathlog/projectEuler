
# The algorithm to compute decimals of a rational number
# is the same algorithm we use in middle school to compute
# divisions by hand.
# If the reminder of the division is equal to 0, we have
# a finite number of decimals and then no cycle.
# But if the reminder goes back to a value that was already
# seen as a reminder, we will have a cycle.
#
# The idea here is to keep in memory all the reminder we saw
# in a set. It's faster to do a inclusion test in a set.
# We also need to know at which "index" of the decimal the 
# reminder was, to know where the cycle begins.
def get_decimal_with_cycle(n: int):
    res = []
    curr = 10
    values = set([curr])
    ordered_values = [curr]
    while curr != 0:
        decimal = curr // n
        res.append(str(decimal))
        curr = curr % n * 10
        if curr in values:
            break
        values.add(curr)
        ordered_values.append(curr)

    if curr == 0:
        return res, None

    for i in range(len(ordered_values)):
        if ordered_values[i] == curr:
            return res, i

def test_with_one_number(n: int):
    l, mu = get_decimal_with_cycle(n)
    if mu is None:
        print (f"1/{n}: 0." + "".join(l))
    else:
        print(f"1/{n}: 0." + "".join(l[0:mu]) + "(" + 
            "".join(l[mu:]) + ")")

def test_with_20_first_numbers():
    for i in range(2, 21):
        test_with_one_number(i)
    
def find_max_decimal_cycle(d: int):
    n = 0
    max_decimals = 0
    for i in range(3, d):
        l, mu = get_decimal_with_cycle(i)
        if mu is None:
            # No cycle
            continue

        lambda_ = len(l) - mu

        # Find a cycle, compare its length
        if lambda_ > max_decimals:
            max_decimals = lambda_
            n = i
            
    # Print the result with a pretty print
    print(f"Number found: {n}. Length: {max_decimals}")
    test_with_one_number(n)


if __name__ == "__main__":
    find_max_decimal_cycle(1000)
    #test_with_one_number(983)