

import math


def is_full_square(m):
    sqrt = math.sqrt(m)
    if sqrt == int(sqrt):
        return True
    else:
        return False


def is_power_of_five(m):
    while m >= 5:
        if m == 5:
            return True
        m /= 5
    return False


def is_prime(m):
    for i in range(2, int(math.sqrt(m)) + 1):
        if m % i == 0:
            return False
    return True


if __name__ == '__main__':
    nums = [int(n) for n in input().split()]
    for n in nums:
        if is_full_square(n):
            print(n, " - повний квадрат")
        if is_power_of_five(n):
            print(n, " - є степенем п'яти")
        if is_prime(n):
            print(n, " - просте")
