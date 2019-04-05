import sys
sys.stdin = open('p1.txt')

def finder(sang, target):
    queue = [sang]
    time = 0
    while queue:
        time += 1
        for _ in range(len(queue)):
            i,j = queue.pop(0)
            for d in range(8):
                x = i+direction[d][0]
                y = j+direction[d][1]
                if 0 <= x < N and 0 <= y < N:
                    if (x,y) == target:
                        return time
                    if (x,y) not in queue:
                        queue += [(x,y)]
    return time

direction = [(-2,-3), (-3,-2), (-3,2), (-2,3), (2,3), (3,2), (3,-2), (2,-3)]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    x,y,tx,ty = map(int, input().split())
    print('#{}'.format(tc), finder((x,y), (tx,ty)))