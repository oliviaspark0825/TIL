import sys
sys.stdin = open('.txt', 'r')

def find():
    s = []
    for i in range(len(code)):
        if code[i] == '+' or code[i] == '-' or code[i] == '/' or code == '*':
            #stack에 숫자가 2개 이상이 있어야 하니까
            if len(s) >= 2:
                op2 =