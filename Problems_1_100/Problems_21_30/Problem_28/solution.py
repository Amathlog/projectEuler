# Starting at the center of the matrix: 1 (n = 0)
# Left-bottom diagonal: v_n = 8 * n - 6 + v_{n-1}
# Right-bottom diagonal: w_n = 8 * n - 4 + w_{n-1}
# Right-top diagonal: x_n = 8 * n - 2 + x_{n-1}
# Left-top diagonal: u_n = (2 * n + 1) ** 2

def next_v(n: int, prev_v: int):
    if n == 0:
        return 1
    return 8 * n - 6 + prev_v

def next_w(n: int, prev_w: int):
    if n == 0:
        return 1
    return 8 * n - 4 + prev_w

def next_x(n: int, prev_x: int):
    if n == 0:
        return 1
    return 8 * n - 2 + prev_x

def u_n(n: int):
    return (2 * n + 1) ** 2

def get_diag_sum_for_matrix_n(n: int):
    if (n % 2 == 0):
        return None

    n = (n + 1) // 2

    u = 1
    v = 1
    w = 1
    x = 1
    res = 1

    for i in range(1, n):
        u = u_n(i)
        v = next_v(i, v)
        w = next_w(i, w)
        x = next_x(i, x)
        res += u + v + w + x

    return res

if __name__ == "__main__":
    print(get_diag_sum_for_matrix_n(1001))

