# https://www.acmicpc.net/problem/20002

# 사과나무

import sys

# 누적합을 어떻게 쓸지 고민이 된다.

# 일단 누적합 테이블을 만들자
T = int(sys.stdin.readline())
Table = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
누적합_Table = [[0]*T for _ in range(T)]

# 원점 초기화
누적합_Table[0][0] = Table[0][0]

# 첫번째 행 초기화 완료
for i in range(1,T):
    누적합_Table[0][i] = Table[0][i]+ 누적합_Table[0][i-1] 

# 첫번째 열 초기화 완료
for i in range(1,T):
    누적합_Table[i][0] = Table[i][0]+ 누적합_Table[i-1][0] 


# 이제 나머지 내용물 채우기만 하면 됨
for i in range(1,T):
    for j in range(1,T):
        누적합_Table[i][j] = 누적합_Table[i][j-1]+누적합_Table[i-1][j]+Table[i][j]-누적합_Table[i-1][j-1]
        

# 누적합 테이블에 0이라는 쿠션을 넣자
누적합_Table = [[0]*(T+1)] + 누적합_Table

for i in range(1,T+1):
    누적합_Table[i] = [0]+ 누적합_Table[i]

#print(누적합_Table)


now = -1001

# 길이가 2 이상인 정사각형 부터 계산을 실시 한다.

for size in range(2,T):# 사각형 사이즈를 담당
    
    for i in range(size,T+1):
        for j in range(size,T+1):
            now1 = 누적합_Table[i][j]-누적합_Table[i-size][j]-누적합_Table[i][j-size]+누적합_Table[i-size][j-size]
            if now<now1:
                now = now1


# 이제 하나 짜리 계산 한다. (1*1 사이즈의 정사각형도 고려를 해준다.)
for i in range(T):
    for j in range(T):
        now1 = Table[i][j]
        if now<now1:
            now = now1

print(now)