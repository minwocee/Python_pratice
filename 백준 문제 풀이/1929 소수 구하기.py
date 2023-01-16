# https://www.acmicpc.net/problem/1929

# 딱봐도 에라토스테네스의 체 활용하는 문제인것 같다.

import sys
start , end = map(int, sys.stdin.readline().split())

dp=[False,False] + [True]*(end-1)

sosu=[]

for i in range(end+1):
    if dp[i]:
        sosu.append(i)
        for k in range(2*i,end+1,i):
            dp[k]=False

for k in sosu:
    if start<=k<=end:
        print(k)