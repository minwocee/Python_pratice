# # https://www.acmicpc.net/problem/18221

# """
# 강의실에는 가로로 N 행, 세로로 N 열, 총 N × N 개의 책상이 있으며, 위쪽에서부터 R 번째 행, 
# 왼쪽에서부터 C 번째 열에 있는 책상의 위치를 (R, C)로 표현한다. 각 책상 자리는 비어있거나, 
# 성규가 아닌 학생 혹은 성규가 앉아있거나, 교수님이 위치해 있다.

# 도망가는 데 성공하려면, 성규와 교수님의 거리가 5 이상이면서, 교수님과 성규를 꼭짓점으로 하는 축에 평행한 직사각형 안에, 
# 교수님을 제지해줄 성규가 아닌 학생이 세 명 이상 있어야 한다.

# 단, 교수님과 성규가 같은 행 혹은 같은 열의 책상에 앉아있다면 
# 교수님과 성규를 잇는 선분 상에 성규가 아닌 학생이 세 명 이상 있어야 한다.

# 이때, 책상 (a, b)와 책상 (c, d) 간의 거리는 $\sqrt{(a-c)^2 + (b-d)^2}$로 정의한다.  #피타고라스의 정리

# 성규는 도망가다가 잡히는 것이 최악이라 판단되어, 도망갈 수가 없는 환경이면 
# 순순히 대학원생의 길로 들어서려고 한다. 이런 성규를 위해 확실히 도망갈 수 있는지 알려주는 프로그램을 작성하자.
# """

# """
# <입력>
# 입력의 첫 번째 줄에 자연수 N(7 ≤ N ≤ 1,000) 이 주어진다.

# 두 번째 줄부터 N개의 각 줄에 0, 1, 2, 5 중 하나의 숫자가 공백으로 구분되어 N개씩 주어진다.

# N개의 줄 중 R번째 줄의 C번째 숫자가 d라는 것은 다음과 같은 의미를 가진다:

# d = 0: 책상 (R, C)는 빈 자리이다.
# d = 1: 책상 (R, C)는 성규가 아닌 학생이 앉아있다.
# d = 2: 책상 (R, C)는 성규가 앉아있다.
# d = 5: 책상 (R, C)는 교수님이 앉아있다.
# 성규와 교수님은 겹치지 않으며, 각각 정확히 한 자리에만 앉아있다.

# """

# # 0 빈자리 1다른학생 2성규 5교수님
# # 도망성공조건: 1. 거리가 5이상(피타고라스 정리 활용) and 다른학생이 3명이상 있어야 한다.

# import sys

# 정사각형=int(sys.stdin.readline())

# mlist=[list(map(str, sys.stdin.readline().strip().split())) for _ in range(정사각형)]

# # for _ in mlist:
# #     print(_)
# '''
# [['0', '5', '0', '0', '0', '0', '0']]
# [['0', '0', '1', '0', '0', '0', '0']]
# [['0', '0', '0', '0', '0', '0', '0']]
# [['0', '0', '0', '1', '1', '0', '0']]
# [['0', '0', '0', '0', '0', '2', '0']]
# [['0', '0', '0', '0', '0', '0', '0']]
# [['0', '0', '0', '0', '0', '0', '0']]
# '''

# # 이제 교수님과 민우 간의 리스트 슬라이싱을 활용해서 계산하기 용이하게 해보자

# # 가로: 교수님 X좌표 ~ 민우 X좌표
# # 세로: 교수님 Y좌표 ~ 민우 Y좌표
# king=0
# cnt=0 #전체 관점
# for _ in mlist:    #2차원 리스트 내용물 들어감
#     #print(_)
#     if '5' in _:
#         king=(_.index('5'),cnt) #튜플 형태로 좌표 전달 (x,y)
#         break 
#     cnt+=1


# slave=0
# cnt=0 #전체 관점
# for _ in mlist:    #2차원 리스트 내용물 들어감
#     if '2' in _:
#         slave=(_.index('2'),cnt) #튜플 형태로 좌표 전달 (x,y)
#         break 
#     cnt+=1

# #시작점은 (0.0)을 기준으로 한다.
# #print(king, slave)    #(1, 0) (5, 4)

