
#여러줄쓰기

# f = open("several.txt","w")
# for i in range(6):
#     line = (f'{i}번째 줄입니다.\t')
#     f.write(line)
# f.close()



with open("several.txt","w", encoding='utf-8') as f:
    for i in range(6):
        line = (f'{i}번 째 줄입니다.\t')
        f.writelines(line)


