

import math


def a(x, eps):
    prev = x/2
    while True:
        curr = (prev + x / prev) / 2
        if abs(curr - prev) < eps:
            break
        prev = curr
    return prev


def b(x, eps):
    xn = x/2
    while abs(xn**2 - x) >= eps:
        xn = (xn + x / xn) / 2
    return xn


if __name__ == '__main__':
    x = float(input())
    eps = float(input())

    print(a(x, eps))
    print(b(x, eps))
    print(math.sqrt(x))
