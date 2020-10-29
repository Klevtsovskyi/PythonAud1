

s = input()

result = ""
prev_c = ""
for c in s:
    if c != prev_c:
        result += c
    prev_c = c

print(result)
