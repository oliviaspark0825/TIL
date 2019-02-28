#순차탐색 - 행으로 하나씩 탐색하기

import sys
sys.stdin = open('마을위성.txt')
N = int(input())
village = []
for i in range(N):
    village.append(list(map(int, input())))

empty = []
for i in range(1,N-1):
    for j in range(1,N-1):
        if village[i][j]: # 일단 언덕일 때
            if village[i-1][j] == 0 or village[i+1][j] == 0 or village[i][j-1] == 0 or village[i][j+1]==0:
                village[i][j] = 1 # 하나라도 0 이 있으면 바뀌지 않음
                #주변이 모두 0이 아니고 가장자리가 아니면
            if village[i-1][j] !=0 and village[i+1][j] != 0 and village[i][j-1] != 0 and village[i][j+1] != 0:
                empty.append(village[i-1][j])
                empty.append(village[i+1][j])
                empty.append(village[i][j-1])
                empty.append(village[i][j+1])
                empty.sort()
                # 처음 시작이 1이니까 어차피 다 주변도 1이라서 min을 찾ㅇ르 필요가 없음
                village[i][j] = empty[0] + 1
max = -1
for i in range(N):
    for j in range(N):
        if village[i][j] > max:
            max = village[i][j]
print(max)
