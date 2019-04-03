import sys
sys.stdin = open('책꽂이.txt')
######### 소의 키를 더하는건 순서가 필요 없으니까, 조합
# 그런데 n개 고르는 조합까지 다 시도해보아서
N = int(input())
arr =[]
for i in range(N):
    arr.append(list(map(int,input().split())))