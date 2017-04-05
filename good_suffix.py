def good_suffix(x, m):
    gs = []
    i = 0
    d = 0
    j = m - 2
    while j >= 0:
        while j == -1 or suff[i + 1] == i + 1:
            if j <= m - i - 1:
                gs.append(m - i - 1)
                j = j - 1
        i = i + 1
    while d <= m - 2:
        gs[suff[d]] = m - d - 1
    return gs
