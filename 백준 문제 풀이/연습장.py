# import sys

# R, C=map(int, sys.stdin.readline().strip().split())    #방의 세로의 길이, 가로의 길이 주어짐
# rg,cg,rp,cp=map(int, sys.stdin.readline().strip().split())    #가희의 세로길이, 가로길이, 베게의 세로길이, 가로길이 주어짐

# #이제 문자열을 입력 받는다
# mlist=[]
# sum=0
# for _ in range(R):
#     k=sys.stdin.readline().strip()
#     mlist.append(k)
#     sum+=k.count("P")   #가희의 개수를 센다

# if sum<rp*cp:
#     print(1)
# else:
#     print(0)



#2번문제 시작

import sys

T,n=map(int, sys.stdin.readline().strip().split())# T초일때까지, n: 입력하는 횟수
# 걍 아무튼 프로세서 선택을 한다 함, 우선순위 높은것부터 1개씩 깎아내리면 됨 와리가리해서


A_list=[0 for _ in range(n)]  #id 저장소
B_list=[0 for _ in range(n)]  #남은 프로세스 시간
C_list=[0 for _ in range(n)]  #우선순위들

for _ in range(n):
    k=list(map(int,sys.stdin.readline().strip().split()))
    A_list[_],B_list[_],C_list[_] =k[0], k[1], k[2]

"""
일단 각 요소들을 분리해서 집어 넣는건 성공함 그렇다면 해야할것
1. 우선순위를 비교해서 해당 인덱스 번호를 찾음 그리고 나머지 것들 모두 1씩 증가(3)
2. 해당 인덱스번호 id 출력후(1), 해당 인덱스의 남은 프로세스 시간을 1 감소시킴(2)
3. 이후 다시 반복을 실시함
"""

while(True):
    king=max(C_list)
    index_list=[]
    for i in range(len(C_list)):
        if king==C_list[i]:
            index_list.append(i)    #우선순위 높은 애를 인덱스 리스트에 받아옴
    
    #이제 중복값이 몇개인지 센다
    if len(index_list)>=2:   #중복값이 2개 이상일때 실행
        low_id=10000000
        for o in index_list:
            if A_list[o]<low_id:
                low_id=A_list[o]
        print(low_id)
        
        


