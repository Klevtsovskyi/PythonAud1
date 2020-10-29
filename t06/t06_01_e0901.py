

s = input()

count = 0
for c in s[1:]:
    if c in "+-*":
        count += 1

# count = s[1:].count("+") + s[1:].count("-") + s.count("*")
print(count)
