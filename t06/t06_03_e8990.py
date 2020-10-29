

s = input()

result = ""
for c in s:
    if c in "aeiouy":
        c *= 2
    result += c

print(result)
