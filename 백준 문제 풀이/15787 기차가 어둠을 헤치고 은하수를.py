# https://www.acmicpc.net/problem/15787



''' 
맨 앞이 1 사람 추가  (사람추가, 기차번호, N번째)
맨 앞이 2 사람 제거  (시림제거, 기차번호, N번째)
맨 앞이 3 모든 사람들 뒤로   (모든사람 한칸씩 뒤로, 기차번호)
맨 앞이 4 모든 사람들 앞으로  (모든사람 한칸씩 앞으로, 기차번호)
'''


import sys
from collections import deque

N, M=map(int,sys.stdin.readline().split())    # 열차의 개수, 명령의 개수
ans=[] #정답을 담는 리스트


# 명령을 받는다.
Order=[list(map(int,sys.stdin.readline().split())) for _ in range(M)]

Train=[[0]*20 for _ in range(N)]


for O in Order:
    if O[0]==1:    # 해당열차 해당칸에 사람 추가
        Train[O[1]-1][O[2]-1]=1    # 해당 좌석에 사람을 추가 한다.
        
    elif O[0]==2:    # 해당열차 해당칸에 사람 제거
        Train[O[1]-1][O[2]-1]=0    # 해당 좌석에 사람을 추가 한다.
        
    elif O[0]==3:    # 해당열차 해당칸에 사람한줄씩 뒤로 밀기
        Train[O[1]-1]=deque(Train[O[1]-1])
        Train[O[1]-1].appendleft(0)
        Train[O[1]-1].pop()
        Train[O[1]-1]=list(Train[O[1]-1])
        
    elif O[0]==4:    # 해당열차 해당칸에 사람한줄씩 앞으로 밀기
        Train[O[1]-1]=deque(Train[O[1]-1])
        Train[O[1]-1].append(0)
        Train[O[1]-1].popleft()
        Train[O[1]-1]=list(Train[O[1]-1])
        
        
# 중복을 제거 하기 위해 딕셔너리를 활용해서 넣고 len 하면 허용가능한 열차의 개수가 나온다.
ans={}
for i in Train:
    ans[str(i)]=0
    
print(len(ans))

'''
# 검사시작
ans={}
for i in Train:
    # 원소 1이 리스트에 없는경우 제거 한다.
    if 1 not in i:
        continue
    
    ans[i]=0


print(ans)
'''







