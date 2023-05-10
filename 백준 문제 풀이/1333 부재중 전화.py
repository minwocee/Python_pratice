# https://www.acmicpc.net/problem/1333

#첫째 줄에 세 정수 N, L, D가 공백을 사이에 두고 주어진다.

'''
import sys

노래개수,노래길이,벨울리는텀=map(int, sys.stdin.readline().split())    #노래개수, 노래길이, 벨울리는 텀

# 어차파 답은 D(벨 울리는 텀)의 배수임

# 노래와 노래 사이에는 5초간의 공백이 존재함(이때 벨이 울리면 전화받기 가능, 4회는 가능함)

# True=노래 재생중
# False= 쉬는 시간

#Table=[True]+([True]*L+[False]*4)+[False]*1000000
Table=[False]



for _ in range(노래개수):
    Table+=[False]*노래길이
    Table+=[True]*3


Table+=[True]*100
#True가 쉬는시간

# 1,2,3,4,5,6,7,8  
# (9 10 11 12 ) 13,14,15,16,17,18,19,20
# (21 22 23 24)  



print(Table)
print(Table[39],Table[40],Table[41])

ans=[i for i in range(벨울리는텀,100,벨울리는텀)]


print(ans)
    
for i in ans:
    if Table[i]:
        print(i)
        break
'''



# 다른분의 코드를 참고해보자

import sys

N, L, D = map(int, sys.stdin.readline().split())#개수 러닝타임, 벨간격



total = N*L+(N-1) * 5 # 앨범의 총 길이
song = [False]*total # 총 길이를 고려해서 False로 전체 초기화

# 6 9 20 을 예시로 사용해보자
for i in range(0, total, L + 5): # 각 노래는 0 초부터 시작해서 L + 5 초마다 나온다. #0,14,28...(노래의 시작점clk)
    for j in range(i, i + L): #노래가 재생중인 지점(점! 이라는게 중요)
        # 시작하는 부분 i부터 노래가 끝나는 부분인 i + L 전까지 체크 
        # (0,9), 0,1,2,3,4,5,6,7,8  ,14,15,16,17,18,19
        song[j]=True    #노래재생중



for i in range(0, total, D): # 0초부터 D초마다 노래가 나오는지 체크 #벨소리는 논리회로의 clk 신호처럼 순간만 체크하면됨
    if not song[i]:#트루(빈 시간이 맞으면) 이면 실행
        print(i)
        exit(0)


print(i + D)#힌번도 실행되지 않으면(앨범의 재생기간동안 울리지 못하는 경우)


"""start<= Now < End 이 개념임, 끝나는 clk에는 전화 받기 가능"""


