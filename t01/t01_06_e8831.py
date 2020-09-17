# https://www.e-olymp.com/uk/submissions/7334702
x, y = [float(d) for d in input().split()]

f = 2 * x ** 2 - 4 * x * y + 3 * y ** 2 + (x + y) / 7

print("%.3f" % f)
