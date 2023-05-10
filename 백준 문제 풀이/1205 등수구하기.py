# https://www.acmicpc.net/problem/1205


'''
0<my_score<2,000,000,000
10 <= N(선수머리수) <= P(랭킹등록제한) <= 50
'''

import sys
N, my_score, P=map(int, sys.stdin.readline().split())

if N==0:    #나말고 다른선수가 없으면
    print(1)
    exit(0)

#경쟁 선수가 1명 이상 존재 하면
ranking_table=list(map(int,sys.stdin.readline().split()))


cnt=1
Samescore_cnt=0 #동점자 세주는 역할
# 등수 매기기 시작함
for i in ranking_table:    #경쟁자들을 하나씩 꺼내서 내 등수가 하락하는걸 구경
    if i>my_score:    #나보다 잘하면
        cnt+=1
    else:    #나보다 같거나 못하면
        if i==my_score:
            Samescore_cnt+=1

    
if cnt+Samescore_cnt >P:
    print(-1)
else:
    print(cnt)




