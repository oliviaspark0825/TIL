# 괄호의 짝을 검사하는 프로그램
s = list()
def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        print("stack is empty")
        return
    else:

        return s.pop(-1)


def isEmpty():
    if lens(s) == 0: return True
    else: Return False

def check_matching(data):
    for i in range(len(data)):
        if data[i] == "(":
            push(data[i])
        elif data[i] == ")":
            if isEmpty(): return False
            pop()
    #         오른쪽 만나면 pop 왼쪽 만나면 push 해주면 됨
    if not isEmpty(): return False
    else: return True

data = input()
print(check_matching(data))
