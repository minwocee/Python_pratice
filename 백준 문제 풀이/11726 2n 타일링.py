# # https://www.acmicpc.net/problem/11726

# 피보나치 점화식 가진 DP

import sys

가로폭 = int(sys.stdin.readline())

#가로폭이 홀수이면, 무조건 ㅣ 막대 써야함

Table=[0]*(가로폭+1)

Table[0]=1
Table[1]=2

if 가로폭>=3:
    for i in range(2,가로폭):
        Table[i]=Table[i-1] + Table[i-2]

print(Table[가로폭-1]%10007)    #나머지 연산 해주는거 잊지 말자









