import sys
sys.stdin = open('홀수만더하기.txt', 'r')
T = int(input())
for tc in range(T):
    data = list(map(int,input().split()))
    sum = 0
    for i in range(len(data)):
        if data[i] % 2:
            sum += data[i]
    print(f'#{tc+1} {sum}')




