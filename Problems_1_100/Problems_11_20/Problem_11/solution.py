s = []
with open("grid") as f:
    data = f.readlines()
for line in data:
    s.append([])
    line = line[:-1] # Remove \n
    s[-1].extend(int(n) for n in line.split(' '))

max_prod = 0
n = 4

def generate_line_coords(s):
    return [[(line, col) for col in range(len(s[0]))] for line in range(len(s))]

def generate_col_coords(s):
    return [[(line, col) for line in range(len(s))] for col in range(len(s[0]))]

def genereate_right_diag_coordinates(s):
    x_start = len(s) - 1
    y_start = 0
    res = []
    while y_start < len(s[0]):
        x = x_start
        y = y_start
        res.append([])
        while x < len(s) and y < len(s[0]):
            res[-1].append((x,y))
            x += 1
            y += 1
        if x_start != 0:
            x_start -= 1
        else:
            y_start += 1
    return res

def genereate_left_diag_coordinates(s):
    x_start = 0
    y_start = 0
    res = []
    while y_start < len(s[0]):
        x = x_start
        y = y_start
        res.append([])
        while x >= 0 and y < len(s[0]):
            res[-1].append((x,y))
            x -= 1
            y += 1
        if x_start != len(s) - 1:
            x_start += 1
        else:
            y_start += 1
    return res

def max_coords(s, coords):
    max_val = 0
    for coord in coords:
        if len(coord) < n:
            continue
        for i in range(len(coord) - n + 1):
            prod = 1
            for j in range(n):
                x,y = coord[i+j]
                prod *= s[x][y]
            if prod > max_val:
                max_val = prod
    return max_val 

lines_coords = generate_line_coords(s)
col_coords = generate_col_coords(s)
diag_right_coords = genereate_right_diag_coordinates(s)
diag_left_coords = genereate_left_diag_coordinates(s)

coords = [lines_coords, col_coords, diag_left_coords, diag_right_coords]
print(max([max_coords(s, coord) for coord in coords]))