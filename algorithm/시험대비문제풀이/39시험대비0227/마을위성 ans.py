import sys
sys.stdin = open('마을위성.txt')
N = int(input())
village = []
for i in range(N):
    village.append(list(map(int, input())))

for h in range(N):# 높이로 돌리기
    flag = 0
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            #사방이 모두 언덕이면 높이 1 증가, 내 자리는 언덕
            if village[i][j] >= h: # 내자리보다 높으면 ( 0 에서 시작할 수도 있으니까 1 이상의 높이가 하나라도 있으면,
                flag = 1  # 높이 이상의 언덕이 존재하면 1로 바꾸기
                if village[i-1][j] > h and village[i+1][j] > h and village[i][j-1] > h and village[i][j+1] > h:
                    village[i][j] += 1 # 나에다가 1만 더하면 되니까, 내 기준으로 순차탐색이라서 2이상 크기는 존재x
    if flag ==0: break
print(h-1)
#모두가 평지면 1부터 높이를 올리는거 시작하면 망함
