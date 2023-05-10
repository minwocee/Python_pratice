# https://www.acmicpc.net/problem/7568

# 덩치가 크다: 몸무게와 키가 상대방 보다 완전한 우선순위임을 의미 이를 활용해 등수를 구하는 문제이다
# 1등 2등 2등 2등 5등 처럼 키가 커도 몸무게가 작으면 공동 순위로 생각을 한다.
# 2 ≤ N ≤ 50
# 10 ≤ x ≤ 200   (몸무게)
# 10 ≤ y ≤ 200   (키)

"""
예제 입력1
5
55 185
58 183
88 186
60 175
46 155

예제 출력1
2 2 1 2 5
"""











"""
만약 if 몸무게 > 라이벌 and 키> 라이벌:
    go up
    elif 몸무게 < 라이벌 and 키 < 라이벌:
    go down
    else     #몸무게나 키가 둘중에 하나는 상대보다 높아서 비교하기가 애매한 경우를 의미한다.
        same ranking 유지

#일단 여기까지 구현이라고 한번 해보자

출력할때는 same ranking은 동점자로 표기를 한다. 어떻게 하면 좋을까
순위를 정하는건 리스트를 만들어서 할까 아니면 딕셔너리로 풀까 고민을 좀 해보자
"""


#택원의 팁 rank=1로 모두 설정을 하고 (몸무게, 키) 둘다 낮으면 등수를 1 올리는 구조를 선택한다.

# 하나하나씩 전부 비교를 시작해보자

# rank=[1]*N

# for i in range(N):
#     ranking=1
#     for K in range(i,N-1):
#         if (Table[i][0] < Table[i+1][0]) and (Table[i+1][1] < Table[i+1][1]):
#             ranking+=1
#             rank[i]+=1

# print(rank)


# 다른분의 블로그 풀이

import sys

N= int(sys.stdin.readline())     # 몇명 넣을지 결정

Table=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]  # 테이블 입력받고 만드는 과정(리스트 컴프리헨션 사용)


for me in Table:     # i=[55 158], [58 183] 이렇게 결국 들어가게 된다. 
    rank = 1     # 일단 기본적으로 1등으로 시작하고 조건 비교후 1씩 등수 증가를 시킨다
    for rival in Table:
        if me[0] < rival[0] and me[1] < rival[1]:    #상대방보다 몸무게, 키가 완전히작으면 않좋은것
                rank += 1    #랭킹 하락
    print(rank, end = " ")    #모든 사람과의 비교가 끝나고 랭킹을 출력한다.
