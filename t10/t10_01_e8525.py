

if __name__ == '__main__':
    n = int(input())

    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(0)

    # print(matrix)

    for i in range(n):
        row = [int(k) for k in input().split()]
        for j in range(n):
            matrix[i][j] = row[j]

    # print(matrix)

    count = 0
    ssum = 0
    for i in range(n):
        for j in range(n):
            x = matrix[i][j]
            if x < 0 and x % 2 == 0:
                count += 1
                ssum += x

    print(count, ssum)
