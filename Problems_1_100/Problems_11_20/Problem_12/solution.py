from utils.util import get_divisors
triangle_numbers = [1]

n = 500

while len(get_divisors(triangle_numbers[-1])) <= n:
    # Add a triangle number
    triangle_numbers.append(triangle_numbers[-1] + len(triangle_numbers) + 1)

print(triangle_numbers[-1])