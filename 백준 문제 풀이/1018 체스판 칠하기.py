# https://www.acmicpc.net/problem/1018
# N: 행개수 M: 열개수
# 8<= N,M <=50 의 자연수이다.
# 체스판 왼쪽상단이 Black 혹은 White로 BWBWBWBW ,WBWBWBWB 이렇게 완성이된다. 
# 이때 흰검흰검 조합을 맞추기 위해서 몇개를 수정해야 하는가가 문제의 핵심이다.

# 조건 1.행열의 개수에 맞게 자르기
# 조건 2. 자른 타일들을 몇개를 칠해야 하는지 검사를 실행 

"""
<예제 입력1> 
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW

<예제 출력1> 
1
"""

import sys

Rows, Colums=map(int, sys.stdin.readline().split())     #행의개수, 열의개수가 입력된다.

# 첫행을 읽고 패턴을 파악한뒤 틀린것의 개수를 파악을 한다. 아주 간단한 문제이다.
Table=[['']*Rows]

for _ in range(Rows):
    Table[_]=[sys.stdin.readline().strip()]

print(Table)























