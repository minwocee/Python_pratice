#

























# 손익 분기점을 판별 (A= 사업 벌이면 무조건 내는 고정 비용 B= 1대 만드는 비용 C=한대 팔면 나오는 수익)

import sys

A,B,C=map(int, sys.stdin.readline().strip().split())

if C-B<=0:
    print(-1)
else:
    print(int(A/(C-B)+1))    #수학적 공식을 이끌어내야함 반복문 돌리면 시간초과가 떠버린다