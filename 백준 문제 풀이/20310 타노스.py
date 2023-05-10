# https://www.acmicpc.net/problem/20310


# 민지학우가 지적한 부분(내가 부분점수를 받은이유)
# 111100 이 있다고 가정하에 타노스 하면 110이되어야 하는데 본인은 011 이라고 생각함(순서가 있다고 생각하면 좋다.)
# 간단하게 생각하자. 문자열의 순서는 그대로 유지하되 지워야하는 1과 0을 가장 효율적으로 지워서 작게 만들어야 한다.
# 문자열의 길이는 2이상 500이하이다 그렇게 많지가 않다.
# 
"""
예시1 
1010을 지우면 01이 나온다 (맨앞 1, 맨뒤 0을 지우면 가장 작은 01이 나오기 때문 하기 때문이다.)

예시2 
000011을 지우면 001이 나온다.(단 이 경우에는 까다로운 조건을 고려하지 않기에 25점만 준다.)
"""
# 010101로 이루어진 2진수에서 가장 작은 수를 만드는 법은 1은 맨앞에서부터 지우고 0은 맨뒤에서부터 지우면 가장 작은수가 될것 같다



import sys


Table=sys.stdin.readline().strip()   #문자열을 분리후 리스트화 완료

zero_counter =int((Table.count('0'))/2)    #삭제해야하는 0의 개수
one_counter =int((Table.count('1'))/2)     #삭제해야하는 1의 개수

Table=list(Table)
for i in range(one_counter):
    Table.remove('1')

Table.reverse()
for i in range(zero_counter):
    Table.remove('0')
Table.reverse()


for i in Table:
    print(i, end='')