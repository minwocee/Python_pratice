# https://www.acmicpc.net/problem/1972

import sys

while(True):
    text = sys.stdin.readline().strip()
    if text =='*':
        exit()
    elif len(text)==1:
        print(text, 'is surprising.')
        continue
    elif len(text)==2:
        print(text, 'is surprising.')
        continue
    else:
        text_len = len(text)
        
        jump=1
        # 0 1 2
        # 0 1
        # 0
        jump=1
        
        ans = True
        for i in range(text_len-1, -1, -1):
            ck = []
            cnt = 0
            for k in range(0, i):
                ck.append(text[k]+text[k+jump])
                cnt +=1
            if len(set(ck)) == cnt:
                ans = True
            else:
                ans = False
                break
            
            jump+=1
        
        if ans:
            print(text, 'is surprising.')
        else:
            print(text, 'is NOT surprising.')
                
                
    









        
        
# 차를 움직이는 클래스 만들어 보기
# 보고있는 방향(동서남북), 움직이는 행동을 고려해서 만들어 보자
class car:
    
    def __init__(self):
        # 처음에는 북쪽을 보고 있다고 가정하자
        self.now_see = 0
        
        # 동서남북 방향으로 움직일수 있는 방향 설정
        #         북 동 남 서 방향 이동 키
        self.dx = [0,1,0,-1]
        self.dy = [1,0,-1,0]
        
        # 현재 위치는 0,0을 기준으로 한다.
        self.now_stand =[0,0]
        
        print("현재 위치: (0,0)")
        print("현자 바라보고 있는 방향(북:0 동:1 남:2 서:3 에 해당!): ", self.now_see)
        print("*********************************************************")
    
    # 움직이고 현재위치좌표를 변경하는 메서드
    def move(self):
        # 이동후 현재위치 = [(기존 위치의 x좌표 + x축 이동량), (기존 위치의 y좌표 + y축 이동량)]
        self.now_stand = [self.now_stand[0]+self.dx[self.now_see], self.now_stand[1]+self.dy[self.now_see]]
        
        
        print("이동후 현재 위치 입니다.: ", self.now_stand)
        print("*********************************************************")
    
    def change_see(self):
        self.now_see = (self.now_see+1)%4
        print("우회전 완료, 현재 보고있는 방향 (북:0 동:1 남:2 서:3 에 해당!): ", self.now_see)
        print("*********************************************************")
        
# 객체
car1 = car()

while(True):
    print("차량 이동 좌표 시뮬레이터 입니다. (1번: 악셀, 2번: 핸들돌리기 3번: 종료하기)")
    T = input("원하는 번호를 입력하세요: ")
    
    if T =='1':
        car1.move()
    elif T == '2':
        car1.change_see()
    elif T == '3':
        break
    
    
    

        
        
        
        

    