# https://www.acmicpc.net/problem/6131

"""
(1 ≤ B ≤ A ≤ 500)

A의 제곱은 B의 제곱보다 N만큼 커 (1 ≤ N ≤ 1,000)
해당 규칙을만족하는 (A,B) 쌍을 구하여라

N은 입력 값으로 주어진다. (1 ≤ N ≤ 1,000)

#A*A==B*B+N 이 성립하면 카운트 N을 뛰어 넘는 범위이면 꽁띵뉴
"""

import sys

N=int(sys.stdin.readline())

cnt=0

for A in range(2,501):

    for B in range(1, A+1):
        if A*A==B*B+N:
            cnt+=1

print(cnt)