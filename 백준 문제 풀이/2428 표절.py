# https://www.acmicpc.net/problem/2428

# 1초의 시간 제한

#  (1 ≤ 검사대상수 ≤ 100,000, 1 ≤ 대상크기 ≤ 100,000,000) 

# 최악의 경우는 100,000개를 모두 검사 하는 100000C2 이다. 약 5*10^9이므로 시간초과 발생
# 아마 권역 별로 묶어서 계산하는게 가장 적절하다고 판단된다.
#                                                                               작은거            큰거
# 따라서, (Fi, Fj) 쌍을 검사해야 하는데, 이때, i≠j이고, size(Fi) ≤ size(Fj)이면서, size(Fi) ≥ 0.9 × size(Fj) 인것만 검사

'''
시간제한    1초 (10^8의 연산)
메모리제한  128MB
N의 개수    10^5 개
size       10^8 정수범위 까 
'''
# 일반적인 10^5C2는? --> 10^8의 시간복잡도 소개


import sys

N=int(sys.stdin.readline())

# 실수형으로 바꿔주기
Field = list(map(float, sys.stdin.readline().split()))

Field.sort()
print(Field)
cnt = 0


# 리스트 정렬후 점점 N개 탐색, N-1개 탐색... 줄여나가는 방식을 쓰기 위한 for문 이다.
for _ in range(N):
    left = _
    right = N
    
    # 왼쪽이 오른쪽을 넘어서는 순간 이분탐색 정지 한다.(인덱스)
    while left < right:
        middle = (left+right)//2
        
        # 카운트 해주어야 하는 이벤트가 발생한다.
        if Field[left]>=Field[middle]*(0.9):
            left = middle +1
        else:
            right = middle
    
    # 현재 탐색이 종료된 인덱스 - 지금까지 for문을 사용해서 줄여나간 시작인덱스 - 0번부터 시작하므로 하나 빼주는 역할
    cnt += right - _ -1
    
print(cnt)