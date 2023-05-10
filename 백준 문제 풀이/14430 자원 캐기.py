# https://www.acmicpc.net/problem/14430

# 아마 브루트 포스겠지 다 둘러보려면
# 역시 아니군
# DAG : Directed acyclic Graph 구조 ,방향성 이 있는 비순환 그래프
# DP 를 활용해서 푸는 문제이다.


'''
5 4
0 1 0 0
0 0 1 0
1 1 0 0
1 0 1 0
1 1 0 0
'''
'''
N, M = map(int, input().split())    # 행개수 & 열개수 입력 받음
li = [list(map(int, input().split())) for _ in range(N)]    # 좌표들의 정보를 입력 받는다.
dp = [[0]*M for _ in range(N)]    # 전체 테이블이 0으로 초기화된 DP테이블을 만든다.

dp[0][0] = li[0][0]    # 각 테이블의 시작점에 해당하는 좌표 포인트를 일치하게 만든다.(첫 포인트 같게 만든다)

for i in range(N):     # 행담당(한줄)
    for j in range(M):    #열 담당(한줄의 원소 하나)
        
        # 왼쪽,오른쪽 테두리 검사
        if i == 0 and j == 0:
            continue
        
        # 왼쪽 ->오른쪽 직선 검사
        elif i > 0 and j == 0:
            dp[i][j] = dp[i-1][j]     # 이전 경우의 수를 다음 경우의 수로 구한다.
        
        # 위 -> 아래 직선 검사
        elif i == 0 and j > 0:
            dp[i][j] = dp[i][j-1]
        
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
        if li[i][j] == 1:
            dp[i][j] += 1
            
print(max(map(max, dp)))
'''




# 가장 많이 자원을 먹을수 있는 경우의수를 찾는 함수 이다.
def myway(x,y,dp,Field):
    if x<0 or y<0:
        return 0    #올바르지 않은 값 처리
    
    if dp[x][y] != -1:
        return dp[x][y]    # 이미 연산된
    
    dp[x][y]= Field[x][y]
    dp[x][y] += max(myway(x-1,y,dp,Field), myway(x,y-1,dp,Field))   # 재귀 함수
    return dp[x][y]
    

import sys

N,M = map(int,sys.stdin.readline().split())    # 행개수(가로), 열개수(세로)

# 자원이 존재하는 테이블 정보를 입력 받는다.
Field=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]    # 정상적으로 2차원 리스트 입력 완료

#DP 테이블 설정 (전체를 우선 -1로 초기화 한다, DP 테이블은 이전에 계산된 값들을 저장하고 있다)
DP=[[-1]*M for _ in range(N)]
DP[0][0]=Field[0][0]    # DP 테이블의 시작지점과 실제 필드의 첫 지점을 같게 한다.


print(myway(N-1,M-1,DP,Field))    # 오른쪽 아래에서 부터 시작한것 같다

# for _ in DP:
#     print(_) 




    
'''
(입력)
5 4
0 1 0 0
0 0 1 0
1 1 0 0
1 0 1 0
1 1 0 0

(결과)
4 -> 최대 자원
[0, 1, 1, 1]
[0, 1, 2, 2]
[1, 2, 2, 2]
[2, 2, 3, 3]
[3, 4, 4, 4]
'''

'''
# 내 방식대로 구현한다.


def findway(x,y,N,M,dp,data):
    
    if x>M-1 or y>N-1:    # 밖을 벗어나는 경우 처리
        return 0
    
    if dp[x][y] !=-1:   # 이미 지나온 길이라면
        return dp[x][y]
    
    dp[x][y]=data[x][y]
    dp[x][y] += max(findway(x+1,y,dp,data), findway(x,y+1,dp,data))   # 재귀 함수
    return dp[x][y]
        


import sys

N,M=map(int,sys.stdin.readline().split())

data=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]    # 자원 정보가 담긴 데이터가 있따.

dp=[[0]*M for _ in range(N)]    # dp 테이블을 초기화 한다 (0으로, 해당 좌표까지의 모은 자원의 총합이 담길 예정)

# find way를 설정 한다.
dp[0][0]=data[0][0]

print(findway(0,0,N,M,dp,data))

print(dp)

'''

