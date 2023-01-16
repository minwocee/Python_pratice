# 민지가 말한 유클리드 호제법 써보자
import sys


N, M= map(int, sys.stdin.readline().split())  # 풍선개수, 공격횟수

풍선위치 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]   #x ,y 체력

공격로그 = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]   #x y 데미지

# print(풍선위치) #[[1, 1, 3], [3, 3, 4], [2, 2, 2]]
# print(공격로그) #[[1, 1, 3]

# 이때 남은 풍선을 구하여라
# x,y의 좌표는 배수임 (1 1) (2 2) (3 3)       (1,3)  (2,6) (3,9)이런식으로 됨...

# 공격 로그에 대한 직선의 방정식을 구하고, 풍선 위치가 해당 기울기와 같다면 생명력을 낮추면됨


for i in range(M):
    try:
        if 공격로그[i][1]==0 or 공격로그[i][0]==0:    # 공격로그의 두좌표중 하나에 0이 들어가면, 
            
            for p in 풍선위치:
                if p[1]==0 and 공격로그[i][1]==0:
                    p[2]-=공격로그[i][2]
                    
                    continue
                elif p[0]==0 and 공격로그[i][0]==0:
                    p[2]-=공격로그[i][2]
                    
                    continue
        
        else:
            #제로 디비전 오류 해결하기
        
        
            # 나중에 기울기를 (튜플1,공격 ) (튜플2 풍선) 식으로 만들어서 나머지 연산했을떄, x y가 모두 0이면 같은 기울기를 가졌다고 보면 될것같아.
            기울기 = 공격로그[i][1]/공격로그[i][0]
            
            
            
            for k in 풍선위치:
                풍선기울기=k[1]/k[0]
                
                if 기울기 == 풍선기울기:
                    k[2]-=공격로그[i][2]      
    except ZeroDivisionError:
        continue
    


#print(풍선위치, '현재 풍선 상황')

cnt=0
for i in 풍선위치:
    if i[2]>0:
        cnt+=1

print(cnt)
