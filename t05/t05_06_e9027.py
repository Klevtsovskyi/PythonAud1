

n = int(input())
digits = [0] * 10

while n:
    d = n % 10
    n //= 10
    digits[d] += 1

print(*digits)
