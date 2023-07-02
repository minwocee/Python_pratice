# 딕셔너리 사용해서 구현한 부분.

import sys#, collections

N, M = map(int, sys.stdin.readline().split())

# '1':[] 형태로 들어가게 된다.
N_arr = {i+1:[] for i in range(N)}


# 이제 내용물을 추가해주자
for i in range(M):
    son, mom = map(int, sys.stdin.readline().split())
    N_arr[mom].append(son)


# 탐색연산 횟수를 반환해주는 함수 작성
def check(rootnode):
    # DFS 방식을 구현하면 된다. stack 사용하기
    #frontier=collections.deque([])
    frontier = []
    frontier.append(rootnode)
    cnt = 0
    visited = [False for _ in range(N+1)]    # 방문체크
    visited[rootnode] = True     # 시작노드 True로 바꿔주기
    while(frontier):
        a = frontier.pop()
        
        for n in N_arr[a]:
            if visited[n]:
                continue
            frontier.append(n)
            visited[n] = True
            cnt+=1
    
    return cnt


# 각 노드의 탐색 정보를 가지고 있게 함(탐색 횟수를 -1로 두고, 최곳값을 찾게 구현한다.)
ans_num = []
top = -1
for i in range(1,N+1):
    now = check(i)
    # 탐색횟수가 더 큰게 존재하면 왕을 교체한다.
    if top< now:
        top = now
        ans_num.clear()
        ans_num.append(i)
        
        
    # 동점자 발생시 후보로 넣는다
    elif top == now:
        ans_num.append(i)

# 우승자들 발표
print(*ans_num)

# 메모리 초과가 발생한다 계속....