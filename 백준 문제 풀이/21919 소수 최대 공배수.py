# https://www.acmicpc.net/problem/21919
'''
n=1000
#a는 총 1001개 길이
a = [False,False] + [True]*(n-1)    # 인덱스 0과 1을 제외하고 나머지 전부 트투로 설정
primes=[]    #소수 담는 주머니

for i in range(2,n+1):# 2~1000 까지 
  if a[i]:    #이프 트루이면~
    primes.append(i)
    
    # i=2, range(2,1001,2) j=2,4,6,8...(2의배수를 False로 바꿈)
    # i=3, range(3,1001,3) j=3,6,9,12...(3의배수를 False로 바꿈)
    # 배수가 존재한다는것은 소수가 아니기에 False를 넣어준다.
    for j in range(2*i, n+1, i):
        a[j] = False
print(primes)
'''

#에라토스테네스의 체를 이용해서 소수 구해보자

import sys

N=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

arr.sort()
#에라토스테네스의 체 구현
n=arr[-1]

tf=[False,False]+[True]*(n-1)#인덱스와 실재값을 일치시키기위해 한칸씩일부러 밀어냄

for i in range(2,n+1):  #비효율
    if tf[i]:     #트루면 어펜드함, 기본 트루임 나중에 펄스로 바꿀 예정

        for j in range(2*i,n+1,i):#배수 만큼 넣어주기 #비효율
            tf[j]=False

sosu=[]

for _ in arr:
    if tf[_]:
        sosu.append(_)

if len(sosu)==0:
    print(-1)
    exit(0)

import math

king=sosu[0]
for i in sosu[1:]:
    king=math.lcm(king, i)

print(king)

"""
for i in ran
"""

    
    