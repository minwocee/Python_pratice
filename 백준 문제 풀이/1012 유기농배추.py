# https://www.acmicpc.net/problem/1012

# 간단함 해쉬테이블 만들고 BFS로 풀면 됨(이때 BFS의 가동 횟수가 애벌레의 숫자임)

#해당 좌표를 모두 1로 바꿔버리는 행동을 한다.(입력받은x, 입력받은y, 현재 딕셔너리상태)
def BFS(x,y,Field,width, height):
    Frontier=[]
    Frontier.append((x,y))
    
    X=width
    Y=height #세로길이
    
    while(len(Frontier)!=0):
        
        Po=Frontier.pop() #튜플형태
        Field[Po[0],Po[1]] = False
        
        # 상하좌우
        Make=[]
        Make.append((Po[0]-1,Po[1]))
        Make.append((Po[0]+1,Po[1]))
        Make.append((Po[0],Po[1]+1))
        Make.append((Po[0],Po[1]-1))
        
        for k in Make:
            #유효한 경우
            if (0<= k[0] <X) and (0<= k[1]<Y) and Field[k[0],k[1]] :
                Frontier.append((k[0],k[1]))
                
    return Field
                
        
    
import sys

T=int(sys.stdin.readline())

# 테스트 케이스의 길이 만큼 입력을 받는다.
for _ in range(T):
    # 가로, 세로, 배추개수 입력 받음
    width, height, bachu_cnt = map(int, sys.stdin.readline().split())
    
    #True면 검사해야하는 배추, False면 검사 안해도 되는 일반 땅임
    Field={}
    for x in range(width):
        for y in range(height):
            Field[(x,y)]=False
    
    #이제 흰배추 좌표 입력 받음
    for _ in range(bachu_cnt):
        x,y=map(int, sys.stdin.readline().split())
        Field[(x,y)]=True
    
    ans_cnt=0
    # 이제 BFS를 돌려서 해당 좌표가 True면 연속제거와 카운터를 증가 시킨다.
    for x in range(width):
        for y in range(height):
            
            # BFS검사해야하는 경우
            if Field[(x,y)]==True:
                ans_cnt+=1
                Field=BFS(x,y,Field,width,height)
    
    print(ans_cnt)        