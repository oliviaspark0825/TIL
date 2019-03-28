def Qsort(s, e):
    if s >= e: return
    p, t = e, s
    for i in range(s, e):
        if arr[i] < arr[p]:
            arr[i], arr[t] = arr[t], arr[i]
            t += 1
    arr[p] , arr[t] = arr[t], arr[p]
    Qsort(s, t-1)
    Qsort(t+1, e)

def Msort(s,e):
    if s >= e:
        return
    m = (s+e)//2
    Msort(s, m)
    Msort(m+1, e)
    L,R,T = s, m+1, s
    while L <= m and R <= e:
        if arr[L] < arr[R]:
            temp[T] = arr[L]
            T += 1
            L += 1
        else:
            temp[T] = arr[R]
            T += 1
            R += 1
    while L <= m:
        temp[T] = arr[L]
        T += 1
        L += 1
    while R <= e:
        temp[T] = arr[R]
        T += 1
        R += 1
    for i in range(s, e+1):
        arr[i] = temp[i]



N = int(input())
arr = [int(input()) for _ in range(N)]
temp = [0] * N
Msort(0, N-1)