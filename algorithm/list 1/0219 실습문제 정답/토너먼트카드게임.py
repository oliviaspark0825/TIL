
def find(l, r):
    if l==r:
        return l
    else:
        # 위로 보낸다는거
        #이긴 애가 올라가면 r1, r2로 받아짐
        r1 = find(l, (l+r)//2)
        r2 = find((l+r)//2+1, r)
        #같으면 번호가 작은 쪽을 리턴하라
        if card[r1]==card[r2]:
            return r1
        else:
            if card[r1]==1 and card[r2]==2:             # 가위 vs 바위
                return r2
            elif card[r1]==1 and card[r2]==3:           # 가위 vs 보
                return r1
            elif card[r1]==2 and card[r2]==1:           # 바위 vs 가위
                return r1
            elif card[r1]==2 and card[r2]==3:           # 바위 vs 보
                return r2
            elif card[r1]==3 and card[r2]==1:           # 보 vs 가위
                return r2
            elif card[r1]==3 and card[r2]==2:           # 보 vs 바위
                return r1

import sys
sys.stdin = open('토너먼트카드게임_input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card = [0] + list(map(int, input().split()))           # 인덱스 1번부터 저장 #0번 안쓰려고
    print('#{} {}'.format(tc, find(1, N)))
