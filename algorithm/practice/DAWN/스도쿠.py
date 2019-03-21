# flag 사용법을 배우다

import sys
sys.stdin = open('sudoku.txt')
T = int(input())
for tc in range(T):
    sudoku = [list(map(int,input().split())) for _ in range(9)]
    # 행으로 1부터 구까지 있는지 확인
    flag = 1
    stack = [s for s in range(1,10)]
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] in stack:
                stack.remove(sudoku[i][j])
        if stack:
            flag = 0
        else:
            stack = [s for s in range(1,10)]
    # # 열 1부터 9까지 있는지 확인
    for i in range(9):
        for j in range(9):
            if sudoku[j][i] in stack:
                stack.remove(sudoku[j][i])
        if stack:
            flag = 0
        else:
            stack = [s for s in range(1,10)]

    for x in range(0,7,3):
        for y in range(0,7,3):
            for f in range(3):
                for g in range(3):
                    if sudoku[x+f][y+g] in stack:
                        stack.remove(sudoku[x+f][y+g])
            if stack:
                flag = 0
            else:
                stack = [s for s in range(1, 10)]

    print('#{} {}'.format(tc+1, flag))

