def is_bixextile(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def get_first_days(year):
    if is_bixextile(year):
        february = 29
    else:
        february = 28

    months = [31, february, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return months

bixextile_year = get_first_days(0)
normal_year = get_first_days(1)

# Monday == 0 ; Sunday == 6

days = 366 # 1 Jan 1901
res = 0
for year in range(1901, 2001):
    count_year = bixextile_year if is_bixextile(year) else normal_year
    if year == 2000:
        # Don't count 1 Jan 2001
        count_year = count_year[:-1]
    for count in count_year:
        days += count
        res += 1 if days % 7 == 6 else 0 

print(res)

# Python style
import calendar

cal = calendar.Calendar(firstweekday=6)

res = 0
for year in range(1901, 2001):
    for month in range(1,13):
        for day in cal.itermonthdays(year, month):
            res += 1 if day == 1 else 0
            break

print(res)
