

n = int(input())

count = 0
while True:
    count = count + 1
    n = n // 10
    if n == 0:
        break

print(count)
