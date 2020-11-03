

import math


def is_prime(m):
    for i in range(2, int(math.sqrt(m)) + 1):
        if m % i == 0:
            return False
    return True


if __name__ == '__main__':
    n = int(input("Введіть натуральне число: "))
    print("Блтзнюки на відрізку [{}, {}]: "
          .format(n, 2*n))
    for j in range(n, 2*n - 1):
        if is_prime(j) and is_prime(j + 2):
            print(j, j + 2)
