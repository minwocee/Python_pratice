# https://www.acmicpc.net/problem/1347

# import sys

# N=int(sys.stdin.readline())
# Table = list(sys.stdin.readline())

"""
초기 위치와 바라보는 방향 설정 및 이동했던 좌표를 저장할 리스트를 생성
명령어를 하나씩 수행하며 위치 좌표와 방향을 변경하며 이동했던 좌표를 저장
이동하면서 찍힌 좌표의 최대값과 최소값의 차이로 최대 변의 길이를 계산
계산된 크기로 이차원배열을 생성 후 이동했던 좌표의 정보를 바탕으로 미로 완성
완성된 미로를 출력
""" 

"""다른분의 코드 분석"""

'''
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]    # 방향 전환을 위해서 사용 dx=상하 dy=좌우



command_length = int(input())    # 명령 항목들의 길이 입력 받음
commands = input()     # 문자열 형태로 입력 받음

dir = 2    # 이건 뭐지(아마 방향 설정하는데 쓰이는듯      <북쪽: 0, 동쪽: 1, 남쪽:2 ,서쪽:3>      )
pos = [0, 0]    # 현재 좌표를 0,0으로 설정
x_list = [0]    # 이건뭐지 (X축에서 이동한 과정이 담기는 리스트)
y_list = [0]    # 이건 뭐지 (Y축에서 이동한 과정이 담기는 리스트)
for command in commands:     # 입력받은 명령 문자열을 바탕으로 반복문 실행 (문자열을 앞에서부터 하나씩 꺼내 받는 형식)
    if command == 'L':    # 만약 해당 문자가 Left이면?
        dir = (dir - 1) % 4     # 연산을 통해 현재 dir는 1이 된다.(동쪽을 보는 형태)
    elif command == 'R':    # 연산을 통해 현재 dir는 3이 된다.(서쪽을 보는 형태)
        dir = (dir + 1) % 4    # %4 연산을 하는 이유는 LLLL식으로 문자열이 들어오면 한바퀴 돌아서 그래도인것과 같은 형태이기 떄문
    elif command == 'F':    # 만약 해당 문자열이 Foward 이면 실행
        x, y = pos     # x와 y에 각각 0,0이 들어간다 (이런식으로도 쓸수가 있구나)
        nx, ny = x + dx[dir], y + dy[dir]    #현재 위치 + (바라보고있는 방향으로 Foward(전진))해서 현재 좌표 설정
        x_list.append(nx)     #이동한 좌표를 X리스트에 더해줌
        y_list.append(ny)   #이동한 좌표를 Y리스트에 더해줌
        pos = [nx, ny]    # 현재 위치를 수정 한다.

max_x, min_x, max_y, min_y = max(x_list), min(x_list), max(y_list), min(y_list)     # 얼마만큼 X,Y의 이동반경인지 max와  min을 사용해 이들이 어디까지 돌아다녔나 확인

N, M = max_x - min_x + 1, max_y - min_y + 1   #최대값-최소값+1 을 통해 움직인 범위 측정 완료

start_x, start_y = abs(min_x), abs(min_y)    # 최소값은 음수가 나올수 있으므로 절대값abs를 활용 처음 영향을 미친 곳
# 이 부분을 이동시작점으로 잡고 #을 .으로 바꿔줄 예정

maze = [['#'] * M for _ in range(N)]    # ['#']으로 2차원 배열을 초기화 하는 과정

for x, y in zip(x_list, y_list):    #zip(리스트1, 리스트2)은 2개이상의 리스트에서 같은 위치(인덱스가 같다)에 있는 요소들을 쌍으로 묶어서 튜플 형태로 처리하는 과정
    maze[start_x + x][start_y + y] = '.'    #실제 이동 지점을 '#'에서 '.'으로 바꿔주는 과정

for line in maze:    # '.'수정이 끝난 2차원 리스트를 바탕으로 '구분자'.join(리스트) 형태를 통해 문자열 형태로 연결한다
    print("".join(line))

'''

"""
''.join(리스트) --> 공백없이 리스트를 문자열로 변환할때 쓰는 과정 

a=''
a+=str(['1']) 이런식으로 과정이 한번에 담겨있는듯

'구분자'.join(리스트)
"""

# 위치 이동 공식 설정(첫 지점을 0,0으로 잡고 , 동서남북 방향을 어떻게 표현할건지 설정)


import sys

N=int(sys.stdin.readline())
Move=sys.stdin.readline().strip()
#상하 좌우    (1,0) (0,-1) (-1,0) (0,1) 이렇게 4가지 방향으로 움직이는 쌍이 있다고 생각하면 편하다!
dx=[-1,0,1,0]
dy=[0,1,0,-1]
watch_position=2 # 북동남서 0 1 2 3, 난 현재 남쪽을 보고 있는 상황
now_stand=[0,0]

Moving_X=[0]   # X가 움직인 좌표 흔적을 저장 (처음 위치는 0인것도 넣어주자)
Moving_Y=[0]    # Y가 움직인 좌표 흔적을 저장 (처음 위치는 0인것도 넣어주자)
for M in Move:     # 문자열을 앞에서 부터 하나씩 떼어가면서 생각을 한다.
    if M=='L': #왼쪽을 보고 있는 상황
        watch_position=(watch_position-1)%4    # 0-1이면 음수가 되는 상황이 발생하므로 나머지연산자와 4를 사용
    elif M=='R':  # 오른쪽을 보고 있는 상황
        watch_position=(watch_position+1)%4
    elif M=='F':   # 전진을 하는 상황, 좌표 수정이 필요한 상황
        nx,ny = now_stand[0]+dx[watch_position], now_stand[1]+dy[watch_position]    #현재위치를 바탕으로 좌표이동을 실시 한다
        Moving_X.append(nx)    #X축 리스트에 더해주기
        Moving_Y.append(ny)    #Y축 리스트에 더해주기
        now_stand=[nx, ny]  #다시 현재 위치를 수정 한다.

#오케이 이제 이동 끝났어 그럼 좌표 설정 해줘야지
Rows_cnt = max(Moving_X)-min(Moving_X)+1
Colums_cnt = max(Moving_Y)-min(Moving_Y) +1  

ans_list = [['#']*Colums_cnt for _ in range(Rows_cnt)]    #2차원 배열 초기화  

#시작 지점 잡기
start_x = abs(min(Moving_X ))
start_y = abs(min(Moving_Y))

for x,y in zip(Moving_X, Moving_Y):
    ans_list[start_x+x][start_y+y]='.'

for k in ans_list:
    print(''.join(k))




