

# n = 0: 1
# n = 1: 1 + 1/1
# n = 2: 1 + 1/(1 + 1/1)


def a_rec(n):
    if n == 0:
        return 1
    else:
        return 1 + 1 / a_rec(n - 1)


def a(n):
    r = 1
    for i in range(n):
        r = 1 + 1 / r
    return r


# n = 0: 1
# n = 1: 1 + 1/2
# n = 2: 1 + 1/(2 + 1/2)


def b(n):
    r = 2
    for i in range(n):
        r = 2 + 1 / r
    return r - 1


if __name__ == '__main__':
    n = int(input())

    print(a_rec(n))
    print(a(n))
    print(b(n))
