import sys
sys.stdin = open('view.txt')
N = int(input())
for tc in range(N):
    data = list(map(int,input().split()))
    cnt = 0
    for i in range(2,N-2):
        if data[i-1] < data[i] and data[i-2]<data[i] and data[i] > data[i+1] and data[i] > data[i+2]:
            cnt +=1

    print("#{} {}".format(tc+1, cnt))