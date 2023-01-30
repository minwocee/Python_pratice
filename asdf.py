# https://www.acmicpc.net/problem/1347

'''
전부다 0으로 초기화 하고 거쳐 온 길을 1로 바꾼다.이후 거쳐온 길을 1로 바꿔준뒤 
규격에 맞게 슬라이싱을 진행한뒤, 1이면 .. 0이면 # 으로 해서 출력한다.
'''

# 원점 (50,50)으로 둔다.

import sys

N=int(sys.stdin.readline())

move=sys.stdin.readline().strip()    #행동강령

check_list=[[0]*101 for _ in range(101)]    #101*101개의 배열을 



now_position=[50,50]    #현재 좌표 초기화()
check_list[50][50]=1    #현재 좌표 True 해줌

now_watch=2    #현재 바라보는 방향(북 0 동 1 남 2 서 3)

#움직이는 좌표를 설정 한다. 북 동 남 서 이동한다.
dx=[0, 1, 0, -1]
dy=[1, 0, -1, 0]

mx=[50]
my=[50]

for order in move:    #행동에 따른 좌표 이동을 실시한다.

    if order=='R':    #우회전이면
        now_watch+=1
        now_watch%=4


    elif order=='L':    #좌회전이면
        now_watch-=1
        now_watch%=4


    elif order=='F':    #전진이면
        x,y=dx[now_watch]+now_position[0], dy[now_watch]+now_position[1]
        
        mx.append(x)    #내가 흔적을 남진 X축 계산시
        mx.append(y)    #내가 흔적을 남긴 Y축 계산시

        now_position=[x,y]
        
        check_list[now_position[0]][now_position[1]]=1


# 좌표에 1을 입력하는걸 완료 하였다.


print(mx)
print(my)





