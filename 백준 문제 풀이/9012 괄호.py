# https://www.acmicpc.net/problem/9012

# 간단히 말해 ()()괄호의 열고 닫는 쌍이 일정한지를 판별 하는 문제
# VPS


'''
예제 입력1

6
(())())   틀림 
(((()())()   틀림
( ( ) ( ) ) ( ( ( ) ) )     맞음
((()()(()))(((())))()    틀림
()()()()(()()())()    맞음
(()((())()(    틀림
'''

"""
조건들 모음 (문자열 길이는 50개 까지 허용 한다.)
1. 왼쪽과 오른쪽 괄호의 개수가 같아야 우선 성립

2. 같은 방향의 괄호가 나온뒤 동일한 개수의 괄호가 나와야 한다 만약 해당 조건을 만족하지 않은 채로
같은 방향의 괄호가 또다시 나오면 문제가 발생 한다. ((")"() 같은 상황
11010
10101010101010
110
3. 
"""


'''실패한 나의 풀이
import sys
#한번 디큐를 써보자
from collections import deque

N=int(sys.stdin.readline())

for _ in range(N):
    Table = sys.stdin.readline().strip()
    
    if Table.count('(')!=Table.count(')'):
        print('NO', '쌍이 문제가 맞지 않는 현상 발생')
        continue
    Table = list(Table)
    
    while(True):
        for i in range(len(Table)-2):
            if Table[i]=='('and Table[i+1]==')':
                del(Table[i:i+2])
        
        if len(Table)==2 and (Table[0]=='(' and Table[1]==')'):
            print('Yes')



    # my_deque = deque(Table)
    
    # while(len(my_deque)>1):
    #     a=my_deque.popleft()
    #     b=my_deque.pop()
        
    #     if a==b:
    #         print('NO')
    #         break

'''

""" 참고한 다른분의 풀이 """
# '(': +1하는 문자열, ')': -1하는 문자열 계산 방식을 통해 
# ())) 처럼 쌍이 맞지 않는 경우 sum<0이 되므로 No 출력
# 연산을 수행하면서 sum이 0보다 작은 음수로 내려가는경우, 0보다큰 양수가 되는 경우는 문제가 발생한다고 생각 하면 된다.
 
import sys

N=int(sys.stdin.readline())

for _ in range(N):
    K=sys.stdin.readline().strip()
    sum =0
    for check in K:
        if check=='(':    # 왼쪽 괄호면 +1
            sum+=1

        elif check==')':   # 오른쪽 괄호면 -1
            sum-=1
        
        
        if sum<0:    # 이떄 만약 0보다 작아지면 불균형 발생하므로 NO 출력후 break
            print('NO')
            break



    if sum>0:    # 만약 (((((만 나와서 양수가 된 경우도 불균형이 발생한 케이스이기 떄문에 NO 출력
        print('NO')
    elif sum==0:    # 정상적으로 짝이 맞는 경우는 합격 (단 elif문을 사용해 우선 검증을 실시 해야 한다.)
        print('YES')
    










