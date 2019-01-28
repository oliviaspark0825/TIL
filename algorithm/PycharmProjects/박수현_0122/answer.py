

#겹쳐진 칸수 카운팅
for i in range(N):
    for j in range(N):
        if(data[i][j] == 3): count += 1





#부분집합
sys.stdin = open("6.부분집합합.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    ans = 0

    # 부분집합 만들기
    for i in range(1 << len(n)):
        sum = 0
        cnt= 0
#비트연산자로 피연산자를 이진법으로 바꾸기
        for j in range(len(n+1)):
            if i & (1 << j):
                sum += A[j] # 1,2,3을 더하기
                sub_A.append(A[j])
        # print(sub_A)
        # print(sum)
        if sum == K and len(sub_A) == N:
            count +=1


    print(
        for  in range(0, 5):
            print(v[j], end=' ')
    )