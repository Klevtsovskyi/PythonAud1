
import math

x1, y1, x2, y2, x3, y3 = [float(d) for d in input().split()]

a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
c = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5

P = a + b + c

p = P / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))

print("%.4f %.4f" % (P, S))
