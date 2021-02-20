def mpy12(x):
    s1 = x << 3
    s2 = x << 2
    return s1 + s2


def mpy16(x):
    s = x << 4
    return s


def mpy15(x):
    s = x << 4
    return s - x


def mpy29(x):
    s1 = x << 4
    s2 = x << 3
    s3 = x << 2
    return s1 + s2 + s3 + x
