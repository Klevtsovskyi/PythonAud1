

import math


def is_prime(m):
    if m == 1:
        return False
    for i in range(2, int(math.sqrt(m)) + 1):
        if m % i == 0:
            return False
    return True


def invert(m):
    s = str(m)
    s = s[::-1]
    m = int(s)
    return m


if __name__ == '__main__':
    a, b = [int(n) for n in input().split()]
    count = 0
    for i in range(a, b + 1):
        if is_prime(i) and is_prime(invert(i)):
            count += 1

    print(count)
