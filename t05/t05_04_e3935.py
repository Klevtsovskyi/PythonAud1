

n = int(input())
nums = []

for i in range(n):
    m = int(input())
    nums.append(m)

#for i in range(n // 2):
#    nums[i], nums[-i-1] = nums[-i-1], nums[i]

#print(nums)

print(*nums[::-1])
