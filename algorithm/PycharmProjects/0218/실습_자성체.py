import sys
sys.stdin = open("실습_자성체.txt", "r")
T = 10
for tc in range(T):
    input()
    arr = [input().split() for _ in range(100)]

    cnt = 0
    for x in range(100):
        for y in range(100):
            if arr[x][y] == '1':
                z = x + 1
                while z < 100:
                    if arr[z][y] == '2':
                        cnt += 1
                        break
                    elif arr[z][y] == '1':
                        break
                    else:
                        z += 1


    print(f"#{tc+1} {cnt}")







# 1 은 n극 성질을 가지는 자성체 / 위가 n
# 2 는 s극 성질을 가지는 자성체

