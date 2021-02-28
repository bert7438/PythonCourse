def f21(x):
    if x[3] == 1993:
        if x[0] == 'ninja':
            if x[4] == 1975:
                return 0
            elif x[4] == 1977:
                return 1
            elif x[4] == 1961:
                return 2
        elif x[0] == 'ioke':
            if x[1] == 'sqlpl':
                return 3
            elif x[1] == 'c++':
                return 4
            elif x[1] == 'xml':
                if x[4] == 1975:
                    return 5
                elif x[4] == 1977:
                    return 6
                elif x[4] == 1961:
                    return 7
    elif x[3] == 1981:
        return 8
    elif x[3] == 1962:
        if x[4] == 1975:
            if x[2] == 'twig':
                return 9
            elif x[2] == 'pony':
                return 10
            elif x[2] == 'tla':
                return 11
        elif x[4] == 1977:
            return 12
        elif x[4] == 1961:
            return 13


def f22(x):
    d = x
    d &= 0x00ffffff
    d <<= 8
    m = x
    m >>= 24
    return d | m


print(f21(['ioke', 'c++', 'tla', 1962, 1977]))
print(f22(0x9866ee43))
