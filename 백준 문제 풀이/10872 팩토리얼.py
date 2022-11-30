# 직접 팩토리얼 재귀 함수를 만들어 보자






























def my_fac(N):
    if N==0:
        return 1
    return N*my_fac(N-1)






import sys
import math
N=int(sys.stdin.readline().strip())
print(my_fac(N))