# plate = input()
# import sys
# sys.stdin = open('그릇.txt', 'r')
# T = int(input())
#
# for tc in range(T):
    plate = input()
    point = [5,10]
    bottom = plate[0]
    sum = 10
    for i in range(0, len(plate)-1):
        # ( )
        if plate[i+1] != plate [i]:
            sum += point[1]
        # (( , ))
        else:
            sum += point[0]
    print(sum)
