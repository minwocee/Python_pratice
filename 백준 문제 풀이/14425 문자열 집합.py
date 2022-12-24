# https://www.acmicpc.net/problem/14425

# 문자열개수 N   (확인정답지)
# 문자열개수 M     (확인해야하는곳)

# in 키워드 사용하면 좋을것같은데

import sys

N,M=map(int,sys.stdin.readline().split())

N_table=[str(sys.stdin.readline().strip()) for _ in range(N)]

counter=0
for i in range(M):
    word = str(sys.stdin.readline().strip())

    # 집합 s에 문자열이 포함되어 있으면 카운트
    if word in N_table:
        counter+=1

print(counter)

""" 아래의 방식이 더 효율적이긴하다 굳이 배열을 만들지 않아서 메모리 낭비가 생기지 않는다. """
import sys


n, m = map(int, sys.stdin.readline().split())
s = [str(sys.stdin.readline()) for _ in range(n)] # 집합 s
cnt = 0

# 반복문을 통해 m개의 문자열을 확인
for i in range(m):
    word = str(sys.stdin.readline())

    # 집합 s에 문자열이 포함되어 있으면 카운트
    if word in s:
        cnt += 1

print(cnt)














