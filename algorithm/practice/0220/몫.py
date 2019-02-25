
import sys
sys.stdin = open('몫.txt', 'r')
T = int(input())
for tc in range(T):
    n1,n2 = list(map(int,input().split()))
    mok = n1//n2
    namoeji = n1 % n2

    print(f'#{tc+1} {mok} {namoeji}')