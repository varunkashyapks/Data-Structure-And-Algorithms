def prefixes(x, m):
    pref = [m]
    g = 0
    f = 0
    i = 1
    while i < m:
        if i < g and pref[i - f] != g - i:
            pref.append(min(pref[i - f], g - i))
        else:
            g = max(g, i)
            f = i
            while g < m and x[g] == x[g - f]:
                g = g + 1
            pref.append(g - f)
        i = i + 1
    return pref
