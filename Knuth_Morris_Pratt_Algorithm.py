# Knuth-Morris-Pratt Algorithm
def kmp_borders(x, m):
    i = 0
    j = -1
    kmpNext = [j]
    for i in range(0, m - 1):
        while j >= 0 and x[i] != x[j]:
            j = kmpNext[j]
        i += 1
        j += 1
        if x[i] == x[j]:
            kmpNext.append(kmpNext[j])
        else:
            kmpNext.append(j)
    kmpNext.append(j)
    return kmpNext
 #print kmp_borders(x, len(x))
