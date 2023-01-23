import sys

#출석 지각 결석

# 개근상을 받는 경우



# 개근상을 받지 못하는 경우
# 1. 순서에 상관없이 지각을 2번 이상
# 2. 3연속 결석시
# O를 출석, L을 지각, A를 결석
# combination을 사용하면 좋겠군

# 모든 경우의수에서 생각을 하면될것같다.

import sys
from itertools import combinations
from math import factorial

N=int(sys.stdin.readline())   #학기



'''
전체 경우의수 =3**N
지각을 0, 1번만 한 경우의수 = 2**N , N!

'''

print(3**N, '전체')
print((2**N)+factorial(N-1), '지각고려')