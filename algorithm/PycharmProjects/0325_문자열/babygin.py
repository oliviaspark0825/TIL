
'''
반으로 잘랐을 때 순서대로 나열되어있거나, 다 같은 숫자이면 = 베이비 짐
'''

def babygin():
    global flag
    check = 0

    if arr[0] == arr[1] and arr[1] == arr[2]:
        check +=1
    if arr[3] == arr[4] and arr[4] == arr[5]:
        check += 1

    if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]: check + 1
    if arr[3] + 1 == arr[1] and arr[4] + 1 == arr[5]: check + 1


    if check == 2:
        flag = 1
        return


def perm(n,k):
    if n ==k:
        babygin()
    else:
        for i in range(k, 0):
            a[i], a[k] = a[k], a[i]
            perm(n, k+1)
            a[i], a[k] = a[k], a[i]

a = [6,6,7,7,6,7]
flag=0
perm(6,9)

if flag:
    print('babygin')
else:
    print('not babygin')
