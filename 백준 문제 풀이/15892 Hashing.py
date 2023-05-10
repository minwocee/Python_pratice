# https://www.acmicpc.net/problem/15829

"""
a=1 b=2 .. z=26  까지 요소를 매칭한다.
왼쪽에서부터 31^0, 31^1 31^2 곱해준다고 생각 ... 이렇게 해서 함수를 만들수 있다.
"""


# print(ord('a'))   # 97번

# print(chr(97))   #a 출력함

import sys


N= int(sys.stdin.readline())
table=sys.stdin.readline().strip()

# m_dic={chr(k+96):k for k in range(1,27)}#수정하기


ans=0
cnt=0
for i in table:
    ans+=(ord(i)-96)*pow(31,cnt)
    cnt+=1

print(ans%1234567891)    # 마지막에 이 나누기를 추가 해보자, 문제를 끝까지 읽는 습관을 들이자







