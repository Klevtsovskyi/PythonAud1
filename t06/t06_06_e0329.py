

s = input()

words = s.split()
count = 0
for word in words:
    for c in word:
        if c.isalnum():
            count += 1
            break

print(count)
