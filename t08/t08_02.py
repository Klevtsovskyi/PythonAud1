# n * m = product(n, m)
# n * m = m + m + ... + m
# n * m = (n - 1) * m + m
# 1 * m = m


def prod(n, m):
    # print(n, m)
    if m == 1:
        return n
    return n + prod(n, m - 1)


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    print(prod(n, m))
