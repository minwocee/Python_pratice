# my_dic={}

# for _ in range(10):
#     my_dic[str(_)]=_


# print(list(my_dic.items())[0])

import sys
from collections import Counter

N=int(sys.stdin.readline())

Table=[int(sys.stdin.readline()) for _ in range(N)]
Table.sort()

tmp=Counter(Table)    # 딕셔너리 형태로 {숫자: 등장횟수} 형태로 저장# Counter({-2: 1, 1: 1, 2: 1, 3: 1, 8: 1})

ans_list=tmp.most_common()    
# 가장 많은 개수의수(최빈값)을 ans_list에 (숫자, 등장횟수) 형태로 넣어주는 역할(등장횟수가 가장 큰순서대로 들어간다)
# 많이 등장하는게 가장 먼저 들어감

# (숫자, 등장횟수) 튜플 형태로 저장함
if len(ans_list)>=2:
    if ans_list[0][1]==ans_list[1][1]:    # 최빈값 동점자가 2명 이상 존재하는 경우
        print(ans_list[1][0])     # (숫자, 등장횟수) 중에서 숫자 부분을 출력한다.
    else:
        print(ans_list[0][0])    # 첫번째 최빈값 숫자 출력
else:    # 한칸짜리 숫자
    print(ans_list[0][0])    #첫번쨰 최빈값 숫자 출력


