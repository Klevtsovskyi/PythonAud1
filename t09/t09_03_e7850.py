

if __name__ == '__main__':
    input()
    nums = [int(m) for m in input().split()]

    dct = {}
    for num in nums:
        dct[num] = dct.get(num, 0) + 1

    for num in nums:
        if dct[num] == 1:
            print(num, end=" ")
