# https://www.acmicpc.net/problem/10773

import sys
from collections import deque

N=int(sys.stdin.readline())
my_dec=deque([])

for _ in range(N):
    K=int(sys.stdin.readline())
    
    if len(my_dec)==0 and K==0:
        continue

    if K!=0:
        my_dec.append(K)
    else:
        my_dec.pop()

print(sum(my_dec))