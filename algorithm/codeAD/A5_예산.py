'''
이진탐색, 인덱스
'''
def binSearch(s,e,mid):
    while s<=e:
        m = (s+e)//2
        # data가 mid번째값이면 mid위치 + 1리턴
        if data == mid : return m +1
        # data가 mid번째값보다 크면 오른쪽영역 재탐색
        elif data>arr[m] :
            s = m+1
        # data가 mid번째값보다 작으면 왼쪽영역 재탐색
        else : e = m-1



import sys
sys.stdin = open('예산.txt')
N = int(input())
data = list(map(int,input().split()))
M = int(input())
data.sort()
start = 1
end = data[-1]
mid = (start + end)//2

binSearch(0,N-1,mid)

