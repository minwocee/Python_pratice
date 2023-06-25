# 딕셔너리 사용해서 구현한 부분.

import sys, collections

N, M = map(int, sys.stdin.readline().split())

# '1':[] 형태로 들어가게 된다.
N_arr = [[] for _ in range(N+1)]


# 이제 내용물을 추가해주자
for i in range(M):
    son, mom = map(int, sys.stdin.readline().split())
    N_arr[mom].append(son)


# 탐색연산 횟수를 반환해주는 함수 작성
def check(rootnode):
    # BFS 방식을 구현하면 된다.
    frontier=collections.deque([])
    frontier.append(rootnode)
    cnt = 0
    visited = [False for _ in range(N+1)]
    while(frontier):
        a = frontier.popleft()
        if len(N_arr[a]):
            for n in N_arr[a]:
                if visited[n]:
                    continue
                frontier.append(n)
                cnt+=1
    
    return (rootnode, cnt)


# 각 노드의 탐색 정보를 가지고 있게 함(탐색 횟수를 -1로 두고, 최곳값을 찾게 구현한다.)
ans_num = [(0,-1)]

for i in range(1,N+1):
    now = check(i)
    # 탐색횟수가 더 큰게 존재하면 왕을 교체한다.
    if ans_num[0][1]< now[1]:
        ans_num = [now]
        
    # 동점자 발생시 후보로 넣는다
    elif ans_num[0][1] == now[1]:
        ans_num.append(now)
    

# 우승자들 발표
for i in ans_num:
    print(i[0], end=' ')

# 메모리 초과가 발생한다 계속....