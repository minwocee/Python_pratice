# 팰린드롬 만들기
# https://www.acmicpc.net/problem/1213

 
# Time Complexity: 
import sys
from collections import Counter

Text = sys.stdin.readline().strip()

'''
펠린드롬, 좌우로 대칭이 되어야 한다.
최대 50글자 이며, 사전순으로 우선 사용 한다.
사전순으로~ 라는 말을 주의 해야 하는것 같다.
'''

# 입력의 길이 만큼 초기화를 해준다.
Mlist = [0]*len(Text)

# 등장횟수를 카운트 한다.
Text_cnt=Counter(list(Text))

# [('A', 3), ('B', 3)] 이런식으로 정리되는 Text_alpa
Text_alpa = list(Text_cnt.items())

A =''
B =''
C = []

Text_alpa = sorted(Text_alpa, key = lambda x :x[0])
for T in Text_alpa:
    cnt = T[1]
    cnt_1 = cnt//2
    cnt_2 = cnt%2
    if cnt_2>0:
        C.append((T[0],cnt_2))
    
    for i in range(cnt_1):
        A+=T[0]
        B+=T[0]
        
# print(C, '나머지들')
# print(A, 'A배열')
# print(B, 'B배열')

if len(C)>1:
    print('I\'m Sorry Hansoo')
else:
    if len(C)>0:
        print(A+C[0][0]+A[::-1])
    else:
        print(A+A[::-1])
        
# 반례 발견(사전순으로 출력이 안된다.), key = lambda x:x[0]을 사용해서 정렬 하자
'''
BCDAADCB
예상출력 : ABCDDCBA
출력 : BCDAADCB
'''