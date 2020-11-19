

def create_matrix(n):
    return [[0 for j in range(n)] for i in range(n)]


def minor(M, im, jm):
    n = len(M)
    rez = create_matrix(n - 1)
    ii = 0
    for i in range(n):
        if i != im:
            jj = 0
            for j in range(n):
                if j != jm:
                    rez[ii][jj] = M[i][j]
                    jj += 1
            ii += 1
    return rez


def det(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    else:
        s = 0
        p = 1
        for j in range(n):
            s += p * M[0][j] * det(minor(M, 0, j))
            p *= -1
        return s


if __name__ == '__main__':
    with open("input.txt") as inp:
        M = []
        for line in inp:
            row = [int(k) for k in line.split()]
            M.append(row)

        print(det(M))
