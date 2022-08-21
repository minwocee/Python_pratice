#1000번 [동시에 입력깂 넣어주기]
a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
print(a + b)
#설명 a,b = map(int,input().split()) 은 2개를 입력받아 띄어쓰기를 기준으로 나눠주고 각각의 변수에 넣어준다.

 #학생의 이름 학번 나이를 입력받는 프로그램을 만들어 보자
name,number,age = map(str,input().split())
print(name,number,age)

#10926번 준하 놀람 표함
print(input()+"??!")     #input()을 print()안에 넣어줘서 바로 사용이 가능하다

#25083 새싹 만들기
def leaf():
   print('         ,r\'\"7')
   print('r`-_   ,\'  ,/')
   print(' \. \". L_r\'')
   print('   `~\/')
   print('      |')
   print('      |')
leaf()


#2884 알람시간 맞추기 -45분
H,M=map(int,input().split())
if H>=1:
    if M>=45:
        print(H,M-45)
    if M<45:
        print((H-1),60+(M-45))
if H==0:
    if M>=45:
        print(H,M-45)
    if M<45:
        H=3
        print(H,60+(M-45))




