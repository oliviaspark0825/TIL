import sys
sys.stdin = open('view.txt')
T = 10
for tc in range(T):
    N = int(input())
    data = list(map(int,input().split()))
    cnt = 0

    for i in range(2,N-2):
        L = []
        if data[i-1] < data[i] and data[i-2]<data[i] and data[i] > data[i+1] and data[i] > data[i+2]:
            L.append(data[i-1])
            L.append(data[i - 2])
            L.append(data[i +1])
            L.append(data[i +2])
            L.sort()
            cnt += data[i] - L[-1]

    print("#{} {}".format(tc+1, cnt))
