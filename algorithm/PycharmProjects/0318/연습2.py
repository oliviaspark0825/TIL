def aToh(c):
    if c <= '9': return ord(c) - ord('0')
    else:
        return ord(c) - ord('A')+ 10

def makeT(x):
    for i in range(4):
        t.append(asc[x][i])

t = []
arr = '0F97A3'
for i in range(len(arr)):
    makeT(aToh)