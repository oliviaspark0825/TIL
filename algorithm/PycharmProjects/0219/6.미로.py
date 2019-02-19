# 미로
# 벽 만들기
def isWall(x, y):
    global N, arr
    if x<0 or x >= N: return True
    if y<0 or y>=N : return True
    return False






import sys
sys.stdin = open('미로.txt', 'r')
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
print(N)
print(arr)
    # 가장 마지막줄의 숫자 2를 찾아서 출발하기

