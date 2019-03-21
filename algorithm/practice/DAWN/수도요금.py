import sys
sys.stdin = open('water.txt')
T = int(input())
for tc in range(T):
    # a 회사 liter 당 요금 p, b 회사 r 리터 이하는 q, 이후는 s
    P, Q, R, S, W = list(map(int,input().split()))
    # a 회사 요금

    if W == int(W):
        com_a = P * int(W)
    else:
        com_a = P * (int(W)+1)


    if R > W:
        com_b = Q
    else:
        if W == int(W):
            com_b = Q + (int(W)-R)*S
        else:
            com_b = Q + (int(W)-R+1)*S


    if com_a > com_b:
        print('#{} {}'.format(tc+1, com_b))
    else:
        print('#{} {}'.format(tc + 1, com_a))

