import sys

change, running_time=map(int, sys.stdin.readline().split())
# 기본적으로 오른쪽을 보고 있는 상태 이다.

'''
3번 100초

30초 right   +30
50초 right         -20
60초 left    +10 
방향을 바꾼 시간임

30미터 간다음 우회전, 
'''
moving_table = [list(map(str, sys.stdin.readline().strip().split())) for _ in range(change)]

# print(moving_table)

now_look=1
# (1,0) (0,1) (-1,0) (0,-1) 
# 0북 1동 2남 3서
dx=[0,1,0,-1]    
dy=[1,0,-1,0]

x_point=0
y_point=0

움직인포인트=0
for Move in moving_table:
    k=int(Move[0])
    if now_look%4==1: #오른쪽 보고 있으면 실행
        x_point+=(k-움직인포인트) #형변환 실행 하자
    elif now_look%4==2:
        y_point-=(k-움직인포인트) #형변환 실행 하자
    elif now_look%4==3:
        x_point-=(k-움직인포인트) #형변환 실행 하자
    elif now_look%4==0:
        y_point+=(k-움직인포인트) #형변환 실행 하자
    
    움직인포인트=k

    if Move[1]=='right':
        now_look+=1 #남쪽을 보게 한다.
    elif Move[1]=='left':
        now_look-=1
    
    now_look=now_look%4

    #print(x_point, y_point , '현재 무브 상태')

# print('현재 바라보는 방향', now_look)
# print('현재 움직 포인트', k)

if now_look%4==1: #오른쪽 보고 있으면 실행
    x_point+=(running_time-움직인포인트) #형변환 실행 하자
elif now_look%4==2:
    y_point-=(running_time-움직인포인트) #형변환 실행 하자
elif now_look%4==3:
    x_point-=(running_time-움직인포인트) #형변환 실행 하자
elif now_look%4==0:
    y_point+=(running_time-움직인포인트) #형변환 실행 하자

print(x_point, y_point)







