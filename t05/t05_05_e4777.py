

v1 = tuple(int(n) for n in input().split())
v2 = tuple(int(n) for n in input().split())

v1 = (v1[2] - v1[0], v1[3] - v1[1])
v2 = (v2[2] - v2[0], v2[3] - v2[1])

len1 = (v1[0]**2 + v1[1]**2)**0.5
len2 = (v2[0]**2 + v2[1]**2)**0.5

sum_v = (v1[0] + v2[0], v1[1] + v2[1])

scal_prod = v1[0]*v2[0] + v1[1]*v2[1]
vect_prod = v1[0]*v2[1] - v1[1]*v2[0]

tr_square = 1/2 * abs(vect_prod)

print("%.9f %.9f" % (len1, len2))
print("%.9f %.9f" % sum_v)
print("%.9f %.9f" % (scal_prod, vect_prod))
print("%.9f" % tr_square)
