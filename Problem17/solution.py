def number_to_text(n):
    if n == 0:
        return ""
    if n == 1:
        return "one"
    if n == 2:
        return "two"
    if n == 3:
        return "three"
    if n == 4:
        return "four"
    if n == 5:
        return "five"
    if n == 6:
        return "six"
    if n == 7:
        return "seven"
    if n == 8:
        return "eight"
    if n == 9:
        return "nine"
    if n == 10:
        return "ten"
    if n == 11:
        return "eleven"
    if n == 12:
        return "twelve"
    if n == 13:
        return "thirteen"
    if n == 14:
        return "fourteen"
    if n == 15:
        return "fifteen"
    if n in [16, 17, 18, 19]:
        return number_to_text(n%10) + ("teen" if n != 18 else "een")
    if n < 30:
        return "twenty" + number_to_text(n%10)
    if n < 40:
        return "thirty" + number_to_text(n%10)
    if n < 50:
        return "forty" + number_to_text(n%10)
    if n < 60:
        return "fifty" + number_to_text(n%10)
    if n < 100:
        tenth = n // 10
        unit = n % 10
        return number_to_text(tenth) + ("ty" if tenth != 8 else "y") + number_to_text(unit)
    if n < 1000:
        return number_to_text(n//100) + "hundred" + ("and" + number_to_text(n%100) if n%100 != 0 else "")

    return "onethousand"

print(number_to_text(100))

print(sum((len(number_to_text(n)) for n in range(1001))))