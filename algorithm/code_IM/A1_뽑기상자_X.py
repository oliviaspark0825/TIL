import sys
sys.stdin = open('뽑기상자.txt')
N = int(input())
p1 = list(map(int,input().split()))
p2 = list(map(int,input().split()))
# 일단, 정확히 N 이 뭘 뜻하는지 생각을 하고 변수를 정하기
b1 = [0]*(5+1)
b2 = [0]*(5+1)
for i in p1:
    b1[i] += 1
for j in p2:
    b2[j] += 1
cnt = 0
for s in range(1,6):
    if b1[s] or b2[s]:
        if (b1[s]+b2[s]) % 2 ==0:
            cnt += max(b1[s],b2[s]) - (b1[s]+b2[s])//2
        else:
            cnt = -1

print(cnt//2)