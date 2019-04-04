import sys
sys.stdin = open('농작물.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    tot = 0
    mid = N // 2
    start = mid
    end = mid

    # 한줄씩 증가할때마다 왼쪽 하나, 오른쪽 하나 추가
    # 정가운데
    # 확장하기 전까지
    for i in range(mid+1):
        for j in range(start,end+1,1):
            tot += arr[i][j]
        start -= 1
        end += 1

    for i in range(mid+1, N):
        for j in range(start+2, end-1, 1):
            tot += arr[i][j]
        start += 1
        end -= 1

    print("#{} {}".format(tc+1,tot))