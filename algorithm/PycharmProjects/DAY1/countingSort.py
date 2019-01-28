def CountingSort(A, B, C):
    for i in range(len(A)):
        C[A[i]] += 1 # 맨 처음에 1이 들어가고 인덱스 숫자를 증가시키기 # 몇번째까지 0으로 채워라

    for i in range(1, len(C)): # 누적시키기
        C[i] += C[i - 1]

    for i in range(len(B) -1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
# b가 0부터 시작해서 하나씩 빼줘야 하니까
# c도 자리 하나씩 줄어야해서 코드 하나 추가한거임

A = [1, 4, 5, 1, 2, 4, 5, 7, 9, 3]
B = [0] * len(A)
C = [0] * 10
CountingSort(A, B, C) # data 넘기기
print(B)

