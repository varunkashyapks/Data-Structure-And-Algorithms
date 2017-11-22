import sys
 
SHINGLE_SIZE = 5
 
def get_shingles(f, size):
    shingles = set()
    buf = f.read() # read entire file
    for i in range(0, len(buf)-size+1):
        yield buf[i:i+size]
 
def jaccard(set1, set2):
    x = len(set1.intersection(set2))
    y = len(set1.union(set2))
    return x / float(y)
 
file1 = sys.argv[1]
file2 = sys.argv[2]
 
with open(file1) as f1, open(file2) as f2:
    shingles1 = set(get_shingles(f1, size=SHINGLE_SIZE))
    shingles2 = set(get_shingles(f2, size=SHINGLE_SIZE))
 
print(jaccard(shingles1, shingles2), file1, file2)