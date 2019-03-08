import sys
sys.stdin = open('스파이.txt')
N, S = input().split()
N = int(N)
node_no = 0
spy = []
stack= []
check = [0] * 2 # 괄호 < 와 > 의 갯수를 카운트
# < 가 나왔다가 바로 다음이  >이면 node 유지, > 닫히지 않고 <가 나타나면 node +1
for i in range(len(S)):
    if S[i] == '<':
        stack.append(S[i])
        node_no += 1
        check[0] += 1

    if S[i] == '>':
        stack.append(S[i])
        node_no -= 1
        check[1] += 1
    if S[i] != '<' and S[i]!='>':
    # if S[i].isdigit():
    #     for j in range(4):
    #         while not S[i+j].isdigit():
        if check[0] > check[1]: # < 갯수가 더 많으면 node_no 를 가져가야함
            spy.append([int(S[i]),node_no])
        elif check[0] == 0 and check[1] == 0:
            spy.append([int(S[i]),0])

for i in range(len(spy)):
    if spy[i][1] == N:
        print(spy[i][0], end=' ')
