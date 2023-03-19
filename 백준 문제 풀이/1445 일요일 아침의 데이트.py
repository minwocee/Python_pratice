# https://www.acmicpc.net/problem/1445

# 딱봐도 BFS죠?

# 왜BFS가 아닌지 알겠음
# 빨리 가는게 목적이 아님, 빙 둘러서라도 최대한 피해가는게 조건임
# 따라서 이 문제는 BFS로 푸는게 아닌것 같음


# 1순위 : 쓰레기를 밟지 않기
# 2순위 : 쓰레기 근처를 지나가지 않기.



import sys

N,M=map(int,sys.stdin.readline().split())    # 높이, 가로 입력 받음

start=0
Final=0

for i in range(N):
    A=list(sys.stdin.readline().strip())
    
    if 'S' in A:
        start=[i,A.index('S')]
    
    if 'F' in A:
        Final=[i,A.index('F')]
        
#print(start, 'S점 좌표')    # 높이, 가로
#print(Final, 'F점 좌표')    # 높이 가로 형식 y,x형태

