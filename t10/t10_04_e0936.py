# D = |  5  8 |
#     | -3  6 |

# D1 = | 11  8 |
#      | 15  6 |

# D2 = |  5 11 |
#      | -3 15 |

# x1 = D1 / D
# x2 = D2 / D


def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def replace2(matrix, col, jj):
    rez = [[0, 0],
           [0, 0]]
    for i in range(2):
        for j in range(2):
            rez[i][j] = matrix[i][j]

    rez[0][jj] = col[0]
    rez[1][jj] = col[1]

    return rez


if __name__ == '__main__':
    with open("input.txt") as inp:
        A = []
        b = []
        for line in inp:
            row = [float(k) for k in line.split()]
            A.append(row[:-1])
            b.append(row[-1])

        d = det2(A)
        for k in range(2):
            dk = det2(replace2(A, b, k))
            x = dk / d
            print("%.4f" % x)
