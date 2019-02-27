import sys
sys.stdin = open('색종이초.txt')
N = int(input())
for i in range(N):
    paper = list(map(int,input().split()))
print(paper)
print(paper[0])
#겹치는 부분의 좌표 찾기
overlap_x, overlap_y = 0,0
for i in range(N-1): # 1: 3,7 2: 5,2
    print(paper[i+1][0])
    # if paper[i+1][0] - paper[i][0] <10:
    #     overlap_x = paper[i][0] - paper[i+1][0]
    # if paper[i][1] - paper[i+1][1]

