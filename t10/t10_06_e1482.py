

def create_matrix(n, m):
    return [[0 for j in range(m)] for i in range(n)]


def product(A, B):
    n1 = len(A)
    m1 = len(A[0])
    n2 = len(B)
    m2 = len(B[0])

    C = create_matrix(n1, m2)
    for i in range(n1):
        for j in range(m2):
            s = 0
            for r in range(m1):
                s += A[i][r] * B[r][j]
            C[i][j] = s
    return C


if __name__ == '__main__':
    n1, m1 = [int(k) for k in input().split()]
    A = []
    for i in range(n1):
        row = [int(k) for k in input().split()]
        A.append(row)

    n2, m2 = [int(k) for k in input().split()]
    B = []
    for i in range(n2):
        row = [int(k) for k in input().split()]
        B.append(row)

    # print(A)
    # print(B)

    if m1 != n2:
        print(-1)
    else:
        C = product(A, B)
        print(n1, m2)
        for row in C:
            print(*row)
