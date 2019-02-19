import sys
sys.stdin = open('평균값.txt', 'r')
T = int(input())
for tc in range(T):
    N = 10
    data = list(map(int, input().split()))
    sum = 0
    ans = 0
    for i in range(len(data)):
        sum += data[i]
        ans = sum/len(data)
        ans = round(ans)

    print(f'{tc+1} {ans}')



