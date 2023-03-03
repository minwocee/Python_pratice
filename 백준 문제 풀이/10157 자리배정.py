# https://www.acmicpc.net/problem/10157
import sys

# 가로의 길이, 세로의 길이 입력 (1,1) ~ (7,6) 까지의 좌표가 존재함
W,H=map(int,sys.stdin.readline().split())

# 모듈러 연산을 해야 하나?
# 일단 입력 받은대로 배열을 만들어보자

Field = [[0]*W for _ in range(H)]

#print(Field[0])   정상적으로 생성 완료

# 처음에는 북쪽을 보고 있다.(북,동,남,서)방향 0,1,2,3
dx=[0,1,0,-1]
dy=[1,0,-1,0]

now_watch=0   #현재 바라보는 방향
now_number=[0,0]    #첫 좌석의 좌표


# 1. 만약 해당 방의 넘버가 1이면 방향을 꺾는다.
# 2. 만약 해당 방의 넘버가 0이면, 직진한다.
# 3. 만약 카운터가 W*H이면, 반복을 멈춘다.


for ___ in range(W*H):
        
    try:
        if Field[now_number[0],now_number[1]]==0:   # 만약 해당방이 아직 지나가지 않은 방이면 -> 마킹을 한다.
            Field[now_number[0],now_number[1]]=1   # 해당 방은 지나왔다고 생각한다.
            now_number=[now_number[0]+dx[now_watch], now_number[1]+dy[now_watch]]    # 현재 위치를 수정한다.
            
        elif Field[now_number[0],now_number[1]]==1:    # 만약 해당 방을 이미 지나갔었다면 오른쪽으로 회전한다,
            now_watch=(now_watch+1)%4      # 모듈러 연산을 실행한다.
            now_number=[now_number[0]+dx[now_watch], now_number[1]+dy[now_watch]]    # 현재 위치를 수정한다.
                
    # 리스트의 범위를 벗어나면 실행한다.
    except IndexError:
        
        
            
            

    
        
        
        
        
    

        
    
    