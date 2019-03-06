import sys
sys.stdin = open('회문.txt')
for tc in range(10):
    n = int(input())
    arr = [list(input()) for _ in range(8)]
    print(arr)