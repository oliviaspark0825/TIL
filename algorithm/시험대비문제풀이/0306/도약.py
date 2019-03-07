import sys
sys.stdin = open('도약.txt')
N = int(input())
point = []
cnt = 0
for i in range(N):
    point.append(int(input()))
point.sort()
for i in range(N-2): # 최소 2번은 더 해야하니까 끝의 2개 방은 아예 조건이 안되는거고
    for j in range(i+1,N-1): # 첫번째 점프 하고서도 점프 한번 더 하려면 적어도 마지막 방은 남겨놔야지?
        distance1 = point[j]-point[i]
        for k in range(j+1,N):# 두번째 점프
            distance2 = point[k] - point[j]
            if distance1 <= distance2 <= distance1*2:
                cnt += 1
            if distance2 > distance1*2: # 만약에 1 6 7 8 12 인데 12가 남아있는데 바로 거리가 7, 8 이면 break하면 안되지
                break
print(cnt)
