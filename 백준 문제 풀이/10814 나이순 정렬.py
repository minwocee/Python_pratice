# https://www.acmicpc.net/problem/10814

# 첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)

# 3초 까지니깐 3*(10^8) 까지 시간 복잡도가 허용 된다.

# 딕셔너리를 활용 해보자~

import sys

_ = int(sys.stdin.readline())

my_dic={str(i): [] for i in range(1,201)}  # 나이: [] 순으로 딕셔너리 컴프리 헨션 진행
# 문자열: 리스트 조합으로 받아 온다.

for __ in range(_):
    age, name = map(str, sys.stdin.readline().strip().split())
    # king=my_dic[age]    # 해당 나이의 기존 리스트를 받아옴 []
    # king.append(name)    # [].append 실행
    # my_dic[age] = king   # 해당 리스트를 다시 원소로 넣어 준다.
    
    my_dic[age].append(name)    # 해당 Value를 수정 한다.
    #print(my_dic['21'])    # ['Junkyu', 'Dohyun'] 식으로 저장 되는걸 체크 완료

for i in range(1,201):
    my_arr=my_dic[str(i)]     # 키를 문자열로 했던걸 잊어버리지 말자
    if len(my_arr)>=1:     # 해당 나이대의 사람이 1명 이상 존재 하면?
        for k in range(len(my_arr)):
            print(i,my_arr[k])   # 먼저 등록한 사람 순으로 출력을 진행 하면 된다.

# 난 진짜 천재인건가? im 지니어스?
"""
가장 까다로운 점이 딕셔너리에서 Value의 자료형을 list형으로 사용을 하였다. 난 그래서 기존값에 새로운 리스트 요소를 append 하고
다시 Value를 덮어씌우는 방향으로 진행을 하려고 하는데, 그냥 Value의 리스트에 append만 해도 내가 원하는 식으로 값이 나오게 된다.
"""


""" 다른 방법 2 Heapq(우선순위 큐) 사용 해보자"""




