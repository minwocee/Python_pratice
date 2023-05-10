# https://www.acmicpc.net/problem/1874

"""
문제 핵심 
8

4
3
6
8
7
5
2
1 

+1 +2 +3 +4 (-4) (-3) +3 +4 +5 +6 (-6) +6 +7 +8 (-8) (-7) (-5) (-2) (-1)

이면 위에서 부터 출력값이 내가 원하는 대로 나와야 한다.

5

1
2
5
3
4

+ - ++-++++-(문제 발생)
+ 푸시 - 팝

이면 No 이지만 3과 4를 바꿔 주면 ok이다.
"""

import sys

N=int(sys.stdin.readline())

Table=[int(sys.stdin.readline()) for _ in range(N)]

# 1. 스택 체크
# 2. +- 활용 구현하기

Top=0

mlist=[]
ans=''
for table in Table:
    
    if Top <= table:    # Table안의 요소 하나에 따라 실행된다.
        for _ in range(table-Top):    # 핵심 코드 이다.
            ans+='+'
            Top +=1 #Top 최신화
            mlist.append(Top) 
    
    if mlist[-1]==table:    # 마지막 요소가 i랑 일치 하면 실행(인덱스랑 요소 비교)
        ans+='-'
        mlist.pop()
    else:    #추가된 요소가 일치하지 않으면, 정지한다.
        print('NO')
        exit(0)
                                                                      
for _ in ans:    # 만약 NO가 없이 정상적으로 실행되었다면, 받아둔 +-를 출력해준다.
    print(_)