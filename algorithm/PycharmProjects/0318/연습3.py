a = '0F97A3'
j = 0
result = ""
binaries = []
for i in a:

    if i in '0123456789':
        i = int(i)
    else:
        i = 10 + (ord(i)-ord("A"))