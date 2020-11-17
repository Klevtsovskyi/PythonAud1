

if __name__ == '__main__':
    input()
    nums = [int(m) for m in input().split()]

    dct = {}
    for i in range(len(nums)):
        if nums[i] in dct:
            dct[nums[i]][0] = i
            dct[nums[i]][1] += 1
        else:
            dct[nums[i]] = [i, 1, nums[i]]

    if len(nums) == len(dct):
        print("NO")
    else:
        for lst in sorted(dct.values()):
            if lst[1] > 1:
                print(lst[2], end=" ")
