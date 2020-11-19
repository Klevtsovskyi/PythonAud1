

def fill_matrix(n, m):
    matrix = []
    counter = 1
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(counter)
            counter += 1
    return matrix


def print_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print()


if __name__ == '__main__':
    n, m = [int(k) for k in input().split()]
    matrix = fill_matrix(n, m)
    print_matrix(matrix)
