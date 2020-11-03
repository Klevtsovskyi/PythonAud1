

def to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n:
        bit = n % 2
        n //= 2
        binary = str(bit) + binary
    return binary


def to_decimal(binary):
    decimal = 0
    n = 1
    for bit in binary[::-1]:
        decimal += int(bit) * n
        n *= 2
    return decimal


if __name__ == '__main__':
    A = input()
    B = input()
    a = to_decimal(A)
    b = to_decimal(B)
    c = a + b
    C = to_binary(c)
    print(C)
