#https://www.acmicpc.net/problem/13413


# 오셀로 문제
# 방법1: 위치를 뒤바꾼.(정답의 흰검 개수를 파악하고, 초기상태랑 똑같다면 바꾸는게 유리)
# 방법2: 돌을 뒤집는다.(초기상태, 목표상태의 흰돌, 검은돌 개수가다르면 실행을 해야 한다.)

import sys
from collections import Counter

T=int(sys.stdin.readline())

# 테스트셋 실행 하기
for ____ in range(T):
    
    # 한세트 시작
    N=int(sys.stdin.readline())
    now=sys.stdin.readline().strip()
    goal=sys.stdin.readline().strip()
    
    new_now=''
    new_goal=''
    
    for n,g in zip(now,goal):    # 동시에 넣어주는 역할
        if n!=g:
            new_now+=n
            new_goal+=g
            
    King=Counter(new_now).most_common()[0][1]
    print(King)    # 태플릿으로 그림 결과, 그냥 가장 많은 바둑돌의 색상이 답이 된다.(불필요한 부분을 제거, 나는 천재인가)