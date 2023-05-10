#https://www.acmicpc.net/problem/16204
import sys

N,M,K=map(int, sys.stdin.readline().split())


front=[True]*M + [False]*(N-M)
back=[True]*K + [False]*(N-K)


cnt=0
for x,y in zip(front, back):

    if x==y:
        cnt+=1

print(cnt)