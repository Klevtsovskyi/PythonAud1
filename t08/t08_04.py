

def is_symmetric(s):
    # print(s)
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_symmetric(s[1:-1])


def invert(s):
    # print(s, s[-1])
    if len(s) <= 1:
        return s
    return s[-1] + invert(s[:-1])


def replace(s, old, new):
    i = s.find(old)
    if i == -1:
        return s
    return s[:i] + new + replace(s[i + len(old):], old, new)


if __name__ == '__main__':
    print(is_symmetric("abccba"))
    print(is_symmetric("ssas"))

    s = "ABC1A23A"
    print(s, invert(s))
    print(s, replace(s, "A", "QQ"))

