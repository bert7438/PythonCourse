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


def f23(table):
    def transpose(tab):
        return [list(row) for row in zip(*tab)]

    z = transpose(table)
    # remove empty columns
    i = 0
    while i < len(z):
        zero_flag = True
        for j in z[i]:
            if j is not None:
                zero_flag = False
                break
        if zero_flag:
            del z[i]
            i -= 1
        i += 1
    # split 2 column
    z.insert(2, [])
    for i in range(len(z[1])):
        z[1][i] = z[1][i].split('&')
    for i in range(len(z[1])):
        t = z[1][i][1]
        z[1][i].remove(t)
        z[2].append(t)
    z[1] = [z[1][i][0] for i in range(len(z[1]))]
    # change to true and false
    for i in range(len(z[0])):
        z[0][i] = z[0][i].replace("Да", "true").replace("Нет", "false")
    # round
    for i in range(len(z[1])):
        z[1][i] = f'{round(float(z[1][i]),2):.2f}'
    # truncate to last name
    for i in range(len(z[2])):
        z[2][i] = z[2][i].split(". ")
    for i in range(len(z[2])):
        z[2][i].remove(z[2][i][0])
    z[2] = [z[2][i][0] for i in range(len(z[2]))]

    return z
