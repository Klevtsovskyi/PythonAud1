

import math


def a(x, eps):
    s = x
    prev = 0
    curr = x
    k = 1
    while abs(curr - prev) >= eps:
        prev = curr
        curr *= -1 * x*x / (2*k * (2*k + 1))
        k += 1
        s += curr
    return s


def b(x, eps):
    s = 1
    prev = 0
    curr = 1
    k = 1
    while abs(curr - prev) >= eps:
        prev = curr
        curr *= -1 * x*x / ((2*k - 1) * 2*k)
        k += 1
        s += curr
    return s


# ak = x^(2k-1) / (2k-1)
# ak/a(k-1) = x^(2k-1) * (2k-3) / (x^(2k-3) * (2k-1)) =
# = x^2 * (2k-3) / (2k-1)
def c(x, eps):
    s = 2*x
    prev = 0
    curr = 2*x
    k = 1
    while abs(curr - prev) >= eps:
        prev = curr
        k += 1
        curr *= x*x * (2*k - 3) / (2*k - 1)
        s += curr
    return s


if __name__ == '__main__':
    x = float(input())
    eps = float(input())

    print(a(x, eps), math.sin(x))
    print(b(x, eps), math.cos(x))
    print(c(x, eps), math.log((1 + x) / (1 - x)))
