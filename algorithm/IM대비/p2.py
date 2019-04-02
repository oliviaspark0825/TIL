import sys
sys.stdin = open('p2.txt')


T = int(input())

for n in range(1):
    X, Y = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(X)]
    C = [0] * 3
    maxN = 0
    for i in range(1, Y-1):
        for j in range(i+1, Y):
            for k in range(1, X):
                L = [0] * 6
                for l in range(0, i):
                    for o in range(0, k):
                        L[0] += arr[o][l]
                    for o in range(k, X):
                        L[3] += arr[o][l]

                for l in range(i, j):
                    for o in range(0, k):
                        L[1] += arr[o][l]
                    for o in range(k, X):
                        L[4] += arr[o][l]

                for l in range(j, Y):
                    for o in range(0, k):
                        L[2] += arr[o][l]
                    for o in range(k, X):
                        L[5] += arr[o][l]


                for l in range(6-2):
                    for o in range(l+1, 6-1):
                        for p in range(o+1, 6):
                            if abs(L[l] - L[o]) + abs(L[o] - L[p]) + abs(L[p] - L[l]) > maxN:
                                print(abs(L[l] - L[o]) + abs(L[o] - L[p]) + abs(L[p] - L[l]))
                                maxN = abs(L[l] - L[o]) + abs(L[o] - L[p]) + abs(L[p] - L[l])

    print("#{0} {1}".format(n, maxN))




