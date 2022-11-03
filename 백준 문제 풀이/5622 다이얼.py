# 한번 아스키 코드를 이용해서 범위를 구하고 풀어 보자고
#chr(65)~chr(90): A~Z까지 대문자 알파벳
#chr(97)~ chr(122): a~z까지 소문자 알파벳
#ord(x)는 x에 숫자를 넣으면 해당 아스키 코드숫자를 보고 알파벳을 반환


















import sys

def ABC_return_countsec (x):    #x에는 문자열이 들어갈 예정   (각 대문자 알파벳 범위마다 반환값이 나오는 함)
    if x>=chr(65) and x<=chr(67):    #ABC
        return 3
    elif x>=chr(68) and x<=chr(70):     #DEF
        return 4
    elif x>=chr(71) and x<=chr(73):     #GHI
        return 5
    elif x>=chr(74) and x<=chr(76):    #JKL
        return 6
    elif x>=chr(77) and x<=chr(79):    #MNO
        return 7
    elif x>=chr(80) and x<=chr(83):    #PQRS
        return 8
    elif x>=chr(84) and x<=chr(86):    #TUV
        return 9
    elif x>=chr(87) and x<=chr(90):    #WXYZ
        return 10

Str=sys.stdin.readline().strip()


# sum=0
# for i in range(len(Str)):
#     sum+=ABC_return_countsec(Str[i])

sum1=[ABC_return_countsec(Str[i]) for i in range(len(Str))]    #리스트 컴프리헨션 사용해보자

print(sum(sum1))