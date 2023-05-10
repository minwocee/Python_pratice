# https://www.acmicpc.net/problem/1463

'''
3으로 나누어 떨어지면 나눔
2로 나누어 떨어지면 나눔
1을 뺀다.
'''

import sys

N= int(sys.stdin.readline())
cnt = 0

while(N!=1):
    if N%3==0:
        N=int(N/3)
        cnt+=1
    elif N%2==0:
        N=int(N/2)
        cnt+=1
    else:
        N-=1
        cnt+=1
print(cnt, N)