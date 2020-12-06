from itertools import permutations

USE_BRUTE_FORCE = True

################## Brute Force ####################
if USE_BRUTE_FORCE:
    initial_set = list(range(10))
    n = 10

    def listToNumber(l):
        res = 0
        for item in l:
            res = res * 10 + item
        return res

    def numberToStr(n):
        if n > 1e9:
            return str(n)
        return "0" + str(n)

    res = sorted([listToNumber(l) for l in permutations(range(n))])
    print([numberToStr(n) for n in res[:50]])
    print(numberToStr(res[999999]))


################### Other solution ####################

