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


#3052번 나머지의 중복 개수 맞추기
arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr)    #쉽게 말해서 중복되는 숫자가 없이 집합을 만들어줌
print(len(arr))    # 그 집합의 길이가 곧 겹치치 않는 원소의 개수와 같다.

#1546번 조작한 점수의 평균을 구하기
N=int(input())
mylist=[]
mylist=list(map(int,input().split()))    #리스트에서 스페이스 간격으로 넣어줄때는 이렇게 넣어 보자

k=max(mylist)

for i in range(N):
    mylist[i]=(mylist[i]/k)*100

print(sum(mylist)/len(mylist))


#백준 25614번(자리바꾸기)
N,M=map(int, input().split())    #7명, 11일
firstlist=list(map(int,input().split()))    #N명 만큼 초기 배치를 넣음(이 규칙대로 인덱스 참고) 5 6 2 1 7 3 4

a = []    # 전체리스트속 리스트를 생성(2차원 배열 활용)
 
for i in range(M):
    line = []              # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(N):
        line.append(0)     # 안쪽 리스트에 0 추가
    a.append(line)         # 전체 리스트에 안쪽 리스트를 추가
 
"""
1일째: 5 6 2 1 7 3 4    (최초 선언 규칙)
2일째: 7 3 6 5 4 2 1
3일째: 4 2 3 7 1 6 5
"""

rulelist=[]
for i in range(N):     #sl에 쓰레기값 넣음
    rulelist.append(0)

for i in range(N):     #tl에 쓰레기값 넣음
    rulelist[i]=firstlist[i]
print(rulelist, "움직이는 규칙들 정상적으로 삽입 완료")    #5 6 2 1 7 3 4

for i in range(1,M):    #M=11 1,2,3,4...11
    for p in range(N):
        c=firstlist[p]
        a[i][p]=rulelist[c-1]
    
    for q in range(N):    #룰 리스트를 업데이트
        rulelist[q]=a[i][q]

print(a[-1])
   
#12034번 문제풀이(김인천씨의 식료품 가게)

T=int(input())    #테스트 케이스가 들어가는 자리
Total=[0]    #마지막 결과물들을 담아주는 배열

for _ in range(T):
    P=int(input())    #할인된 가격표의 개수
    mlist=list(map(int,input().split()))    #리스트 크기를 할당하고 생성 완료
    
    for i in range(P):    #정상가 요소들을 제거하는 과정
        if(mlist[i]*(4/3) in mlist):
            mlist.remove(mlist[i]*(4/3))
    Total.append(mlist)

del(Total[0])    #첫번째 요소인 정수 0을 지운다.

for k in range(T):
    print(f"Case #{k+1}",end=": ")
    for _ in range(len(list(Total[k]))):    #리스트 속의 리스트를 추출하기위해 사용
        print(Total[k][_],end=" ")
    print()

#어떤 문제 였진
mlist=list(range(1,10001))    #1~10000까지의 정수를 입력
Total=list(range(1,10001))

def devide(x):#각 자리수를 분해하는 함수를 만들기
    if x>=1000:    #천의자리 분해
        m1000=x//1000    #9903에서 9를 가져옴
        m100=(x-(m1000*1000))//100    #903에서 9를 가져옴
        m10=(x-m1000*1000-m100*100)//10    #0이 들어감
        m1=(x-m1000*1000-m100*100-m10*10)    #3이 들어감
        return x+m1000+m100+m10+m1  #9903+9+9+0+3=9924는 예외
    
    elif x>=100:    #백의자리 분해
        m100=x//100
        m10=(x-m100*100)//10
        m1=(x-m100*100-m10*10)
        return x+m100+m10+m1
    
    elif x>=10:    #십의자리 분해
        m10=x//10
        m1=x-m10*10
        return x+m10+m1
    elif x>=1:
        return x+x


for i in range(10000):
        try:
            if(devide(mlist[i])  in mlist):
                Total.remove(devide(mlist[i]))
        except ValueError:
            continue

print(1)

for i in mlist:
    try:
        print(Total[i])
    except IndexError:
        continue


# 백준 11654 아스키 코드 리턴
# ord() : 문자의 아스키 코드값을 리턴하는 함수이다.
# chr() : 아스키 코드값 입력으로 받아 그 코드에 해당하는 문자를 출력하는 함수이다

N=input()
print(ord(N))