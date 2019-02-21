import sys
sys.stdin = open('중간값.txt', 'r')
N = int(input())
for tc in range(N):
    data = list(map(int, input().split()))
    print(data)
    new = []
    for i in range(len(data)):
        min = data[0]
        if data[i] < min:
            new.append(data[i])
    print(new)



