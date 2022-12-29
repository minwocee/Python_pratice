#https://www.acmicpc.net/problem/1436

import sys
# from itertools import permutations

Table=[str(a) for a in range(666,10000000) if '666' in str(a)]

N= int(sys.stdin.readline())
print(Table[N-1])


# 순열을 사용해서 666이 들어간 문자열 조합을 만든뒤 666~10000000까지의 정수 조합을 통해서
# 해당 요소의 순서에 맞게 출력한다.
# 아주 머리를 잘썻다고 필자는 생