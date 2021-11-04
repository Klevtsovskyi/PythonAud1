"""
 ------> k
|   1
|   1 1    C(n, k)
v   1 2 1
n   1 3 3 1
    1 4 6 4 1
    1 5 10 10 5 1
    1 6 15 20 15 6 1
    1 7 21 35 35 21 7 1
    1 8 28 56 70 56 28 8 1

    C(n, k) = n! / (k! * (n - k)!)
    C(n, 0) = C(n, n) = 1
    C(n, k) = C(n - 1, k - 1) + C(n - 1, k)
"""

from math import factorial


def cc(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)


def pascal(n):
    for i in range(n + 1):
        for j in range(i + 1):
            print(cc(i, j), end=" ")
        print()


def c(n, k):
    if k == 0 or n == k:
        return 1
    return c(n - 1, k) + c(n - 1, k - 1)


def pascal_rec(n):
    for i in range(n + 1):
        for j in range(i + 1):
            print(c(i, j), end=" ")
        print()


if __name__ == '__main__':
    pascal_rec(10)
    pascal(10)
