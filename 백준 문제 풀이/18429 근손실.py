# https://www.acmicpc.net/problem/18429
# 근손실


# DP 인듯

# (1 ≤ 날짜 ≤ 8, 1 ≤ 운동키트 ≤ 50) 


import sys
from itertools import combinations, permutations

날짜수, 근손실 = map(int, sys.stdin.readline().split())
루틴 = list(map(int,sys.stdin.readline().split()))

# 깔끔하게 덜어내는 경우의 수
for i in range(날짜수):
    루틴[i] -= 근손실
    
경우의수 = list(permutations(루틴, 날짜수))

cnt = 0


def counter(text):
    summ = 0
    
    for i in text:
        if summ<0:
            return 0
        summ += i
    return 1

for k in 경우의수:
    cnt+=counter(k)
#print(경우의수)
print(cnt)
    