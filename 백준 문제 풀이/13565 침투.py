# https://www.acmicpc.net/problem/13565

# 시간제한 1초, 메모리제한 512 MB

# 그냥 DFS로 풀면 될것 같은 문제 이다.

# 행개수: 1000이하, 열개수: 1000 이하


# 2차원 리스트 필드정보가 들어온다.
def DFS(new_Field, width, height):
    
    # 참고로 필드 요소는 문자열임ㄴ
    # 경계 자료구조에서 사용될 stack 선언
    frontier_stack=[]
    
    
    # 시작점 포인트 잡아 주어야 함(첫줄에서 행 좌표가 0인 곳을 선택하는것이다.)
    for i in range(height):
        if new_Field[1][i] == '0':
            frontier_stack.append((1,i))
    
    # 탐색 가능 방향은 상,하,좌,우 모두 가능하게 한다.
    # 0북 1동 2남 3서
    visited={}
    
    for i1 in range(width+2):
        for i2 in range(height+2):
            
            if new_Field[i1][i2]=='1':
                visited[(i1,i2)] = True   # 벽,이미갔던데 못가는데를 의미
            else:
                visited[(i1,i2)] = False   #갈수있는 공간을 의미 한다.
    
    while(len(frontier_stack)!=0):
        now = frontier_stack.pop()    # 도달 자료구조에서 하나 가져 온다.
        visited[now]= True
        
        nexts = [(now[0],now[1]-1), (now[0],now[1]+1), (now[0]-1,now[1]), (now[0]+1,now[1])]
        
        for i in nexts:
            
            # 맨 밑 도달시 사용
            if i[0]==width:
                print("YES")
                exit(0)
            
            # 왓던곳이 아니면서, 벽이 아니면 수행 가능
            if (visited[i] == False) and (new_Field[i[0]][i[1]] != '1'):
                frontier_stack.append(i)
                
    print("NO")
            
        
        
        
        
            
        
        
        
        
import sys

# 가로개수, 세로개수 입력 받는다.
width, height = map(int, sys.stdin.readline().split())

Field = [list(sys.stdin.readline().strip()) for _ in range(width)]

'''
DFS 에서 필요한 자료구조

경계 자료구조: stack 
도달상태를 나타내는 부분 또한 필요

start 리스트, 시작점 리스트

end 조건 --> y좌표의 리스트가 
행,열의 개념을 사용할것이다. 1행의 2열 개념 처럼 (2,1)이 아니라
'''

# 필드의 외곽에 벽을 세워 주어야 한다.

new_Field = [['1']*(height+2)]

for i in Field:
    new_Field.append(['1']+i+['1'])
    
new_Field.append(['1']*(height+2))
# NO, YES를 탐색 조건으로 반환 한다.
DFS(new_Field, width, height)