# # 왼쪽 위에 있는게 무엇인지 알아야 하고
# # 오른쪽 아래에 있는게 무엇인지 알아야 한다.
# # 우선 가로로 슬라이싱을 먼저 해보자
# """불필요한 행자르기 시전"""
# top=max(king[0],slave[0])   # 둘중에 더 큰게 오른쪽
# bottom = min(king[0], slave[0])    # 둘중에 더 작은게 왼쪽

# mlist2=[absol[bottom:top+1] for absol in mlist]

# for _ in mlist2:
#     print(_)
# """불필요한열 자르기 시전"""
# top=max(king[1],slave[1])   # 둘중에 더 큰게 밑줄에 존재
# bottom = min(king[1], slave[1])    # 둘중에 더 작은게 윗줄에 존재


# cnt=list(range(bottom,top+1))
# #print(cnt)

# temp=0

# ans=[]
# for _ in mlist2:
#     if temp in cnt:
#         ans.append(_)
#     temp+=1

# for _ in ans:
#     print(_)

# '''현재 ans에는 자르기 완료한 깔끔한 상태가 되었다.'''
# # 이제 거리가 5 이상인지 점검을 실시해보자



# if (len(ans[0])**2 + len(ans)**2)<25:    #두사람의 거리가 5 이하이면 
#     print(0, "거리가 딸립니다.")    #실패를 출력
# else:     #거리가 5이상은 충족함, 그럼 이들 사이에 1의 개수가 3개 이상인지 검사를 실행
#     cnt1=0    # 다른학생들의 개수를 세는 변수
#     for _ in ans:
#         for i in _:
#             if i=='1':
#                 cnt1+=1
#                 if cnt1>=3:
#                     print(1)
#                     break
        

# if cnt1<3:
#     #print(0, '지켜줄 친구들이 없습니다.')
#     print(0)


"""
문제 풀이는 괜찮았지만 마지막 부분에서 거리의 개념과, 출력이 0 0 두번나오는 문제가 발생하는등 완벽하지 못하였다.
좀더 꼼꼼히 문제를 보도록 하자
"""


import sys

정사각형=int(sys.stdin.readline())

mlist=[list(map(str, sys.stdin.readline().strip().split())) for _ in range(정사각형)]


king=0
cnt=0 #전체 관점
for _ in mlist:    #2차원 리스트 내용물 들어감
    #print(_)
    if '5' in _:
        king=(_.index('5'),cnt) #튜플 형태로 좌표 전달 (x,y)
        break 
    cnt+=1


slave=0
cnt=0 #전체 관점
for _ in mlist:    #2차원 리스트 내용물 들어감
    if '2' in _:
        slave=(_.index('2'),cnt) #튜플 형태로 좌표 전달 (x,y)
        break 
    cnt+=1

"""불필요한 행자르기 시전"""
top=max(king[0],slave[0])   # 둘중에 더 큰게 오른쪽
bottom = min(king[0], slave[0])    # 둘중에 더 작은게 왼쪽

mlist2=[absol[bottom:top+1] for absol in mlist]

"""불필요한열 자르기 시전"""
top=max(king[1],slave[1])   # 둘중에 더 큰게 밑줄에 존재
bottom = min(king[1], slave[1])    # 둘중에 더 작은게 윗줄에 존재


cnt=list(range(bottom,top+1))
#print(cnt)

temp=0

ans=[]
for _ in mlist2:
    if temp in cnt:
        ans.append(_)
    temp+=1



'''현재 ans에는 자르기 완료한 깔끔한 상태가 되었다.'''
# for _ in ans:    # 2차원
#     print(_)


# 이제 거리가 5 이상인지 점검을 실시해보자

"""
1.
0***0
0****0   #이 개념으로 거리를 구하는게 맞다
0*****0
"""

cnt1=0
if ((len(ans[0])-1)**2 + (len(ans)-1)**2)<25:    #두사람의 거리가 5 이하이면 *중요* 위의 개념을 인지 하자 , 인덱스 번호와 len의 차이 
    print(0)
    exit(0)
    
else:     #거리가 5이상은 충족함, 그럼 이들 사이에 1의 개수가 3개 이상인지 검사를 실행
    # 다른학생들의 개수를 세는 변수
    for _ in ans:
        for i in _:
            if i=='1':
                cnt1+=1
                if cnt1>=3:
                    print(1)
                    exit(0)    #강제 종료
                
        
if cnt1<3:
    print(0)



















