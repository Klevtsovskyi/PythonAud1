

# n * m = n + ... + n = n + n * (m - 1)


def prod(n, m):
    # print(n, m)
    if m == 1:
        return n
    return n + prod(n, m - 1)


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    print(prod(n, m))
