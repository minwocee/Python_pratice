#가희와 btd 벌룬 타워 디펜스

''' <직접 구현한 틀린 코드>
import sys

Ballun, at_chance= map(int, sys.stdin.readline().split())    #풍선개수, 공격횟수

B_table=[list(map(int,sys.stdin.readline().split())) for _ in range(Ballun)]
at_table=[list(map(int, sys.stdin.readline().split())) for _ in range(at_chance)]

# print(B_table)    #풍선x좌표, y좌표, 체력 형태로 들어가는걸 확인 
# print(at_table)    #타워x, 타워y, 데미지 입력 받는다.

# 기울기가 같으면, 같은 선상에서 위치한다는걸 알아두자
# 그런데 기울기 개념을 사용하면, 제로 디비전 에러가 나온다. 일단 구현 먼저 해보자

for i in range(at_chance):
    # 0,1   1,0  -1,0  0,-1 4가지의 축 위에 있느 경우를 생각해보자 4개의 elif
    if at_table[i][0]==0 :   #북쪽
        타워공격방향=0
    else:
        타워공격방향=at_table[i][1] / at_table[i][0]     #y/x 를 해주는 꼴이다.

    

    for k in range(Ballun):    #풍선에 대한 검사를 실행한다.

            

        if 타워공격방향 == (B_table[k][1] / B_table[k][0]):     #타워의 기울기와 원점-풍선의 기울기가 같으면,
            B_table[k][2]-=at_table[i][2]    #풍선의 체력이 감소한다.

#print(B_table)

cnt=0
for _ in B_table:    #
    if _[2]>0:
        cnt+=1


print(cnt)

# 확인결과, x좌표가 0이면 제로 디비전 에러가 발생하는걸 알수있다.
# 이 부분만 예외 처리를 해주자
'''

# 다른분의 코드를 분석해보자

import sys   
input = sys.stdin.readline
from heapq import heappop, heappush     # 힙 사용(힙: 최소값, 최대값을 사용하기 위해서 만든 형태)
# 힙은 시간 복잡도가 짧은 정렬 라이브러리
from math import gcd    #최대공약수 문제 해결시 사용

def find_s(x, y):
    g = gcd(x, y)
    return (x/g, y/g)     # x,y를 각각 두 수의 최대공약수로 나눠서 반환하는 함수


N, M = map(int, input().split())     # 풍선개수, 공격횟수
D = {}    #빈 딕셔너리 자료형 선언(리스트보다는 속도가 빨라서 사용한다.)

# D는 (x/g, y/g) :[0, []]  이런 형태로 딕셔너리는 저장이 된다.

for _ in range(N):    # 풍선의 개수 만큼 반복을 실행한다.
    x, y, d = map(int, input().split())    # 풍선의 정보 입력 받는다.
    s = find_s(x, y)    # s는 튜플형태
    if not D.get(s, ''):    #만약 딕셔너리에서 key=s(s는 최대공약수로 나눈 튜플)를 가진게 존재하지 않으면
        D[s] = [0, []]    # s : [0, []] 쌍을 추가한다.(없으면 공간을 할당)
    heappush(D[s][1], d)    # 딕셔너리 value의 리스트(중첩리스트)에 풍선체력을 넣는다.
    #(x/g, y/g) :[0, [<풍선체력>]]     *이걸 기약분수 꼴 이라고 한다.


#print(D)     #{(1.0, 1.0): [0, [2, 4, 3]]} 형태로 예제가 저장된다.
# (1.0, 1.0)의 좌표/최대공약수를 가진 딕셔너리의 키가 [2,4,3]--> 해당 직선에 존재하는 풍선의 체력이 힙 구조(이진트리구조로 정렬 되어 있다.)


for _ in range(M):    # 공격 횟수 만큼 입력을 받는다.
    x, y, d = map(int, input().split())    #x좌표,y좌표,데미지 입력받는다.
    s = find_s(x, y)    #최대공약수로 x,y를 튜플형태로 바꾼다.
    
    if not D.get(s, ''):    #만약 해당 딕셔너리가 s를 가지지 못하면
        print(N)    #풍선의 개수를 출력한다.
        continue
    
    D[s][0] += d    #(x/g, y/g) :[0, [풍선체력리스트]] 에서의 0에 데미지를 추가한다.
    
    while D[s][1]:    # 만약 풍선이 존재하면
        if D[s][1][0] > D[s][0]: 
            break    
        #풍선리스트 힙의 첫번째 요소 체력(최소힙) > 타워데미지  이면 반복을 중지한다. 
        
        # D[s]=[damage, [풍선 체력들]] 이런 형태 이다. s는 좌표를 최대공약수로 나눈 형태 
        heappop(D[s][1])    #풍선체력리스트 하나씩 제거
        N -= 1   # 살아있는 풍선의 개수를 하나 감소 시킨다.

    print(N)    #풍선을 출력한다.

''' 간단히 말해서 풍선 힙구조에서 맨 앞에 최소값인데 이 최소값이 데미지 보다 같거나 작으면 터짐 
(계산한것들은 heappop을 통해서 가장 위에 존재(최소값)이 빠져 나간다.)
'''





