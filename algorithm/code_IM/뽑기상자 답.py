import sys
sys.stdin = open('뽑기상자.txt')
N = int(input())
kim = list(map(int, input().split()))
park = list(map(int, input().split()))
K = [0] * 5
P = [0] * 5

for i in range(N):
    K[kim[i]-1] += 1
    P[park[i]-1] += 1
print(K, P)

cnt = 0
for i in range(5):
    if K[i] or P[i]:
        if (K[i] + P[i]) % 2 == 0:
            cnt += max(K[i], P[i]) - (K[i] + P[i]) // 2
        else:
            cnt = -1
print(cnt//2)