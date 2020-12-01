

def func(a):
    x = 1
    k = 1
    while x <= a:
        k += 1
        x += 1 / k
    return x, k


if __name__ == '__main__':
    a = float(input())
    print(*func(a))
