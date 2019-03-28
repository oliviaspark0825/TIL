
count = 0
N = 10
A = [0 for _ in range(N)]
total = 0
data =[int(x) for x in range(1,11)]

def printSet(n):
    global count

    sums = 0
    for i in range(N):
        if A[i] == 1:
            sums += data[i]
    if sums == 10:
        count += 1
        print('%d: ' % count, end="")
        for i in range(n):
            if A[i] == 1:
                print("%d" % data[i], end="")
        print()

def powerset(n, k, currentsum=0): #n: 원소의 갯수, k:현재 depth
    global total
    total += 1
    if k ==10:return
    if currentsum==10:  # basis part
        for i in range(10):
            if A[i]:
                print(data[i], end= " ")
        print()
    else: # inductive part
        if currentsum+data[k] <= 10:

            A[k] = 1 # k 번 요소 o
            powerset(n, k+1, currentsum+data[k]) # 다음요소 포함 여부 결정
            A[k] = 0 # k번 요소 x
            powerset(n, k+1, currentsum) # 다음요소 포함 여부 결정

powerset(N,0)
print("호출횟수 : {}".format(total))



def powerset(n, k, sum): #n: 원소의 갯수, k:현재 depth
    global total

    if sum > 10:return
    total += 1
    if n == k:  # basis part
        for i in range(10):
            if A[i]:
                print(data[i], end= " ")
        print()
    else: # inductive part
        if currentsum+data[k] <= 10:

            A[k] = 1 # k 번 요소 o
            powerset(n, k+1, currentsum+data[k]) # 다음요소 포함 여부 결정
            A[k] = 0 # k번 요소 x
            powerset(n, k+1, current