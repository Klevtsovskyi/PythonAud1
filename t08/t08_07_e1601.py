

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == '__main__':
    a, b = [int(n) for n in input().split()]
    print(gcd(a, b))
