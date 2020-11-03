

def maxx(*args):
    m = -float("inf")
    for n in args:
        if n > m:
            m = n
    return m


def minn(*args):
    m = float("inf")
    for n in args:
        if n < m:
            m = n
    return m


if __name__ == '__main__':
    x, y, z = [float(n) for n in input().split()]
    a = minn(maxx(x, y), maxx(y, z), x + y + z)
    print(a)
