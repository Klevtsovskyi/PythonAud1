

s = input()

count = 0
for c in s:
    if c in "AEIOUY":
        count += 1

print(count)
