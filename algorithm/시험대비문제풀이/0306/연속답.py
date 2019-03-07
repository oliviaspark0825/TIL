import sys
sys.stdin = open('최대곱.txt')
N = int(input())
arr = []
for i in range(N):
    arr.append(float(input()))


mul = 1.0
max = 0.0
#2중 루프로 구현
# for i in range(N):
#     mul = 1.0
#     for j in range(i,N): # 0번방꺼를 누적하기
#         mul *= arr[j] # 0 1 2 3 4
#         if mul > max:
#             max = mul
# print('%.3f'% max)
#1중으로 구현하려면
mul = 1.0
max = 0.0
for i in range(N):
    mul *= arr[i]
    if arr[i]>mul:
        mul = arr[i]
    if mul > max:
        max = mul
print('%.3f'% max)