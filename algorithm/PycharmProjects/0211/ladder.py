import sys
sys.stdin = open("ladder_input.txt")
T = 10
SIZE = 100
for tc in range(T):
    data = [[0 for i in range(100)] for j in range(100)]
    data = list(map(int, input().split()))

    while x < 100 and y < 100:
        if data[x][y] == 1 and data[x][y-1] == 1:
            x -= 1
        elif data[x][y] == 1 and data[x][y-1] != 1:




    # for x in range(100):
    #     for y in range(100):
    #         ans = 0
    #         # 다음 칸이 1이 아닐 경우는 아래로 이동
    #         if data[x][y] == 1 and data[x][y+1] != 1:
    #             ans = x
    #             x = x
    #             y += 1
    #         # 다음 칸도 1일 경우는 옆으로 이동
    #         elif data[x][y] == 1 and data[x][y+1] == 1:
    #             x += 1
    #             y = y
    # if data[x][y] == 2:
    #     return ans



# 다시 못돌아가게 하려면, 이미 지나온 1은 값을 바꿔야 함










# print("{} {}".format())