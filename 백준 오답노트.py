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
H, M = map(int, input().split())

if M < 45 :	# 분단위가 45분보다 작을 때 
    if H == 0 :	# 0 시이면
        H = 23
        M += 60
    else :	# 0시가 아니면 (0시보다 크면)
        H -= 1	#내가 이걸 깜빡해서 많이 틀림
        M += 60        
print(H, M-45)

#2525 오븐 알람시간 맞추기
A,B=map(int,input().split())
C=int(input())
A+=(B+C)//60    #먼저 시침을 넣어주기
B=(B+C)%60    #먼저 분침을 넣어주기
if A>23:
    A-=24
print(A,B)    

#


