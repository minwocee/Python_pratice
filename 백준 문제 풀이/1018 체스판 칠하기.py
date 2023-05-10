# # https://www.acmicpc.net/problem/1018
# # N: 행개수 M: 열개수
# # 8<= N,M <=50 의 자연수이다.
# # 체스판 왼쪽상단이 Black 혹은 White로 BWBWBWBW ,WBWBWBWB 이렇게 완성이된다. 
# # 이때 흰검흰검 조합을 맞추기 위해서 몇개를 수정해야 하는가가 문제의 핵심이다.

# # 조건 1.행열의 개수에 맞게 자르기
# # 조건 2. 자른 타일들을 몇개를 칠해야 하는지 검사를 실행 

# """
# <예제 입력1> 
# 8 8
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBBBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW

# <예제 출력1> 
# 1
# """

# import sys

# Rows, Colums=map(int, sys.stdin.readline().split())     #행의개수, 열의개수가 입력된다.

# # 첫행을 읽고 패턴을 파악한뒤 틀린것의 개수를 파악을 한다. 아주 간단한 문제이다.

# Table=[sys.stdin.readline().strip() for _ in range(Rows)]


# def make_answerlist_B(Colums):
#     ans_list=''
#     for i in range(Colums):
#         if i%2==0:
#             ans_list+='B'
#         elif i%2==1:
#             ans_list+='W'
#     return ans_list

# def make_answerlist_W(Colums):
#     ans_list=''
#     for i in range(Colums):
#         if i%2==0:
#             ans_list+='W'
#         elif i%2==1:
#             ans_list+='B'
#     return ans_list




# if Table[0][0]=='W': #시작이 W이면 WBWBWBW... 형태로 나와야 한다.
#     Odd_answer=make_answerlist_W(Colums)    #1,3,5,7 번째 행의 정답본을 만든다.
#     Even_answer=make_answerlist_B(Colums)     #1,3,5,7 번째 행의 정답본을 만든다.
#     Test_table=[]
#     counter=0    #오타 개수 세는 용도
    
#     for i in range(0,Rows,2):    #Odd_answer리스트와 추후 비교를 할것이다.
#         Test_table.append(Table[i])    #1,3,5,7 번째 행의 정보가 들어가게 된다.

#     for case in Test_table:    #홀수차항 계산 완료
#         for i in range(Colums):
#             if case[i]!=Odd_answer[i]:
#                 counter+=1

#     Test_table=[]

#     for i in range(1,Rows,2):    #Even_answer리스트와 추후 비교를 할것이다.
#         Test_table.append(Table[i])    #2,4,6,8 번째 행의 정보가 들어가게 된다.

#     for case in Test_table:    #홀수차항 계산 완료
#         for i in range(Colums):
#             if case[i]!=Even_answer[i]:
#                 counter+=1
    
#     print(counter)

# elif Table[0][0]=='B':
#     Odd_answer=make_answerlist_B(Colums)    #1,3,5,7 번째 행의 정답본을 만든다.
#     Even_answer=make_answerlist_W(Colums)     #1,3,5,7 번째 행의 정답본을 만든다.
#     Test_table=[]
#     counter=0    #오타 개수 세는 용도
    
#     for i in range(0,Rows,2):    #Odd_answer리스트와 추후 비교를 할것이다.
#         Test_table.append(Table[i])    #1,3,5,7 번째 행의 정보가 들어가게 된다.

#     for case in Test_table:    #홀수차항 계산 완료
#         for i in range(Colums):
#             if case[i]!=Odd_answer[i]:
#                 counter+=1

#     Test_table=[]

#     for i in range(1,Rows,2):    #Even_answer리스트와 추후 비교를 할것이다.
#         Test_table.append(Table[i])    #2,4,6,8 번째 행의 정보가 들어가게 된다.

#     for case in Test_table:    #홀수차항 계산 완료
#         for i in range(Colums):
#             if case[i]!=Even_answer[i]:
#                 counter+=1
    
#     print(counter)

import sys

N, M = map(int, sys.stdin.readline().split())
original = []
count = []     #여러개의 경우의수를 모드 계샌해야하기떄문에 배열의 형태롤 저장하자

for _ in range(N):
    original.append(sys.stdin.readline().strip())

for a in range(N-7):      #8*8체스판을 만들어야 하므로 자르는 기준이 판을 초과하지 않게 -7을 해줘서 모든 경우의수를 탐색하도록 한다
    for b in range(M-7):     #a는 행의정모 b는 열의정보를 다룰때 사용하낟.
        index1 = 0
        index2 = 0
        for i in range(a, a+8):      #a~a+7까지 탐색
            for j in range(b, b+8):     #b~b+7까지 탐색
                if (i+j) % 2 == 0:      # *핵심* 체스판 형식처럼 한칸 흰색 한칸 검은색의 반복이기 때문(0,0) (0,2) (0,4) (0,6) 
                    if original[i][j] != 'W':     #해당칸이 흰색이 아니면? 카운터증가
                        index1 += 1
                    if original[i][j] != 'B':     #해당칸이 검은색이 아니면? 카운터증가
                        index2 += 1
                else:
                    if original[i][j] != 'B':     #0X0X0X0X에서 X번째 칸들의 검사를 여기서 진행한다.
                        index1 += 1
                    if original[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))      #이떄 해당좌표에서 B를 스타트로잡는경우, W를 스타트로 잡는경우 2가지 방법중 가장 작은값을 후보리스트에 넣는다.

print(min(count))     #이후 가장 적게나오는 경우의수를 출력을 진행한다.




















