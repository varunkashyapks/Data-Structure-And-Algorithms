# bracket balancing
lefts = '{[('
rights = '}])'
closes = { a:b for a,b in zip(rights,lefts)}

def valid(s):
    stack = []
    for c in s:
        if c in lefts:
            stack.append(c)
        elif c in rights:
            if not stack or stack.pop() != closes[c]:
                return False
    return not stack  # stack must be empty at the end

t = int(raw_input().strip())
for a0 in xrange(t):    
    s = raw_input().strip()    
    if valid(s):
        print 'YES'
    else:
        print 'NO'