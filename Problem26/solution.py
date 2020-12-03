from utils.util import is_prime, _getThreads
from multiprocessing import Queue, Process, Value

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
    for i in range(3, d, 2):
        # Discard not prime numbers
        if not is_prime(i):
            continue

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

def consuming(q1: Queue, q2: Queue):
    while True:
        n = q1.get()

        if n is None:
            break

        l, mu = get_decimal_with_cycle(n)
        if mu is None:
            # No cycle
            continue

        lambda_ = len(l) - mu
        q2.put((n, lambda_))

def compute_max(q1: Queue, q2: Queue):
    max_n = 0
    max_decimal = 0

    while True:
        n, lambda_ = q1.get()

        if n is None:
            break

        if lambda_ > max_decimal:
            max_decimal = lambda_
            max_n = n

    q2.put((max_n, max_decimal))

def find_max_decimal_cycle_mt(d: int):
    nb_threads = _getThreads()
    producer_queue = Queue(nb_threads - 1)
    temp_queue = Queue()
    res_queue = Queue()

    consumers = [Process(target=consuming, 
    args=(producer_queue, temp_queue)) 
    for _ in range(nb_threads-1)]

    max_computer = Process(target=compute_max, 
    args=(temp_queue, res_queue))

    for p in consumers + [max_computer]:
        p.start()

    for i in range(3, d, 2):
        # Discard not prime numbers
        if not is_prime(i):
            continue

        producer_queue.put(i)

    # Signal that it's over for consumers
    for _ in range(len(consumers)):
        producer_queue.put(None)

    # Wait for them
    for p in consumers:
        p.join()

    # Then signal to the max_compute that it's over
    temp_queue.put((None, None))

    # Wait for it
    max_computer.join()

    # And then print the results
    n, lambda_ = res_queue.get()

    # Print the result with a pretty print
    print(f"Number found: {n}. Length: {lambda_}")
    test_with_one_number(n)


if __name__ == "__main__":
    import time

    D = 1000

    start = time.perf_counter()
    find_max_decimal_cycle(D)
    duration = time.perf_counter() - start

    print(f"Single thread: {duration} s")

    start = time.perf_counter()
    find_max_decimal_cycle_mt(D)
    duration = time.perf_counter() - start

    print(f"Multi thread: {duration} s")