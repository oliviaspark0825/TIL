def check_not(start, end):
    #배수 개념, 마지막 수의 제곱근까지
    for i in range(start,end+1):
        # if i*i > end: # 초과하면 제외하겠다 10 * 10 넘어가면 버리겠다
        #     break
        if check_table: continue
        for j in range(i*2, end+1, i): # 이 다음 4부터 시작해서 끝까지 배수 개념으로 2, 4, 6
            check_table[j] = 1



import sys
sys.stdin = open('소수의갯수.txt')
start, end = list(map(int,input().split()))
# 배수개념이라 루트 씌운 거까지만 나누어보겠다
check_table = [1]*start + [0] * (end-start)
cnt= 0
max = 0
min = 999
check_not(start, end)
print(check_table)
# 체크가 끝난 후 소수 갯수, 최대, 최소 찾기
for i in range(end):
    if check_table[i] == 0:
        cnt += 1
        if i > max:
            max = i
        if i < min:
            min = i

print(cnt,max+min)

