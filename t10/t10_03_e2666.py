

def fill_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n - 1 - i):
            matrix[i].append(2)
        matrix[i].append(0)
        for j in range(n - i, n):
            matrix[i].append(1)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(*row, sep="")


if __name__ == '__main__':
    n = int(input())

    matrix = fill_matrix(n)
    print_matrix(matrix)
