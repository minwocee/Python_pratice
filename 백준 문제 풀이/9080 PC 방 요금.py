# PC방 요금을 계산하여야함

"""
모르겟음 나중에 연구 해야 됨
"""


# 특이사항 1번   1시간에 1000원 부과 (60분, 1분이라도 넘으면 1000원이 추가 결정됨)
#
#  특이사항 2번   22~08시 까지는 5000원만 내면 자유 이용권처럼 사용이 가능 
#  야간권은 선택사항임
#  (단 22~03시 사에에 결제해야 이득봄 03시부터는 야간권 끊어도 이득 없음)


# 특이사항 3번   야간 이용권이 끝나면 바로 일반 사용료 부과됨 21:59~08:01 사용시 1000+5000+1000=7000원 나감



'''
4           #테스트셋 개수
14:30 180   #시작 시간(나중에 모두 분으로 계산하자) , 사용할 시간(최대 4320)
19:28 242   #시작 시간(나중에 모두 분으로 계산하자) , 사용할 시간(최대 4320)
23:25 580   #시작 시간(나중에 모두 분으로 계산하자) , 사용할 시간(최대 4320)
21:10 765   #시작 시간(나중에 모두 분으로 계산하자) , 사용할 시간(최대 4320)
'''

#참고 22:00~08:00을 분으로 나타내면 1320~1440 과 0~480이다 이 주

# 하루는1440분이다, 4320분 까지만 고려
# 신경써야할 부분 1320~1920, 2760~3360, 4200~4800

import sys

T=int(sys.stdin.readline().strip())

for _ in range(T):
    Timer, stay=map(str, sys.stdin.readline().strip().split())
    
    Timer=int(Timer.split(":")[0])*60+int(Timer.split(":")[1]) #시간변환 완료
    stay=int(stay)  #있어야 하는 시간 변환 완료

    #여기까지는 정상적으로 변환을 완료함
    #night_start=[1320~1440]    #야간타임 시작 
    #night_end=[0~480]    #야간타임 끝     야간은 총 600분을 차지,결제시 이전 사용시간 없애고 새로 갱신함
    
    #"""
    #핵심포인트: 야간을 어떻게 대처할것인가
    #포인트1 야간에 겹치는 시간이 5시간 아래면 할필요 없음
    #포인트2 야간에 겹치는 시간이 5시간 이상이면 야간권을 신청하는게 좋다
    #"""
    #0~1440을 기준으로 판별 
    #24시간을 기준으로 작성해보자
    pay_money=0
    while(stay>0):
        if  stay>=300 :
            if Timer>=1320 or Timer<=180:
                pay_money+=5000
                
                if Timer>=1320:
                    stay-=(1440-Timer+480) 
                else:
                    stay-=480-Timer   
                Timer=480
        if stay>0:
            stay-=60
            pay_money+=1000
            Timer= (Timer+60)%1440
        

    print(pay_money)






















