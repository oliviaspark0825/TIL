# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
# 정수가 들어오는데 잘라서 쓰려니까 처음에 0 으로 시작하면 0번째 카드는 셀 수가 없음 -> 그래서 걍 STR으로 받음 == LIST 형태로 저장이 됨 / 하나씩 잘라서 INT로 바꾸고, COUNTING -> MAX 값을 구해야하는데 1) 번호 2) 몇장인지 두개를 다 구해야 함
import sys

sys.stdin = open("numberlist.txt", "r")

T = int(input())  # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())  # 주어지는 정수 갯수 받고
    card = input() # 문자열 자체를 받아오면 지가 알아서 LIST 형태 방에 하나씩 들어가 있음
    count = [0]* 10 # 갯수를 셀 것을 만들어놓고
    for i in range(len(card)):
        count[int(card[i])] += 1  # 카드 123456 에서 인덱스로 i 하면 card[1]의 값 나오고 - 그거를 count [2] 이런식으로 해서 숫자 1번 방의 숫자를 count 하면 됨
    max_index = 0 # index
    max_value = 0 # 얘는 값
    for i in range(len(count)):
        if count[i] >= max_value: # 만약 숫자 3 과 5 가 갯수가 같으면 더 큰거로 넘어가야하니까, value 가 같아도 index를 바꾸기 위해서는 = 이 함께 있어야 함
            max_value = count[i]
            max_index = i
    print('#{} {} {}'.format( test_case, max_index, max_value))

