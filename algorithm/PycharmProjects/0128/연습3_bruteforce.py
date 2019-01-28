# find 구현
p = "is"
t = "this is a book. this is a computer"

m = len(p)
n = len(t)

def bruteForce(p, t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    check_list = []
    while j < m and i < n:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1 # 다음 인덱스 확인해야하니까 하나씩 증가
        j = j + 1
    if j == m:
        return i - m # 검색 성공
    else: retrun -1 # 검색 실패

print(bruteForce(p,t))


#여러번
def bruteForce(p, t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    start = 0
    while j < m and i < n:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1 # 다음 인덱스 확인해야하니까 하나씩 증가
        j = j + 1
    if j == m:
        return i - m # 검색 성공
    else: retrun -1 # 검색 실패

print(bruteForce(p,t))





def bruteForce2(test, pattern):
    for i in range(len(text) - len(pattern) + 1):
        cnt = 0
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                break
            else: nt += 1
        if(cnt >= len(pattern)) : return i

start = 0
while True:
    start = bruteForce(text, pattern, start)
    print(start)
    start = start + len(pattern)
    if start > lent(Text) - len(pattern) + 1)



def bruteForce(text, pattern, start):
  i, j = start, 0
  while j < len(pattern) and i < len(text):
      if text[i] != pattern[j]:
          i = i -j
          j = -1
      i = i + 1
      j = j + 1