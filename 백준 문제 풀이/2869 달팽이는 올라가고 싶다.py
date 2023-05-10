# # https://www.acmicpc.net/problem/2869

# # if문 탈출을 언제 시작할지가 관건 이다.

# '''
# 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다.
# (1 ≤ B < A ≤ V ≤ 1,000,000,000)
# '''

# import sys

# # 올라가기, 내려가기, 나무높이 실행한다.
# Up, Down, Tree_height= map(int, sys.stdin.readline().split())

# Date=0
# #나무가 올라가는데 걸리는 시간을 구하였다.
# # 2업 1다운 5미터, 4일 걸린다.
# Date=round(Tree_height/(Up-Down))
# dar = Tree_height/(Up-Down)

# print(Date, '예상 수치')
# print(dar, '다운 고려 안함')

"""
점화식을 작성해보자
K=우리가 구하고자 하는 일수

Up*K - Down*(K-1) >= Tree_Height
올라감  내려감(1일제외)

K에 대해서 정리를 해보면

(UP-Down)K >= Tree_Height+Down
K >= (Tree_Height - Down) / (Up-Dowun)    # 단 2.3 같이 나오면 +1해서 3 출력 해야 한다.

부등호를 활용해서 범위를 저장 해보자.
"""


import sys

Up, Down, Tree_height = map(int, sys.stdin.readline().split())

K = (Tree_height - Down) / (Up-Down)
print(int(K) if int(K)==K else int(K)+1)     
# K가 소수점이 없으면 K 출력, 소수점이 있으면 K+1을 출력 한다.

"""
수학적 공식을 유도하는게 핵심, 부등호를 사용해서 생각해보자
"""
