

def a(n):
    s = 0
    for k in range(1, n + 1):
        s += k
    return s


def b(n):
    s = 0
    p = 1
    for k in range(1, n + 1):
        s += p * 1/k
        p *= -1
    return s


# pn = (-1)^(n-1) * 1/n
# pn / p(n-1) = -1 * (n-1) / n
# p1 = 1


def b_v2(n):
    s = 0
    p = 1
    for k in range(1, n + 1):
        s += p
        p *= -1 * k / (k + 1)
    return s


if __name__ == '__main__':
    n = int(input())

    print(a(n))
    print(b(n))
    print(b_v2(n))
