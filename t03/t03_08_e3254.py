

n = int(input())


result = 0
i = 0
while n:
    d = n % 10
    n //= 10
    result += d * 2**i
    i += 1

print(result)
