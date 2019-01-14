import sys
sys.stdin = open("view_input.txt")

# def view(data):
T = 10 # 10번 돌아라
for tc in range(T):
    ans = 0 # case 마다 초기화
    N = int(input())  # 문자열을 정수로 받고
    data = list(map(int, input().split())) # input 받은 문자열을 공백으로 잘라서 숫자로 바꾸고 리스트에 넣어라
    for i in range(2, len(data)-2): # data에 담긴 숫자 안에서
        if data[i] > max(data[i - 1], data[i - 2], data[i + 1], data[i + 2]):
                ans += data[i] - max(data[i - 1], data[i - 2], data[i + 1], data[i + 2])


    print("#{} {}".format(tc+1, ans))

