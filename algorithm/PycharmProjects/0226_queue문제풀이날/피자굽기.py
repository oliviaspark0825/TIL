import sys
sys.stdin = open('피자굽기.txt', 'r')
T = int(input())
for tc in range(1):
    N, M = list(map(int, input().split())) # N: 화덕크기 M: 피자 갯수
    c = list(map(int, input().split()))
    # 피자에다가 번호를 붙여주기
    idx_pizza = []
    for i in range(M):
        idx_pizza.append([i,c[i]])
    # 화덕크기만큼 피자를 넣어주기
    queue=[]
    for j in range(N):
        queue.append(idx_pizza[j])
    while queue:
        # 한개씩 확인하자
        pick = queue.pop(0)
        print(pick)
        if pick[1]//2 != 0:
            pick = [pick[0], pick[1]//2]
            # 피자 치즈를 반으로 줄이고, queue의 맨 끝에다가 다시 저 피자를 넣기
            queue.append(pick)
        elif




