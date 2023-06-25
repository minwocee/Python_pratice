#https://www.acmicpc.net/problem/1240

# 노드사이의 거리
'''
import sys

Node, Test = map(int, sys.stdin.readline().split())

# 그래프 맵(가중치를 넣는다. 0~N까지의 노드가 직접 대응 된다.)
Graph = [[] for _ in range(Node+1)]

print("초기 그래프의 정보", Graph)
# 노드 정보를 입력 받는다.
for _ in range(Node-1):
    start,end,cost = map(int, sys.stdin.readline().split())
    # 각 노드에 대응되는 노드에 비용을 넣어 준다.
    Graph[start].append(cost)
    Graph[end].append(cost)

print("그래프 정보")
print(Graph)


# 시작, 목적지
from collections import deque
def bfs(S,E):
    my_queue = deque()
    
    # 초기화(튜플형태의 원소를 가진다.)
    my_queue.append((S,0))
    
    # 방문체크
    visited = [False]* (Node+1)
    
    # 첫 시작점은 방문했다고 가정한다.
    visited[S] = True
    
    while my_queue:
        현재노드, 거리 = my_queue.popleft()
        
        # 목적지 노드를 찾으면 반복 중지
        if 현재노드 == E:
            return 거리
        
        # 목적지가 아니라면 현재노드 그래프 원소 불러옴 [[], [2, 3], [2], [2], [2, 3, 1], [1]]
        for i, 가중치 in Graph[현재노드]:
            #방문하지 않는 노드라면 실행 한다.
            if not visited[현재노드]:
                visited[i] = True
                my_queue.append((i, 거리+가중치))
            
# 테스트케이스를 입력한다.
for _ in range(Test):
    start, end = map(int, sys.stdin.readline().split())
    print(bfs(start,end))
    



import sys
from collections import deque
input = sys.stdin.readline

def bfs(start,find):
    queue = deque()
    queue.append((start,0))
    visited = [False] * (n+1)
    visited[start] = True
    
    while queue:
        # d에는 점점 가중치가 누적되는 구조 이다.
        v, d = queue.popleft()
        
        if v == find: #찾는 노드와 번호가 일치하면 거리 리턴
            return d
        
        for i, l in graph[v]: #연관된 노드에 대한 노드번호와 간선길이
            if not visited[i]:
                visited[i] = True
                queue.append((i,d+l)) #지금까지 노드를 찾으면서 거리를 기록
    
n, m = map(int,input().split())    # 전체노드개수, 테스트케이스개수
graph = [[] for _ in range(n+1)]   # 2차원 리스트의 요소는 (노드번호, 가중치)이렇게 기록된다.

# 예를 들면 4번-2번, 가중치 3 이면, (4,3) (2,3) 이렇게 기록이 된다고 생각하면 된다.

# 노드정보를 입력 받는다.
for _ in range(n-1):
    n1, n2, l = map(int,input().split())
    graph[n1].append((n2,l))
    graph[n2].append((n1,l))

for _ in range(m):
    n1, n2 = map(int,input().split())
    print(bfs(n1,n2))
    
    
#print(graph, "**그래프 생성 결과 이다.**")

# [[], [(2, 2), (4, 3)], [(1, 2)], [(4, 2)], [(3, 2), (1, 3)]] **그래프 생성 결과 이다.** 이렇게 나오는데ㅐ
# [(2, 2), (4, 3)] --> (노드번호, 간선비용) (노드번호, 간선비용) 이렇게 만들어 진다.


'''

# 다시 코드를 짜보자
import sys
from collections import deque

def bfs(start,find):
    queue = deque()
    queue.append((start,0))
    visited = [False] * (N+1)
    visited[start] = True
    
    while queue:
        # d에는 점점 가중치가 누적되는 구조 이다.
        v, d = queue.popleft()
        
        if v == find: #찾는 노드와 번호가 일치하면 거리 리턴
            return d
        
        for i, l in Graph[v]: #연관된 노드에 대한 노드번호와 간선길이
            if not visited[i]:
                visited[i] = True
                queue.append((i,d+l)) #지금까지 노드를 찾으면서 거리를 기록

N, T = map(int ,sys.stdin.readline().split())

# 1~N까지의 인덱스 번호를 쓰기 위해서 N+1로 측정 한다.
Graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    s,e,w = map(int, sys.stdin.readline().split())
    Graph[s].append((e,w)) # 각 노드 별로 가중치를 담아 준다.
    Graph[e].append((s,w)) # 각 노드 별로 가중치를 담아 준다.
    
for _ in range(T):
    a,b = map(int, sys.stdin.readline().split())
    print(bfs(a,b))
#print(Graph)
