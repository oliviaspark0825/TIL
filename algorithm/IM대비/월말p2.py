import sys
sys.stdin = open('p2.txt')
T = int(input())
for tc in range(1):
     N, M = list(map(int,input().split()))
     arr = [list(map(int,input().split())) for _ in range(N)]
     maxx =0

     for i in range(1, N):
         for j in range(0,M-1):
             for k in range(j+1, M):
                 L = [0]*6
                 for a in range(0,i):
                     for b in range(0,j):
                         L[0] += arr[a][b]

                     for b in range(j,k):
                         L[1] += arr[a][b]

                     for b in range(k,M):
                         L[2] += arr[a][b]

                 for a in range(i,N):
                     for b in range(0,j):
                         L[3] += arr[a][b]
                     for b in range(j, k):
                         L[4] += arr[a][b]
                     for b in range(k, M):
                         L[5] += arr[a][b]


                 for c in range(0, 4):
                     for d in range(c+1,5):
                         for e in range(d+1,6):
                             if abs(L[c] - L[d]) + abs(L[e]-L[c]) + abs(L[d] - L[e]) > maxx:
                                 print(abs(L[c] - L[d]) + abs(L[e]-L[c]) + abs(L[d] - L[e]))
                                 maxx = abs(L[c] - L[d]) + abs(L[c]-L[e]) + abs(L[d] - L[e])


     print("#{} {}".format(tc+1,maxx))

