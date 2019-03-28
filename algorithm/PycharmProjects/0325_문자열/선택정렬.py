# 반복을 이용한 선택정렬
'''
def selectionSort(A):
    n = len(A)
    for i in range(0, n-1):
        min = 1
        for j in range(i+1, n):

            if A[j] < A[min]:
                min = j

        temp = A[min]
        A[min] = A[i]
        
'''


def recselectionsort(ary, s,e):
    mini = s

    if s == e: return
    for j in range(s+1, e, 1):
        if ary[j] < ary[mini]:
            mini = j

    ary[s], ary[mini] = ary[mini], ary[s]

    recselectionsort(ary, s+1, e);


def selectionsort(ary):
    for i in range(i+1, )

