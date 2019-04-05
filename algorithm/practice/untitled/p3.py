import sys, time
sys.stdin = open('p3.txt')

st = time.time()
def solution(n):
    def permutation(n, k, total):
        nonlocal minN
        if n == k:
            minN = min(minN, total)
            return
        if total > minN:
            return
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            nxt = abs(robot[k][0]-snack[arr[k]][0]) + abs(robot[k][1]-snack[arr[k]][1])
            permutation(n, k+1, total+nxt)
            arr[i], arr[k] = arr[k], arr[i]
    arr = list(range(n))
    minN = 10*100
    permutation(n,0,0)
    return minN

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    snack = list(map(int, input().split()))
    robot = list(map(int, input().split()))
    snack = [(snack[i-1], snack[i]) for i in range(2*n) if i%2]
    robot = [(robot[i-1], robot[i]) for i in range(2*n) if i%2]
    print('#{}'.format(tc), solution(n))
print(time.time()-st)
# 로봇 인덱스 ==  로봇이 먹는 쿠키인덱스 라고 생각하자.
# 로봇이 출발하는 위치와 순서는 같지만, 로봇에 매칭되는 쿠키가 다르다고 생각하면
# 쿠키의 인덱스를 순열처럼 변경하면서 값을 찾을 수 있다는 말이 된다.