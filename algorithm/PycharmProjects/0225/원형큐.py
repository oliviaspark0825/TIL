#인덱스로 접근하는 연습
SIZE = 4
Q = [0]*SIZE
front, rear = 0, 0
#0으로 다 채움
def isFull():
    global front, rear
    return (rear+1) % len(Q) == front

def isEmpty():
    global front, rear
    return front == rear


def enQueue(item):
    global rear
    if isFull(): print("Queue full")
    else:
        rear = (rear +1) % len(Q)
        Q[rear] = item


def deQueue():
    global front
    if isEmpty(): print('Queue empty')
    else:
        front += (front + 1) % len(Q)
        return Q[front]


enQueue(1)
enQueue(2)
enQueue(3)
print(deQueue())
print(deQueue())
print(deQueue())
enQueue(4)
print(deQueue())
enQueue(5)
print(deQueue())
print(Q)