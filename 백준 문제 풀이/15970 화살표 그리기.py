#https://www.acmicpc.net/problem/15970

# 색깔과 위치를 잘 기억해주는 것이 핵심 이다.

# 리스트를 만들고 뒤집어서 다시 구하면 끝이다.

import sys

N=int(sys.stdin.readline())   # 점의 개수를 입력 받는다.

Field = [list(map(int,sys.stdin.readline().split())) for i in range(N)]
# 2차원 배열 형태로 입력 완료 (좌표, 색)

print(Field)