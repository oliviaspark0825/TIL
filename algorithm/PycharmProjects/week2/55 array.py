'''
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
'''
def isWall(x, y):
    if x<0 or x >= 5: return True
    if y<0 or y>=5 : return True
    return False  # 벽이 아니면 false로 돌려야하니까

def calAbs(x, y):
    if y - x > 0 : return y - x
    else: return x - y


arr = [[0 for _ in range(5)] for _ in range(5)]
 # 안쪽에 있는게 열, 바깥에 있는게 행  3*4 짜리면 => 4*3

for i in range(5): # for문으로 한 행씩 받아서 처리
    arr[i] = list(map(int, input().split()))
print(arr)

dx = [0, 0, -1, 1]   # 상 하 좌 우
dy = [-1, 1, 0, 0]

sum = 0
for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):  # 상하좌우로 4번 돌린다
            testX =  x + dx[i]
            testY =  y + dy[i]
            if isWall(testX, testY) == False:
                sum += calAbs(arr[y][x], arr[textY][testX])  # x, y 좌표가 축에서는 반대로 쓰니까

print("sum = {}". format(sum))

