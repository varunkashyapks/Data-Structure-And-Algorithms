def search(x, y, m, n, algorithm):

    print "Preprocessing phase:"
    if algorithm == 'kmp':
        MP_next = kmp_borders(y, n)
    elif algorithm == 'mp':
        MP_next = mp_borders(y, n)
    print MP_next

    print "\nSearching phase:"
    i = 0
    j = 0
    while j < m:
        while (i == n) or (i >= 0 and x[j] != y[i]):
            i = MP_next[i]
        i = i + 1
        print i
        j = j + 1
        if i == n:
            print "x occurs in y at the position %d" % (j - 1)

y = 'aba'
x = 'abcacacabac'
search(x, y, len(x), len(y), 'mp')
