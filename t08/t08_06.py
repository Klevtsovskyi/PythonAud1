

def split(n, k, lst):
    if n == 0:
        print(*lst)
        return
    for i in range(1, k + 1):
        m = n - i
        lst.append(i)
        split(m, min(i, m), lst)
        lst.pop()


if __name__ == '__main__':
    n = int(input())
    split(n, n, [])
