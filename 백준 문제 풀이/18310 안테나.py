# https://www.acmicpc.net/problem/18310
'''
import sys

N= int(sys.stdin.readline())
N_list=list(map(int,sys.stdin.readline().split()))

# 내 생각에는 점의 합을 구한뒤, 평균에 가장 가까운 값을 출력하면 될것같은 느낌이다.(점을 기준)

myavg=sum(N_list)/N

if myavg in N_list:
    print(int(myavg))
    exit(0)

if len(N_list)<=2:
    print(N_list[0])
    exit(0)
    

N_list.append(sum(N_list)/N)

N_list.sort()


target_index = N_list.index(myavg)    # 평균치의 인덱스 번호를 찾는다.

# 첫번째 포인트에 모두 거주하는 경우
if target_index==0:
    print(N_list[1])
    
elif target_index==N-1:
    print(N_list[-1])

else:
    king = N_list[target_index]
    if abs(king-N_list[target_index-1]) == abs(king-N_list[target_index+1]):
        print(N_list[target_index-1]) 
        
    elif abs(king-N_list[target_index-1]) < abs(king-N_list[target_index+1]):
        print(N_list[target_index-1])
    else:
        print(N_list[target_index+1])
'''        
# 코드가 너무 복잡하고 내가 원하는 결과가 잘 나오지 않는다.(중앙값의 개념을 활용해서 다시 한번 풀어보자)
# 1. 중앙값을 찾는다.(정수임)
# 2. 집들의 위치에서 중앙값에 가장 가까운 집을 선택한다.
'''
import sys

N= int(sys.stdin.readline())
N_list=list(map(int,sys.stdin.readline().split()))

# 만약 N-> 홀수이면 중앙값이 1개, N -> 짝수이면 중앙값이 2개인걸 알아야 한다.

home=200000

if  max(N_list)%2==0:    # 짝수이면
    mid= max(N_list)//2 +1
    top =200000
    for i in N_list:
        if 0<=mid-i<top:
            top=mid-i
            home=i
else:
    mid= max(N_list)//2 +1
    top =200000
    for i in N_list:
        if 0<=mid-i<top:
            top=mid-i
            home=i
    
#print(mid, "<-- 현재의 중앙값 위치이다 (최대값을 기준으로 선정함)")
print(home, "최적의 집주소")
# 다음으로는 N_list에 적혀있는 집 주소 중에서 가장 중앙값과 가까이 있는 애들을 찾는다.
'''

# 중앙값을 고르는게 핵심인건 잘 알았는데, N이 짝수일때 어떻게 하면 좋지? 를 해결하지 못하였다.
# 하지만 문제에서 
# "첫째 줄에 안테나를 설치할 위치의 값을 출력한다. 단, 안테나를 설치할 수 있는 위치 값으로 여러 개의 값이 도출될 경우 가장 작은 값을 출력한다."
# 라는 문구를 통해서 N=4이면 1 2 3 4 중에서 2 3이 중앙값인데 그냥 2를 선택하면 끝이었다.

import sys

N=int(sys.stdin.readline())
N_list=list(map(int,sys.stdin.readline().split()))

N_list.sort()


# 짝수일떄(중앙값 2개임)  1 2 7 8
if N%2==0:
    print(N_list[N//2-1])
# 홀수일떄(중앙값 1개임)
else:
    print(N_list[N//2])
