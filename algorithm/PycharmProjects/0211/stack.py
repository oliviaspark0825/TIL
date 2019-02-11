def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        print("stack is empty")
        return
    else:
        return s.pop(-1) # 마지막 값을 출력해라
# length가 제로면 길이가 없는건 비어있는거니까
s=[]

push(1)
push(7)
print(pop())
print(pop())
#데이터는 지워짐 새로 push 되면 그 값이 추가됨
