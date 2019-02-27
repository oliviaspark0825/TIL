import sys
sys.stdin = open('색종이배치.txt')
# for i in range(2):
r1, c1, len1, len1 = map(int,input().split())
r2, c2, len2, len2 = map(int, input().split())
if r1+len1 == r2 and c1+len1 == c2:
    print('1')
if r1+len1 == r2 and c1+len1 > c2:
    print('2')
if r1+len1 > r2 and c1+len1 > c2:
    print('3')
if r1+len1 < r2 and c1+len1 < c2:
    print('4')

#첫번째 색종이를 그냥 배열에다가 마킹을 해놓고 시작
#겹친 자리를 2로 만들어주면 - 3
# 채우려했는데, 1이 이미 있으면 3이구나
# 1이 아무것도 없으면 4
# tpye 1, 2 는 가장자리의 문제
# 색종이 자리 마킹하는것처럼 주변을 마킹하기 - 2로  1채운거 제외하고
#1 범위내에서 2가 하나만 있으면
#2 범위내에서 2가 2개 이상이기만 하면