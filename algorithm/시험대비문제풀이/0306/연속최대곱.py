import sys
sys.stdin = open('최대곱.txt')
N = int(input())
arr = []
for i in range(N):
    arr.append(float(input()))


total = 0.0
max = 0
#2중 루프로 구현
for i in range(N):
    for j in range(i,N): # 0번방꺼를 누적하기
        total *= arr[j] # 0 1 2 3 4
        if total > max:
            max = total
    total = 1.0 # 다시 돌아가면 초기화해야하니까
print("{:.3f}".format(max))
