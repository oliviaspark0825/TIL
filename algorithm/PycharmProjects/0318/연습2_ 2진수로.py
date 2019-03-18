a = '0F97A3'
j = 0
result = ""
binaries = []
for i in a:

    if i in '0123456789':
        i = int(i)
    else:
        i = 10 + (ord(i)-ord("A"))
    for k in range(3,-1,-1):
        if (1<<k)&i:
            result += str(1)
            print(1, end="")
        else:
            result += str(0)
            print(0, end="")
        j += 1;
        if j == 7:
            j = 0;
            print(end=" ")
            binaries.append(result)
            result = ""
    binaries.append(result)
    print(binaries)



