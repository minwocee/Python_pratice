# https://www.acmicpc.net/problem/2121

# 시간복잡도: 2초
# 공간복잡도: 128MB

# 제한
'''
첫 줄에 점들의 개수 N(5 ≤ N ≤ 500,000)이 주어진다. (500000C4는 불가능한 경우이다.)
둘째 줄에 만들고 싶은 직사각형의 가로 길이 A(1 ≤ A ≤ 1,000)와 세로 길이 B(1 ≤ B ≤ 1,000)가 주어진다. 
다음 N줄에 걸쳐서 점들의 좌표가 정수로 주어진다. 이 값의 범위는 -1,000,000,000이상 1,000,000,000이하이다. (엄청큰 범위폭)
N개 점들의 좌표는 각각 다르다.

출력
첫 줄에 가능한 모든 경우의 수를 출력한다. 경우의 수는 2^31-1보다 작거나 같다.
'''

'''
우선 x축 방향으로 오름차순으로 정렬을 해야 한다고 생각함
이제 생각을 해보자, 평행한 x,y축을 가진 변이 있어야 한다고 적혀있다. 그말은, 가로의 길이가 2라고 되어있으면,

2,y, 4,y가 있어야지 그 점을 쓸수 있다는 말이다.(y는 동일한 높이를 의미 한다.)
이렇게 해서 1차로 가로길이로 쓸수 있는 점들을 걸러내고, 
걸러낸 점들을 바탕으로 y축방향으로 또 검사를 진행해서 (x,3) (x,6)의 쌍이 존재한다면 OK걸러내면 문제 해결 가능성?



import sys
T = int(sys.stdin.readline())

# 만들고 싶은 사각형 가로, 세로 길이 입력 받는다.
make_sqr = list(map(int, sys.stdin.readline().split()))

# 각 점들의 좌표 이다.
Field = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]

    
Field.sort(key=lambda x: x[0])



# 공간복잡도 문제가 발생할것 같기는 한데(10^18 승의 자료의 개수가 존재한다.)
import sys

mlist ={}

for x in range(-1000000000, 1000000001):
    for y in range(-1000000000, 1000000001):
        mlist[(x,y)] = False
        
T = int(sys.stdin.readline())

Wx, Wy = map(int, sys.stdin.readline().split())

for  i in range(T-1):
    x, y = map(int, sys.stdin.readline().split())
    mlist[(x,y)] = True
    
cnt = 0
try:
    for x in range(-1000000000, 1000000001):
        for y in range(-1000000000, 1000000001):
            if mlist[(x,y)] and mlist[(x+Wx,y)] and mlist[(x,y+Wy)] and mlist[(x+Wx,y+Wy)]:
                cnt+=1
except KeyError:
    pass

'''

# 시간복답도 분석 n임 그냥, 알고리즘 안쓰고 품
import sys

T = int(sys.stdin.readline())

x,y = tuple(map(int, sys.stdin.readline().split()))

Mlist ={tuple(map(int, sys.stdin.readline().split())):True for _ in range(T)}

keys = list(Mlist.keys())

cnt = 0

for k in keys:
    try:
        if Mlist[k] and Mlist[(k[0]+x, k[1])] and Mlist[(k[0], k[1]+y)] and Mlist[(k[0]+x, k[1]+y)]:
            cnt+=1
    except KeyError:
        cnt+=0
print(cnt)