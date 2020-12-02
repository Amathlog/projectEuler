from utils.util import is_prime

def get_decimals(n: int, max_decimals: int):
    res = []
    curr = 10
    while len(res) < max_decimals:
        decimal = curr // n
        res.append(str(decimal))
        curr = curr % n * 10
        if curr == 0:
            break
    return res

def cycle_detection(l: list):
    # Floyd's algorithm

    # 1: Start tortoise and hare at index 0
    tortoise_index = 1
    hare_index = 2
    found = False

    # 2: Move them until they reach the same value
    # Tortoise go one by one and hare two by two
    while not found:
        while hare_index < len(l):
            if l[tortoise_index] == l[hare_index]:
                found = True
                break

            tortoise_index += 1
            hare_index += 2

        # If we didn't found it, early out
        if not found:
            return None, None

        # At this point, we might have a cycle.
        # Save the tortoise and hare point to backtrack
        # if it was not one
        save_tortoise = tortoise_index
        save_hare = hare_index

        # 3: Move back the tortoise to the beginning and 
        # continue to advance them at the same speed until they
        # reach the same value again, or the tortoise reached the
        # previous hare point
        tortoise_index = 0
        found = False
        while hare_index < len(l) and tortoise_index != save_tortoise:
            if l[tortoise_index] == l[hare_index]:
                found = True
                break
            tortoise_index += 1
            hare_index += 1

        # If we didn't found it, it means that it was not a cycle.
        # Go back to step 2 (with one more advance step)
        if not found:
            tortoise_index = save_tortoise + 1
            hare_index = save_hare + 2

    # At this point, the tortoise index is the beginning of the cycle
    # We call it "mu"
    mu = tortoise_index

    # 4: Place the hare next to the turtoise, and go through 
    # until the hare meet the same number
    found = False
    hare_index = tortoise_index + 1
    while hare_index < len(l):
        if l[tortoise_index] == l[hare_index]:
            # We might have find it! But it is possible that the
            # found cycle is too short!
            lambda_ = hare_index - tortoise_index

            # To test it, compare two "cycles", if they are the same,
            # we did it!
            # We need to have enough decimal to test though.
            # If we don't, we can't say for sure...
            if mu + 2*lambda_ > len(l):
                return None, None
            
            if l[mu:mu+lambda_] == l[mu+lambda_:mu+2*lambda_]:
                return mu, lambda_

        hare_index += 1

    # If we come here, we failed...
    return None, None

def test_with_one_number(n: int, max_decimals: int):
    l = get_decimals(n, max_decimals)
    if len(l) != max_decimals:
        print (f"1/{n}: 0." + "".join(l))
    else:
        mu, lambda_ = cycle_detection(l)
        if mu is None:
            print(f"1/{n}:", "Error, no cycle detected...")
        else:
            print(f"1/{n}: 0." + "".join(l[0:mu]) + "(" + 
            "".join(l[mu:mu+lambda_]) + ")")
        print(l)

def test_with_20_first_numbers():
    for i in range(2, 21):
        test_with_one_number(i, 50)
    
def find_max_decimal_cycle(d: int):
    n = 0
    max_decimals = 0
    for i in range(3, d, 2):
        # Discard not prime numbers
        if not is_prime(i):
            continue

        test_with_one_number(i, 300)
        # print(i)
        # nb_decimals = 100        
        # l = get_decimals(i, nb_decimals)
        # if len(l) != nb_decimals:
        #     # No cycle
        #     break
        
        # mu, lambda_ = cycle_detection(l)
        # if mu is None:
        #     print(f"{i}: Failure")
        #     continue

        # # Find a cycle, compare its length
        # if lambda_ > max_decimals:
        #     max_decimals = lambda_
        #     n = i
            
    print(n)


if __name__ == "__main__":
    #find_max_decimal_cycle(1000)
    #test_with_20_first_numbers()
    test_with_one_number(997, 300)