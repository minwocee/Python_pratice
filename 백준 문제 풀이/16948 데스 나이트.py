# https://www.acmicpc.net/problem/16948

# 첫번째 검사: X 축방향으로 이동하는데 둘의 X축 간격이 짝수이면 됨
# 두번쨰 검사: 이동을 했다면 Y축방향으로 수직 이동을 하면된다.(만약 이것 또한 간격이 짝수가 아니면 넘어가게 된다.)
'''
import sys

N=int(sys.stdin.readline())    # 정사각형 모양의 체스판을 만듬
r,c,r2,c2=map(int, sys.stdin.readline().split())    # 시작점, 목적지의 좌표가 주어 진다.

# 첫번째 검사를 수행한다.
if (r2-r)%2!=0:
    print(-1)
    exit(0)
    
# 두번째 검사를 수행한다.(만약 이동이 가능하다면, 4개의 방향이 존재 1,2,3,4사분면까지)    
else:
    cnt=0
    # 나보다 오른쪽 위에 있는 경우
    if r2>r and c2>c:
        ahr=abs(r2-r)//2    # 몫
        r=r+2*ahr
        c=c+1*ahr
        cnt+=ahr   # 카운터 증가
        #이후 Y축 이동이 가능한지 살펴보아야 한다.(+2, -2)
        if (abs(c2-c))%2==0:
            cnt+=abs(c2-c)//2
            print(cnt)
            exit(0)
        else:
            print(-1)
            exit(0)
            
    # 나보다 오른쪽 아래 있는 경우
    elif r2>r and c2<c:
        ahr=abs(r2-r)//2    # 몫
        r=r+2*ahr
        c=c-(1*ahr)
        cnt+=ahr   # 카운터 증가
        #이후 Y축 이동이 가능한지 살펴보아야 한다.(+2, -2)
        if (abs(c2-c))%2==0:
            cnt+=abs(c2-c)//2
            print(cnt)
            exit(0)
        else:
            print(-1)
            exit(0)
    
    # 나보다 왼쪽 위에 있는 경우
    elif r2<r and c2>c:
        ahr=abs(r2-r)//2    # 몫
        r=r-(2*ahr)
        c=c+(1*ahr)
        cnt+=ahr   # 카운터 증가
        #이후 Y축 이동이 가능한지 살펴보아야 한다.(+2, -2)
        if (abs(c2-c))%2==0:
            cnt+=abs(c2-c)//2
            print(cnt)
            exit(0)
        else:
            print(-1)
            exit(0)
    
    
    # 나보다 왼쪽 아래에 있는 경우
    elif r2<r and c2<c:
        ahr=abs(r2-r)//2    # 몫
        #print(ahr, "목을 의미")
        r=r-(2*ahr)
        c=c-(1*ahr)
        cnt+=ahr   # 카운터 증가
        #print(ahr, "목을 의미")
        
        #이후 Y축 이동이 가능한지 살펴보아야 한다.(+2, -2)
        if (abs(c2-c))%2==0:
            cnt+=abs(c2-c)//2
            print(cnt)
            exit(0)
        else:
            print(-1)
            exit(0)
            
    # 같은 X축 선상에 있는 경우
    elif c==c2:
        if (abs(r2-r))%2==0:
            cnt+=abs(r2-r)//2
            print(cnt)
            exit(0)
        else:
            print(-1)
            exit(0)
    # 같은 Y축 선상에 있는 경우
    elif r==r2:
        if (abs(c2-c)%2)==0:
            cnt+=abs(c2-c)//2
            print(cnt)
            exit(0)
        else:
            print(-1)
            exit(0)
'''

'''
graph[0] -> 비워둠
graph[1] -> 1번노드가 2,3,8번 노드와 이어져 있다.
graph[2] -> 2번노드가 1,7번 노드와 이어져 있다.
graph[3] -> 3번노드가 1,4,5번 노드와 이어져 있다 ...
.
.
.
graph[8] -> 8번노드가 1,7번 노드와 이어져 있다.
'''

# https://www.youtube.com/watch?v=CJiF-muKz30&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=21

# 다른분의 코드를 분석하기())
'''
from collections import deque #(덱 사용 예)

# BFS 함수 생성
def bfs(y, x):
    q = deque()
    q.append((y, x))    # 초기 위치가 담긴다.
    graph[y][x] = 0    # 여기서 그래프는 전역 리스트임
    
    while q:
        y, x = q.popleft()    # 처음: (y,x) 튜플임
        for dy, dx in d:    #d는 움직일수 있는 좌표를 튜플원소를 가진 리스트 이다.
            ny, nx = y+dy, x+dx    # 점에따른 좌표이동을 실시한다.
            
            # 1. 만약 격자판 밖을 벗어나지 않고, 해당 위치의 좌표가 아직 도달하지 않는(-1인곳) 곳이면 실행됨
            if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == -1:
                q.append((ny, nx))    #변경하고난 위치가 담긴다.
                graph[ny][nx] = graph[y][x]+1    #해당 위치에 +1을 해준다.(0으로 바꿈으로써 룸 클리어 했다는 의미)
            # 또한 만약 격자판을 벗어나는 큐의 원소가 발생하면
            # append를 멈추기 때문에, while문의 종료 조건이 된다.

# 입력 받기
n = int(input())
r1, c1, r2, c2 = map(int, input().split())
graph = [[-1] * n for _ in range(n)]    #2차원 배열의 격자판을 생성한다. 
d = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]    #6개의 점으로 이동하는 좌표값을 설정한다.
bfs(r1, c1)    # BFS 함수를 돌린다.

print(graph[r2][c2])    # 만약에 이동이 불가능하면 -1을 출력한다.(이미 -1로 초기화가 되어있다.)

for _ in graph:
    print(_)
    
'''








import sys
import collections
# 첫 좌표가 5,1이다 -> 1행의 5열 개념으로 생각 그래서 x,y를 바꿔서 생각한다.
def bfs(y,x):    #(열,행) 좌표로 들어온다고 생각한다.
    queue=collections.deque()    # 빈 큐를 생성한다.
    queue.append((y, x))
    Field[y][x]=0    # 처음 이동을 시작한 지점은 -1에서 0으로 바꿔준다.(왔던길을 표시한거임)
    while queue:
        y,x = queue.popleft()
        
        for move_y, move_x in Move:
            now_y,now_x = y+move_y,x+move_x
            
            # 유효한 값이면, 큐에 집어 넣는다.    만약 왔던길을 다시 돌아가는 경우도 여기서 멈추어 준다.(==1)
            if 0<=now_x<N and 0<=now_y<N and Field[now_y][now_x]==-1:
                queue.append((now_y,now_x))
                Field[now_y][now_x] = Field[y][x]+1    # 이전 위치의 코스트에서 +1을 해주는 개념 이다.
            
        



N=int(sys.stdin.readline())
r1,c1,r2,c2=map(int,sys.stdin.readline().split())

Move=[(-2,-1),(-2,1),(0,2),(0,-2),(2,-1),(2,1)]

Field=[[-1]*N for _ in range(N)]
# 첫 좌표가 5,1이다 -> 1행의 5열 개념으로 생각
bfs(r1,c1)
print(Field[r2][c2])    # 만약 해당 좌표가 한번도 도달하지 못한곳이라면, -1이 출력이 될것이다.