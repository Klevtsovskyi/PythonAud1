

n = int(input())


m = n
k = 0
while m:
    k = k * 10 + m % 10
    m //= 10

if k == n:
    print("Yes")
else:
    print("No")
