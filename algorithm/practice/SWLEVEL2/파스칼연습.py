import sys
sys.stdin = open('파스칼.txt')

T = int(input())

def Printarr():
    global N
    L = [1]
    for i in range(N):
        if i < 2:
            for j in range(i+1):
                print(L[j], end=" ")
                L.append(L[j])
        else:
            x = len(L)
            for j in range(i+1):
                if j == 0 or j == i:
                    print(1, end=" ")
                    L.append(1)
                else:
                    print(L[j-1]+L[j], end=" ")
                    L.append(L[j-1]+L[j])
            for j in range(x):
                L.pop(0)
        print()

for n in range(1, T+1):
    N = int(input())
    print("#{0}".format(n))
    Printarr()