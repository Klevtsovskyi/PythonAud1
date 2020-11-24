

def tribonacci(n):
    t0 = 0
    t1 = 1
    t2 = 1
    for i in range(n):
        t3 = t2 + t1 + t0
        t0 = t1
        t1 = t2
        t2 = t3
    return t0


def tribonacci_v2(n):
    t0 = 0
    t1 = 1
    t2 = 1
    for i in range(n):
        t0, t1, t2, = t1, t2, t2 + t1 + t0
    return t0


if __name__ == '__main__':
    n = int(input())

    print(tribonacci(n))
    print(tribonacci_v2(n))
