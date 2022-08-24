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

#15552번 sys 사용(좀더 빠르게 컴파일 가능,거의 사용 안함)
import sys
 
inp = int(input())
for i in range(inp):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)

#2439 별찍는 문제
N=int(input())

for i in range(1,N+1):
    print(" "*(N-i),end="")
    print("*"*i)

#10871번 리스트 생성하고 넣어주기
N, X = map(int, input().split())
A = list(map(int, input().split()))    #이런식으로도 리스트 생성에 넣어주기까지 바로 가능하구나 몰랏네
for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")

#10952번 break를 사용해라
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a+b)

#10951번 try-except 활용  (오류가 발생하면 종료하는 시스템)
while True:
    try:
        a, b = map(int, input().split())
    except:    #오류가 생기면 종료한다
        break    #break대신 print("error")라고 적으면 오류메세지 출력하고 다시 실행한다.
    print(a+b)

#1110 일의자리,십의자리 분리하는 문제(좀 어려웠음)
N=int(input()) #0~99 사이의 수를 입력 받음 나눗셈 10을 해서 십의 자리와 일으 ㅣ자리를 구분하자
k=N    #변하는 수
q=0    #나중에 출력 해야 하는 시도 횟수
while True:
    result = k//10 + k%10 # 2+6=8 완성  6+8=14 완성
    if result>=10:
       result=result-(result//10)*10
    k=result + (k%10)*10  #8+60= 68 완성 14+4=18 완성
    q+=1
    if N==k:
        break    
print(q)
#2+6=8 -->68
#6+8=14 -->84
#8+4=12 -->42
#4+2=6 -->26

#10181번 배열에서의 최솟값과 최댓값
cnt = int(input())    #이 문장이 코드에 영향을 미치지는 않는다
numbers = list(map(int, input().split()))
print(min(numbers),max(numbers))     #배열내에서의 최대,최솟값을 구해주는 함수 작성

#또다른 방법2
cnt = int(input())
numbers = list(map(int, input().split()))
numbers.sort()    #오름차순으로 정렬
print(numbers[0], numbers[-1])    #첫번째, 마지막 인덱스를 출력

#또다른 방법3
cnt = int(input())
numbers = list(map(int, input().split()))    #배열을 스페이스 간격으로 계속 받아줌(엔터 치면 초기화)
max = numbers[0]    #배열의 첫번째 값을 넣어준다.
min = numbers[0]

for i in numbers[1:]:    #배열의 2번째 인덱스 부터 비교를 시작한다
    if i > max:
        max = i
    elif i < min:
        min = i
print(min,max)

#2562번 최댓값구하기
numbers = []
for _ in range(9):
    i = int(input())
    numbers.append(i)
    
print(max(numbers))
print(numbers.index(max(numbers))+1)