def DFS(n):
    arr = [0] * (n+1)
    if n == 2 or n == 1 : return 1
    arr[n] = DFS(n-1) + DFS(n-2)
    return arr[n]
    # 가지치기
    # 이전에 값을 구했는지 확인, 있으면 값을 저 if n==2 로 보내주기
    if arr[n]: return arr[n]



n = int(input())
print(DFS(n))
