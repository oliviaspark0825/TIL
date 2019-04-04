import sys
sys.stdin = open('민석이.txt')
T = int(input())
for tc in range(T):
    N,K = list(map(int,input().split()))
    snum = list(map(int, input().split()))
    ans = [int(x) for x in range(1, N+1)]
    for i in snum:
        if i in ans:
            ans.remove(i)
    print("#{}".format(tc+1), end=" ")
    print(*ans)
