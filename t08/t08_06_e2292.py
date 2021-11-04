
# 1
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
# fib(n - 1) + fib(n - 2) =  fib(n - 2) + fib(n - 3) + fib(n - 2)


# 2
from sys import setrecursionlimit
setrecursionlimit(100000)

fibs = [0] * 10000
fibs[1] = fibs[2] = 1


def fibb(n):
    if fibs[n] == 0:
        fibs[n] = fibb(n - 1) + fibb(n - 2)
    return fibs[n]


# 3
def fibbb(n):
    f1 = 1
    f2 = 1
    for _ in range(1, n):
        f3 = f2 + f1
        f1 = f2
        f2 = f3
    return f1


t = int(input())
for i in range(t):
    n = int(input())
    print(fibb(n))
