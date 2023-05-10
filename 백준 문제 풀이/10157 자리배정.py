# https://www.acmicpc.net/problem/10157

'''
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
counter=1

# 1. 만약 해당 방의 넘버가 1이면 방향을 꺾는다.
# 2. 만약 해당 방의 넘버가 0이면 현재위치 직진, 1로 마킹, 보는 시점은 그대로 유지
# 3. 만약 카운터가 W*H가 끝나면 반복을 중지한다.


num_dic={}

# Field는 2차원 배열이 맞다.

while(True):
    try:
        if Field[now_number[0]][now_number[1]]==0:   # 만약 해당방이 아직 지나가지 않은 방이면 -> 마킹을 한다.
            Field[now_number[0]][now_number[1]]=1   # 해당 방은 지나왔다고 생각한다.
            num_dic[counter]=[now_number[0],now_number[1]]    # 딕셔너리에 순서:[x,y] 좌표 꼴로 저장을 한다\
            counter+=1
            if counter>W*H:
                break
            now_number=[now_number[0]+dx[now_watch], now_number[1]+dy[now_watch]]    # 현재 위치를 수정한다.
            print(now_number)
            
        elif Field[now_number[0]][now_number[1]]==1:    # 만약 해당 방을 이미 지나갔었다면 오른쪽으로 회전한다,
            now_watch=(now_watch+1)%4      # 모듈러 연산을 실행한다.
            # now_number=[now_number[0]+dx[now_watch], now_number[1]+dy[now_watch]]    # 현재 위치를 수정한다.
                
    # 리스트의 범위를 벗어나면 실행한다.(외곽 밖으로 벗어나면 오른쪽으로 방향을 틀어줘야 한다.)
    except IndexError:
        now_watch=(now_watch+1)%4      # 모듈러 연산을 실행한다.
        print(now_number, '리스트 범위 벗어남')
        
        
        
print(num_dic)# 딕셔너리를 출력한다.
'''    
            
# 문제를 풀다 기가막힌 생각이 떠올랐다. 테두리를 전부 1로 초기화를 하고 애벌레가 사과먹는 게임 하는것처럼 1(막히면)오른쪽 회전하고 직진
# 테두리를 설정해주는게 핵심 (+2 해주면 된다.)
# 그리고 지나온 영역에 부딫히면? 왓던길 한칸 뺵 -> 우회전 -> 전진 

import sys

W,H=map(int, sys.stdin.readline().split())    #가로 세로 입력
Where=int(sys.stdin.readline())    # 찾고자하는 몇번째 손님인지?

Field=[[0]*(W+2) for _ in range(H+2)]


if W*H<Where:
    print(0)
    exit(0)

# 이제 테두리 부분을 1로 초기화 해준다.

# 밑과 위를 1로 초기화
Field[0]=[1]*(W+2)
Field[-1]=[1]*(W+2)

# 왼쪽, 오른쪽을 1로 초기화하기
for i in range(H+2):
    Field[i][0]=1
    Field[i][-1]=1
    
'''
for _ in Field:
    print(_)
'''

# 환경설정
now_see=0
now_point=[1,1]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
dic_counter=1
dic_ans={} 

while(True):
    x=now_point[0]
    y=now_point[1]
    if Field[y][x]==0:
        dic_ans[dic_counter]=[x,y]
        now_point[0]=x+dx[now_see]
        now_point[1]=y+dy[now_see]
        dic_counter+=1
        
        Field[y][x]=dic_counter
        
        if dic_counter>W*H or dic_counter==Where+1:
            break
        #print(now_point, '현재위치(양호)')
        dic_ans[dic_counter-1]=[x,y]
        
        
    elif Field[y][x]!=0: #벽에 막히면?
        #한칸 뒤로 뺸다.
        #now_point[0]=x-dx[now_see]
        x=x-dx[now_see]
        #now_point[1]=y-dy[now_see]
        y=y-dy[now_see]
        
        #오른쪽으로 방향 틀기
        now_see=(now_see+1)%4
        
        #이후 한칸 전진
        now_point[0]=x+dx[now_see]
        now_point[1]=y+dy[now_see]
        Field[y][x]=dic_counter
        
        #print(now_point, '현재위치(막힘)')
        dic_ans[dic_counter-1]=[x,y]
        
        
#print(dic_ans[Where])

'''
for _ in Field:
    print(_)
'''

#print(Field[3][4], '42번째 답')
print(dic_ans[Where][0], dic_ans[Where][1])