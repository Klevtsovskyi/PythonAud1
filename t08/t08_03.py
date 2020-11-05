

# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1


def C(n, k):
    if k == 0 or n == k:
        return 1
    return C(n - 1, k) + C(n - 1, k - 1)


def pascal_rec(n):
    for i in range(n + 1):
        for j in range(i + 1):
            print(C(i, j), end=" ")
        print()


def pascal(n):
    lst = [0] * (n + 1)
    lst[0] = 1
    print(*lst)
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            lst[j] = lst[j - 1] + lst[j]
        print(*lst)


if __name__ == '__main__':
    pascal_rec(10)
    pascal(10)
