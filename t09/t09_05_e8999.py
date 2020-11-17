

if __name__ == '__main__':
    string = input()

    dct = {}
    max_char = chr(0)
    for char in string:
        dct[char] = dct.get(char, 0) + 1
        if char > max_char:
            max_char = char

    print(max_char, dct[max_char])
