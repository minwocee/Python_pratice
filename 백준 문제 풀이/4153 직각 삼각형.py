# https://www.acmicpc.net/problem/4153
"""
피타고라스 정리를 활용해 직각이 맞는지 틀린지 판별하는 문제
가장 큰 변을 출력하면 된다.

입력
6 8 10
25 52 60
5 12 13
0 0 0

출력
right
wrong
right
"""

import sys
Table=[1]
while(True):
    a,b,c =map(int, sys.stdin.readline().split())
    if a==0 and b==0 and c==0:
        break
    Table=[a,b,c]
    T=max(Table)
    ab=0
    for k in Table:
        if k==T:
            continue
        ab +=k*k
    if T*T==ab:
        print('right')
    else:
        print('wrong')