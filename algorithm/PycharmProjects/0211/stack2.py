#1 스택 구현
size = 100
stack = [0] * size
top = -1 # 값 형은 꼭 넘겨주어야함 - 그래서 global 한거임
def push(item):
    global top
    if top > size -1:
        return
    else:
        top += 1
        stack[top] = item

def pop():
    global top
    if top == -1:
        print("stack is Empty")
        return 0;
    else:
        result = stack[top] # top 에 있는거를 result에다가 주고, 하나 감소시킴
        top -= 1
        return result

# 나중에 들어간 것이 먼저 나오게 되니까
push(1)
push(3)
push(5)
print(pop())
print(pop())
print(pop())
