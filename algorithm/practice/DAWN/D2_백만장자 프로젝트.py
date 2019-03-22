import sys
sys.stdin = open('백만장자.txt')
T = int(input())
for tc in range(3):
    N = int(input())
    days = list(map(int,input().split()))
    stack = []
    total = 0
    biggy = 0
    # 다음거보다 작거나 같으면 일단 스택에 값을 쌓기
    for i in range(len(days)-1):
        while i<N-1 and days[i] < days[i+1]:
            stack.append(days[i])
            biggy = days[i+1]
            i+=1
        # 다 쌓았으면 계산을 해야지
        for s in range(len(stack)):
            total += (biggy - stack[s])
        stack = []


    print('#{} {}'.format(tc+1, total))

    biggest = max(days)
    for i in range(N):