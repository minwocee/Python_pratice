import sys

while(True):
    A=sys.stdin.readline().strip()

    if A=='0':
        break

    if A == A[::-1]:  #처음부터 끝까지 슬라이싱하되 증감폭이 -1로 설정(문자열을 reverse 하는 방법이다!)\
        print('yes')
    else:
        print('no')
    
    