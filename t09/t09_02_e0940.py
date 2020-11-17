

if __name__ == '__main__':
    n = int(input())
    nums = [int(m) for m in input().split()]

    dct = {}
    for num in nums:
        if num in dct:
            dct[num] += 1
        else:
            dct[num] = 1

    for num, count in dct.items():
        if count > n / 2:
            print(num)
            break
    else:
        print(-1)
