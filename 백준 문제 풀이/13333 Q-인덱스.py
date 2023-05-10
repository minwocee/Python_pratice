# https://www.acmicpc.net/problem/13333

"""
조건
n<=1000
인용횟수: 0~ 10,000
"""

import sys

n= int(sys.stdin.readline())    #논문 개수
N=list(map(int,sys.stdin.readline().split()))   #횟수 입력

N.sort()
N.reverse()


for i in range(n+1,-1,-1):    #비교해야할 수 n+1부터 0까지 비교 
    cnt=0
    for k in N:
        if k>=i:
            cnt+=1
    
    if cnt>=i:
        print(i)
        exit(0)
# 아까처럼 모든 조건을 충족하지 않는 경우 실행될것들

"""
문제 설명이 이상함, 숫자가 아무리 커도 정답의 범위는 0~논문의 개수 까지 임

반례1 
5
3 99 98 97 96
답: 4

5,4,3,2,1,0까지 비교를 시작 한다.
4보다 크거나 같은게 4개라서 답이 4
k번 이상 인용된 논문이 k 이상

반례2
1
0
답: 0

반례3
5
100 200 300 400 500
답: 5

"""