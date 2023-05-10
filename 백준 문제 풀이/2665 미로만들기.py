# https://www.acmicpc.net/problem/2665

'''
n×n 바둑판 모양으로 총 n2개의 방이 있다. 일부분은 검은 방이고 나머지는 모두 흰 방이다. 
검은 방은 사면이 벽으로 싸여 있어 들어갈 수 없다. 서로 붙어 있는 두 개의 흰 방 사이에는 문이 있어서 지나다닐 수 있다. 
윗줄 맨 왼쪽 방은 시작방으로서 항상 흰 방이고, 아랫줄 맨 오른쪽 방은 끝방으로서 역시 흰 방이다.

시작방에서 출발하여 길을 찾아서 끝방으로 가는 것이 목적인데, 
아래 그림의 경우에는 시작방에서 끝 방으로 갈 수가 없다. 
부득이 검은 방 몇 개를 흰 방으로 바꾸어야 하는데 되도록 적은 수의 방의 색을 바꾸고 싶다.

아래 그림은 n=8인 경우의 한 예이다.



위 그림에서는 두 개의 검은 방(예를 들어 (4,4)의 방과 (7,8)의 방)을 흰 방으로 바꾸면, 
시작방에서 끝방으로 갈 수 있지만, 어느 검은 방 하나만을 흰 방으로 바꾸어서는 불가능하다. 
검은 방에서 흰 방으로 바꾸어야 할 최소의 수를 구하는 프로그램을 작성하시오.

단, 검은 방을 하나도 흰방으로 바꾸지 않아도 되는 경우는 0이 답이다.

'''

# 반드시 1개 이상의 검은방을 흰방으로 바꾸어야 하며, 변환 없이도 목적지까지 도착이 가능하면, 0을 출력한다.
# 분명 BFS나 DFS를 쓰는 문제인것 같기는 하다.

         
'''

# 미로만들기
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

arr = []
for i in range(N):
    arr.append(list(map(int, input().strip())))


def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[-1] * N for _ in range(N)]
    visited[0][0] = 0
    while q:
        x, y = q.popleft()
        if x == N-1 and y == N-1:
            return visited[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if arr[nx][ny] == 1:
                    q.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


print(bfs())
'''


import sys
from collections import deque

n=int(sys.stdin.readline())

Field=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]    # 2차원 배열 정보를 담는다 (1: 흰방(통과가능), 0:검은방(막힘))

# 북 동 남 서 방향으로 진행한다.
dx=[0,1,0 ,-1]
dy=[1,0,-1,0]

# BFS 사전작업 끝
# 시작점 (0,0) 목표점 (n-1,n-1) 도착하면 된다.


def BFS():
    # DQ는 다음 움직임을 탐색할수 있는 목록들을 가지고 있는 덱 이라고 생각한다.
    DQ=deque()
    DQ.append((0,0))
    
    #방문했던 길을 기록하는곳
    visited=[[-1]*n for _ in range(n)]    # 각 방의 방문 기록을 남길때 사용하는 visited 필드
    visited[0][0]=0    # 첫 시작점은 당연히 방문한걸로 초기화를 해야 한다.
    
    while DQ:
        x,y =DQ.popleft()    # 행,열 정보가 각각 담긴다.
        
        # 종료조건을 설정한다.(최종 목적지 도달시)
        if x==n-1 and y==n-1:
            return visited[x][y]
        
        # 4개의 방향으로 좌우이동을 실시함 (저번의 데스나이트는 6개의 좌표를 이동했던걸로 기억한다.)
        for k in range(4):
            mx=x+dx[k]
            my=y+dy[k]
            
            # 유효한 값이면 실행한다.
            if 0<=mx<n and 0<=my<n and visited[mx][my]==-1:
                # 흰방이면 더 움직일수 있는 공간을 발견!
                if Field[mx][my]== 1:
                    # 왜 어펜드 레프트일까 아마 이걸 왼쪽으로 넣어주어야지 될것같다
                    DQ.appendleft((mx,my))
                    visited[mx][my] = visited[x][y]    # 첫 점에서 흰방으로 이동하는 경우는 벽을 부술 필요가 없다. 따라서 첫 지점의 값인 0을 넣으면 된다.
                # 검은 방인 경우 벽을 부수어야 한다. 단 탐색의 우선순위는 흰방이므로, 오른쪽에서 append를 해서 원소가 오른쪽으로 들어가게 해야 한다.
                else:
                    DQ.append((mx,my))
                    visited[mx][my] = visited[x][y]+1    # 방이 막혔기에, 코스트를 소모해서 벽을 제거 한다.
                    
print(BFS())