

n = int(input())


s = 0
p = 1
while n != 0:
    d = n % 10
    n //= 10
    s += d
    p *= d

print("%.3f" % (p/s))
