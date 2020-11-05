

fibs = {0: 0, 1: 1, 2: 1}


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def fib_rec1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec1(n - 1) + fib_rec1(n - 2)


def fib_rec2(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        k = n // 2
        if n % 2 == 1:
            return (fib_rec2(k)**2 +
                    fib_rec2(k + 1)**2)
        else:
            return fib_rec2(k) * (fib_rec2(k - 1) +
                                  fib_rec2(k + 1))


def fib_rec3(n):
    if fibs.get(n) is None:
        k = n // 2
        if n % 2 == 1:
            fibs[n] = (fib_rec3(k)**2 +
                       fib_rec3(k + 1)**2) % 10**8
        else:
            fibs[n] = (fib_rec3(k) * (fib_rec3(k - 1) +
                                      fib_rec3(k + 1))) % 10**8
    return fibs[n]


def fib(n):
    f0 = 0
    f1 = 1
    for i in range(n):
        f2 = f0 + f1
        f0 = f1
        f1 = f2
    return f0


if __name__ == '__main__':
    with open("input.txt") as inp:
        for line in inp:
            n, m = [int(k) for k in line.split()]
            print(fib_rec3(gcd(n, m)))
