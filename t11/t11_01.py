

# xk / x(k-1) = x^k / k * (k-1) / x^(k-1) = x * (k-1) / k
# x1 = x


def a(x, k):
    p = x
    for i in range(2, k + 1):
        p *= x * (i - 1) / i
    return p


# x0 = 1
# xk / x(k-1) = - x^2 / ((2k-1) * 2k)


def b(x, k):
    p = 1
    for i in range(1, k + 1):
        p *= -1 * x * x / ((2*i - 1) * 2*i)
    return p


if __name__ == '__main__':
    x = float(input())
    k = int(input())

    print(a(x, k))
    print(b(x, k))
