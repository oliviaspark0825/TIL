L=["Python", "YUNDAEHEE", "076923"]

file=open('textfile.txt','w')

file.write("START\n")

for i in range(3):
    file.write('%s\n' %L[i])

file.write("END")

file.close()


L=[]

file=open('textfile.txt','r')

while (1):
    line=file.readline()

    try:escape=line.index('\n')
    except:escape=len(line)
    
    if line:
        L.append(line[0:escape])
    else:
        break
    
file.close()

print(L)