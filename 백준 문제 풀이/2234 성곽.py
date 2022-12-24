# https://www.acmicpc.net/problem/2234

# 서쪽(1) 북쪽(2) 동쪽(4) 남쪽(8) 벽이있을떄 더하는 수이다.
# 만약 오른쪽(동쪽)에만 구멍이 뚫려있으면 1+2+8이므로 11이 입력이 된다.
"""
출력해야되는값 3가지
1. 이 성에 있는 방의 개수
2. 가장 넓은 방의 넓이
3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
"""

""" BFS(Breadth First Search), 너비우선탐색
윗층 좌측부터 탐색을 시작하는 과정 (왼쪽 --> 오른쪽으로) 
1 2 3
4 5 6
7 8 9... 이런식으로 진행한다고 생각하면 편하다(보통은 트리의 형태라는것을 알아두자)

이 알고리즘의 핵심은 큐(queue)를 사용하는것

노드들중에서 아직 방문하지 않았던 노드의 정보만 큐에 넣어 먼저 큐에 
들어있던 노드부터 방문하면된다.

Collections 라이브러리에서 deque(덱, 양쪽 방향에서 입력,출력이 가능한 구조)를 사용하면 시간 절약이 가능(list 자료형을 이용한 큐의 list.pop은 시간복잡도가 O(N)이다.())

또한 인접 노드 중 방문하지 않았던 노드를 큐에 넣을 때는 파이썬 데이터 타입 중 set 을 사용하면 구현할수 있다.
"""





















""" 다른분의 코드"""
from collections import deque
import sys
input = sys.stdin.readline     #이렇게 해두면 sys.stdin.readline()을 매번 쓸필요가 없다
dx = [0, -1, 0, 1]    #좌표이동 X축
dy = [-1, 0, 1, 0]    #좌표이동용 Y축


def bfs(i, j):
    q = deque()    #덱 구조 선언
    q.append([i, j])     #행의개수, 열의개수가 들어감 덱의 공간을 확보
    visit[i][j] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == 0:
                if k == 0:
                    if 1 & s[x][y]: continue   #왼쪽 비트 비교 and 연산
                elif k == 1:
                    if 2 & s[x][y]: continue    #오른쪽 비트 비교 and 연산해서 나온 2진수를 10진수로 나옴 (0만 아니면 if가 성립)
                elif k == 2:
                    if 4 & s[x][y]: continue
                elif k == 3:
                    if 8 & s[x][y]: continue
                visit[nx][ny] = 1
                q.append([nx, ny])
                cnt += 1
    return cnt


n, m = map(int, input().split())
s = [list(map(int, input().split())) for i in range(m)]
visit = [[0] * n for i in range(m)]     #방문한곳은 나중에 1로 출력을 한다(현재는 0으로 한다.)
result1, result2, result3 = 0, 0, 0

for i in range(m):    # i는 행의정보
    for j in range(n):    #j는 열의정보 
        if visit[i][j] == 0:
            result1 += 1
            result2 = max(result2, bfs(i, j))

for i in range(m):
    for j in range(n):
        num = 1
        while num < 9:
            if num & s[i][j]:
                visit = [[0] * n for k in range(m)]
                s[i][j] -= num
                result3 = max(result3, bfs(i, j))
                s[i][j] += num
            num *= 2

print(result1)
print(result2)
print(result3)

























