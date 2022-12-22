












































# import sys

# N, K = map(int, sys.stdin.readline().strip().split())    # 사람수, 사거리가 들어감

# Table=sys.stdin.readline().strip()    
# #H (H P) (H P) (P H) (H P) P (H P) P P (H P) (H P) (H P)  총 8명이 식사 가능!
# # H H H (H H P P) P P (P H) (P H) (P H) (P H) H (H P)
# # 매칭의 기준을 햄버거를 잡는게 좋을듯 하다 (조건1: 한사람당 1개의 햄버거를 먹어 치운다.)


# n, k = map(int, input().split())     #사람수와 사거리 들어간다
# placement = list(input())      #입력받은 문자열을 리스트화해서 placement 변수에 넣어준다
# ans = 0
# for idx in range(n):     #테이블의 길이 만큼 반복문을 실행 (idx변수)
#     if placement[idx] == 'P':     #만약 Table 에서의 해당 요소가 P(사람) 이면 실행됨
#         for i in range(max(idx-k, 0), min(idx+k+1, n)):     # max와 min을 사용하는 이유: 첫요소의 왼쪽 벗어남 방지,  끝 요소의 오른쪽 벗어남 방지
#             if placement[i] == 'H':    #만약 햄버거가 사거리 내에 존재한다?
#                 placement[i] = 0      # 먹어치우고 정수 0으로 변경함 (겹치는 현상을 막기 위해서)
#                 ans += 1    # 카운터에 1을 증가시키고 
#                 break     #idx반복문으로 다시 돌아간다
# print(ans)

# '''
# HHPHP에 사거리가 1인 경우
# for i in range()
# '''



# PHPH H PH  그리디 알고리즘 익히기 
import sys

N, K =map(int,sys.stdin.readline().split())
Table=list(sys.stdin.readline().strip())   

eat_counter=0

for i in range(N):
    if Table[i]=='P':
        for Q in range(max((i-K),0), min((i+K+1),N),-1):    #가장 많이 먹어야 하기 떄문에 왼쪽에서 부터 먹는다는점을 기억
            if Table[Q]=='H':
                Table[Q]=-1
                eat_counter+=1
                break

print(eat_counter)




























