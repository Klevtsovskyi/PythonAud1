

# n! = 1 * 2 * ... * (n - 1) * n
# (n - 1)! = 1 * 2 * ... * (n - 1)
# n! = (n - 1)! * n


def fact(n):
    if n == 0:
        return 1
    return fact(n - 1) * n


if __name__ == '__main__':
    n = int(input())
    print(fact(n))
