import sys
sys.stdin = open('성적표.txt')
T = int(input())
for tc in range(T):
    N,K = list(map(int,input().split()))
    score = list(map(int, input().split()))
    score.sort()
    tot = 0
    for i in range(K):
        tot += score[-i-1]

    print("#{} {}".format(tc+1, tot))

