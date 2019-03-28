#{1,2,3} 모든 부분 집합 출력하기
'''
상태공간 트리
'''
count = 0
N = 3
A = [0 for _ in range(N)]
data = [1, 2, 3]

def printSet(n):
    global count
    count += 1
    print("%d" %(count), end=" : ") # 생성되는 부분의 갯수 출력
    for i in range(n): # 각 부분 배열의 원소 출력
        if A[i] == 1: # A[i]가 1이면 포함된 거니까 출력
            print("%d " % data[i], end="")
    print()


def powerset(n, k): #n: 원소의 갯수, k:현재 depth
    if n==k:  # basis part
        printSet(n) # 다 되었으니 출력을하던, 부분집합을 만들던 하라
    else: # inductive part
        A[k] = 1 # k 번 요소 o
        powerset(n, k+1) # 다음요소 포함 여부 결정
        A[k] = 0 # k번 요소 x
        powerset(n, k+1) # 다음요소 포함 여부 결정

powerset(N,0)