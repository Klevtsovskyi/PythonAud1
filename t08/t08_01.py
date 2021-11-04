# n! = 1 * 2 * 3 * ... * n
# n! = (n - 1)! * n
# 0! = 1

def fact(n):
    if n == 0:
        return 1
    return fact(n - 1) * n


if __name__ == '__main__':
    n = int(input())
    print(fact(n))
