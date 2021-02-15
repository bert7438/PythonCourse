import math


def f11(x, y):
    s1 = math.sqrt(math.sin(x ** 7 - 97 * y ** 6) + math.cos(x))
    s2 = math.sqrt((88 * y ** 3 - 33 * y ** 2) / (x ** 3 / 91 + 3 * y))
    s3 = math.sqrt((math.cos(y) + y ** 8) / (32 * y ** 6 + math.e ** x - 53))
    return s1 - s2 - s3


def f12(x):
    if x < 94:
        return 69 * x ** 8 - math.e ** x
    elif 94 <= x < 184:
        return (97 * x ** 8 + math.cos(x) + 91) ** 7 - math.log(x)
    elif 184 <= x < 247:
        return x ** 3 / 58 + 76 * x ** 5 + 8
    elif 247 <= x < 331:
        return math.cos(math.sin(math.cos(x) + x ** 8)) + 27 * x ** 6
    elif x >= 341:
        return math.cos(x ** 3 - 32 * x ** 7) - x ** 6


def f13(n, m):
    s1 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s1 += 20 * i ** 3 - 64 * i ** 6 + 65

    s2 = 0
    for i in range(1, n + 1):
        s2 += math.e ** i - i ** 4 + 59

    return 21 * s1 + s2


def f14(n):
    if n == 0:
        return 6
    else:
        return math.sin(f14(n - 1)) - 1 / 5 * f14(n - 1)
