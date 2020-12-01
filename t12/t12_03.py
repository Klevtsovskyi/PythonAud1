

# p0 = p1 = p2 = 1
# pk = p(k-2) + p(k-3), k >= 3


def padovan(a):
    p0 = p1 = p2 = 1
    k = 0
    while p1 < a:
        p3 = p1 + p0
        p0 = p1  # k
        p1 = p2  # k+1
        p2 = p3  # k+2
        k += 1
    return p0, k


if __name__ == '__main__':
    a = int(input())
    p, k = padovan(a)
    print(p, k)
