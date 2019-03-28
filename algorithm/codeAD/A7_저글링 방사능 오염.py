'''
bfs
'''
def bfs():
    que = []
    dr =[-1,1, 0, 0]
    dc = [0, 0,-1, 1]

    que.append((sr,sc,3))
    grid[sr][sc] = 0 # 맵에 방문표시
    while que: # 큐가 있을 동안 반복 -- 없다 - 더이상 연결된 저글링이 없다

        r,c, time = que.pop(0)# 2 큐에서 데이터 꺼내기(현재위치)
        for i in range(4):# 3 4방향 탐색하면서 연결점
            nr = r + dr[i]
            nc = c + dc[i]
            if nr<0 or nr >=R or nc < 0 or nc>=C: continue
            if grid[nr][nc] == 1: # 저글링이면
                que.append((nr,nc,time+1))
                grid[nr][nc] = 0 # 방문표시하기
    return time # 큐가 빈 상태 (더이상 없앨 저글링 없을 때)




import sys
sys.stdin = open('저글링.txt')

# main ----------

C,R = list(map(int,input().split()))
grid = [list(map(int,input())) for _ in range(R)]
sc,sr = list(map(int,input().split()))
sc -= 1
sr -= 1
print(bfs())