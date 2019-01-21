# 행우선
arr = [[0, 1, 2, 3],
       [4, 5, 6, 7],
       [8, 9, 10,11]]
# i : 행의 좌표, n = len(arr)
# j : 열의 좌표, m = len(arr[0])

for i in range(len(arr)): # 3*4 길이이면 i는 3번 돌겠지
    for j in range(len(arr[i])):  # 0 번째는 4개 , 1번째에 4개 들어가고 2 째 줄에 4게
        print(arr[i][j], end=" ")
    print()
print()

# 열우선
for j in range(len(arr[0])): # 첫 줄 길이가 4개니까 4번 돌테고
    for i in range(len(arr)): # 행 갯수가 3개니까 4개씩 3번 돌겠지
        print(arr[i][j], end=" ") # 줄바꿈 안하려고
    print()
print()

#지그재그
n = len(arr)
m = len(arr[0])
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j] + (m -1 -2*j)) * (i*2)



