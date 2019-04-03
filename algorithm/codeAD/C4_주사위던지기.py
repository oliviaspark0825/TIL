def DFS(no, start):
    if no>N:
        print
        return

    for i in range(start,7):
        rec[no] = i
        DFS(no+1, i+1) # i 를 스타트로 잡으면 2부터 시작
