import sys
sys.stdin = open('같은놈.txt', 'r')
T = int(input())
for tc in range(T):
    data = list(map(int,input().split()))
    print(data)
    ans = ''
    for d in range(1, len(data)):
        if data[d] > data[d-1]:
            ans = '<'
        elif data[d] == data[d-1]:
            ans = '='
        else:
            ans = '>'
    print(f'#{tc + 1} {ans}')
