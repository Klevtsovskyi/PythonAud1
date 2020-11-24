

def a(n):
    p = 1
    for k in range(1, n + 1):
        p *= (1 + 1/(k*k))
    return p


if __name__ == '__main__':
    n = int(input())

    print(a(n))
