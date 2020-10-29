

with open("input.txt") as finput:
    for s in finput:
        words = s.split()
        for word in words:
            print(len(word), end=" ")
