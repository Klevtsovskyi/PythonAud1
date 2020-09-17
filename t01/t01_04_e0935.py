
n = abs(int(input()))

d0 = n // 100
k = n % 100
d1 = k // 10
d2 = k % 10

print(d0, d1, d2, sep="\n")
