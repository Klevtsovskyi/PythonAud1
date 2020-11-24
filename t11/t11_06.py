

# D1 = | 2 | = 2
# D2 = | 2 3 | = 2*2 - 1*3 = 1
#      | 1 2 |
# Dn = 2 * D(n-1) - 3 * 1 * D(n-2)


def a(n):
    d1 = 2
    d2 = 1
    for i in range(n - 1):
        d3 = 2 * d2 - 3 * d1
        d1 = d2
        d2 = d3
    return d1


if __name__ == '__main__':
    n = int(input())

    print(a(n))
