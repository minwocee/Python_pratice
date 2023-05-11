# import sys

# T = int(sys.stdin.readline())    # 문제의 개수
# winner = 0    #처음에는 이기고 있는 팀이 없음
# A = 0    # 에이팀 현재 스코오
# B = 0   # 비팀 현재 스코어 

# A_time = 0    # 에이팀 이기고 있는 시간  결과물임
# B_time = 0    # 비팀 이기고 있는 시간    결과물임
# 득점시간 = 0

# def time(text):    # 문자열을 시간으로 변환해주는 역할
#     asnwer = int(text.split(':')[0])*60 + int(text.split(":")[1])
#     return asnwer

# for i in range(T):    #문에의 개수만큼 반복을 시작한다.
#     # 끝에 도달했을때 해주는 예외 처리
#     if i == T-1:
#         # 1팀이 게임에서 승리할때
#         if winner == 1:
#             A_time += 2880 - 마지막으로 기록된 1팀의 최초 득점 시간
#         elif winner ==2:
#             B_time+= 2880 - 마지막으로 기록된 2팀의 최초 득점 시간
        
        
#         # 이제 점수 프린트 하고 끝내면 됨(시계 시간 변환 하기)
#         print(A_time)
#         print(B_time)
#         exit()
    
#     # 한줄씩 입력을 받는다.  list 현태로 남는다.[1 , 10:10]
#     k = sys.stdin.readline().strip().split()
    
#     if k[0] == 1:
#         A +=1
#     else:
#         B +=1
        
#     # 이제 누가 이기는지, 비기는지 체크를 한다.
#     if A>B:
#         # 0에서 1로 바뀐 경우 기록을한다.
#         if winner ==0:
#             starttime = k[1]
#         winner = 1
        
#     elif A<B:
#         # 0에서 2로 바뀐 경우 기록을한다.
#         if winner ==0:
#             srarttime = k[1]
#         winner =2
    
#     # 둘이 같아지
#     elif A == B :
#         winner


for i in range(N):
    teamNo, timeStr = input().split()
    scoreDict[timeToNum(timeStr)] = int(teamNo)

teamWinTime1 = 0 # 1번 팀이 이기고 있던 시간
teamWinTime2 = 0 # 2번 팀이 이기고 있던 시간
teamScore1 = 0 # 현재 1번 팀 점수
teamScore2 = 0 # 현재 2번 팀 점수
for i in range(0, timeToNum("48:00")): # 매 초마다 승자를 체크한다.
    if i in scoreDict:
        if scoreDict[i] == 1:
            teamScore1 += 1
        else:
            teamScore2 += 1
   
    if teamScore1 > teamScore2:
        teamWinTime1 += 1
    elif teamScore1 < teamScore2:
        teamWinTime2 += 1
        
print(numToTime(teamWinTime1))
print(numToTime(teamWinTime2))
        
            