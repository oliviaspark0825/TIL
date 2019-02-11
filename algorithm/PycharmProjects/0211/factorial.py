def fact(s):
    if s == 1:
        return 1
    else:
        return s * fact(s-1)

print(fact(4))


def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(4))


# 양갈래로 빠지지 않게 하기 위해서 memoization 중복해서 호출하지 않겠다
# 테이블을 만들어서 결과를 저장하고, 다음번에는 테이블에서 가져와서 결과를 호출한다
def fibo(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]

memo = [0 , 1]
print(fibo(100))


#점화식을 적용한 피보나치 수열 DP
#반복적인 과정을
#재귀를 쓰지 않으니까 1000도 가능함

def fibo2(n):
    f = [0, 1]

    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

print(fibo2(1000))


# DFS 알고리즘 - 재귀
# DFS_Recursive(G, v)
#처음에는 방문 안했다고 해서 다 0으로 채우고, 재귀는 스택이 필요 없음




