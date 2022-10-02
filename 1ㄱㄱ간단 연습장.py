#if문 활용예제
k=int(input("1부터 100사이의 정수를 입력 하시오: "))

if k<100:
    print("입력한 정수가 100보다 작음")
    print(f"a = {k}")

if k>=100:
    print("프로그램 종료") 

#예제 4-2 if-else 활용

k=int(input("1부터 100사이의 정수를 입력 하시오: "))

if k<100:
    print(f"입력한 a의 값은 {k}이며 100보다 작음")
    print("프로그램 종료") 
else:
     print(f"입력한 a의 값은 {k}이며 100보다 크다")
     print("프로그램 종료") 


#중복 if-else문 활용
k=int(input("1부터 100사이의 정수를 입력 하시오: "))
if k>=0:
    if k==0:
        print("입력한 정수는 0임")
    else:
        print("입력한 정수는 %d이고 양수임"%k)
else:
    print("입력한 정수는 %d이고 음수임"%k)

#나이와 점수에 따라 합/불을 정하는 프로그램
age, score=map(int,input().split())

if age>20:
    if score>80:
        print("합격입니다")
    else:
        print("점수가 너무 낮아 불합격 입니다.")
else:
    print("나이가 너무 어려서 불합격 입니다.")


#-10에서 10까지의 정수를 입력받고 크기를 측정한다.
for i in range(5):
    i=int(input("-10에서 10 사이의 정수를 입력 하세요: "))
    
    if i<-10:
        print(f"입력한 정수는 {i}이고 -10보다 작음")
    elif i>=-10 and i<=10:
        print(f"입력한 정수는 {i}이다.")
    elif i>10:
        print(f"입력한 정수는 {i}이고 10보다 크다")
    elif i==0:
        print("입력한 정수는 %d이다."%i)


#리스트에 특정 요소가 있으면 작동하는 프로그램 생성(if 요소 in 리스트)
pocket=[]
pocket.append(input("내 지갑에 현재 있는것은? (money, card...) : "))
if "money" in pocket:
    print("택시타고 가자")
elif "card" in pocket:
    print("버스타고 가자")
else:
    print("아무것도 없으니 걸어가자...")


#학생들의점수에 따른 학점을 부과하는 프로그램을 작성 해보자:
score=int(input("학생의 점수를 입력 하시오: "))

if score>=90:
    grade='A'
elif score>=80:
    grade='B'
elif score>=70:
    grade='C'
elif score>=60:
    grade='D'
else:
    grade='F'
print("당신의 점수는 {0} 이며 등급은 {1} 입니다.".format(score, grade))

#윤년을 계산하는 프로그램 만들기
year=int(input("윤년 계산을 원하는 연도를 입력하시오(예시: 1999, 1989 ....): "))

if((year%4==0) and (year % 100 !=0) or (year%400==0)):
    print(year,"은 윤년이 맞습니다.")
else:
    print(year,"은 윤년이 아닙니다.")

#for 문을 활용한 팩토리얼을 계산하는 법

N=int(input("팩토리얼 계산을 원하는 0 이상의 정수를 입력 하시오: "))

for i in range(N):
    if(N==0):    #0!=1이므로 이 경우는 특수하게 처리한다.
        sum=1
        break
    sum=sum*i

print("입력한 정수는",N,"이며 팩토리얼 연산 결과는 :",sum)

#1~100까지의 홀수, 짝수의 합
even,odd=0,0
print("1부터 100까지의 짝수항, 홀수항의 합을 구해보자\n")
for i in range(1,101):
    if(i%2==0):    #짝수인 경우
        even+=i
    else:
        odd+=i
print("짝수항의 합:",even)
print("홀수항의 합:",odd)

#range를 활용해서 리스트를 생성하는법
L1=list(range(10))    #이러면 리스트에 0~9까지 들어감
print(L1)
print(list(set(L1)))    #이건 중복을 제거한후 다시 리스트로 변환해서 넣어주는 과정


#이중으로 for 문을 사용해 구구단을 출력하자
for i in range(2,10):
    for k in range(1,10):
        print(f"{i} * {k} = {i*k}", end=" | ")
    print("")


#일반 리스트와 튜플의 값을 출력해보자
Lis1=["one","two","three"]
for i in range(Lis1):
    print(Lis1)
Lis2=[(1,5),(2,6),(3,7)]
for(a,b) in Lis2:
    print(a+b)

#일반 리스트와 튜플의 값을 출력해보자
Lis1=["one","two","three"]
for i in Lis1:
    print(i)


Lis2=[(1,5),(2,6),(3,7)]    #튜플 형태로 리스트에 저장이 되어 있다.
for(a,b) in Lis2:
    print(a+b)

#학생의 점수
score=[90,20,10,100,80]
for i in score:
    if i>=70:
        print(f"{score.index(i)+1}번 학생은 합격이며 점수는 {i}입니다.")
    else:
        print(f"{score.index(i)+1}번 학생은 탈락이며 점수는 {i}입니다.")


#continue 를 사용한 반복문건너뛰기

score=[90,20,10,100,80]
for i in score:
    if i<70:
        continue    #불합격자들은 건너뛰고 합격자만 메세지를 출력함
    print(score.index(i)+1,"번 학생은",i, "점으로 합격입니다.축하드립니다.")

#트리 만드는 방법1(반복문 2개 사용)
N=int(input("숫자를 입력 하시오: "))
for i in range(1,N+1):
    for k in range(i):
        print("*",end="")
    print("")

#트리 만드는 방법2(반복문 1개 사용)
N=int(input("숫자를 입력 하시오: "))
for i in range(1,N+1):
    print("*"*i)

#for문 1번 사용해서 역으로 만드는 트리 생성하기

x=int(input("가로의 길이: "))

for _ in range(x,0,-1):
    print("x"*_)

#직사각형의 가로와 세로를 입력받고 점을 찍으주는 프로그램

x=int(input("가로의 길이: "))
y=int(input("세로의 길이: "))

for i in range(x):
    for k in range(y):
        print("x", end="")
    print('')


#더 간단하게 만드는 직사각형의 가로와 세로를 입력받고 점을 찍으주는 프로그램

x=int(input("가로의 길이: "))
y=int(input("세로의 길이: "))

for _ in range(y):
    print("*"*x)

#가운데로 정렬해서 만드는 트리를 만들어 보자(어려움)

x=int(input("밑변의 길이: "))

for i in range(1,x+1):
    print(((x-i)*' ')+'x '*i)    #빈칸의 배열+점의 배열을 합한 원리이다.

#5의 배수를 제거해서 출력하는 프로그램

N=int(input("출력을 원하는 숫자를 입력 하시오: "))

for i in range(1,N+1):
    if not (i%5==0):    #if not을 사용하 특정조건이 아닐시 실행하는 조건을 걸어줌 if (i%5==0)이면 continue로 써도 가능
        print(i,end=" ")

#예제 4-27 비트연산해서 출력하는것 (어려움)
x=int(input("숫자를 입력 하세요: "))
a=1

for i in range(0,11):
    print('{0:6,}'.format(a<<i),end=' ')
print()


#while 활용법
x=int(input("출력 횟수를 지정 해주세요: "))
sum=0
while(sum<x):
    print("Hello world")
    sum+=1

#4-30 예제
i,hap=0,0
num1=int(input("시작 값을 입력 하시오: "))
num2=int(input("끝값을 입력 하시오: "))
num3=int(input("증감값을 입력 하시오: "))
i=num1

while i<num2+1:
    hap+=i
    i+=num3
print("{}에서{}까지 {}씩 증가시킨 값의 합계: {}".format(num1,num2,num3,hap))


#while 활용법2
import random
i,count=0,0
while i !=1:
   i=random.randint(1,101)
   print(i)
   count+=1
print("드디어 끝났네요 시도횟수: ", count) 

#무한루프 활용

sum=0

while(True):
    a=int(input("첫번째 수를 입력 하시오 (0을 입력하면 종료됨): "))
    if(a==0):
        break
    b=int(input("두번째 수를 입력 하시오: "))
    print("두수의 합: {}".format(a+b))

#while 활용 학점 분류

while(True):
    score=int(input("학생의 점수를 입력 하시오: "))
    if(score>100 or score<0):
        print("0~100 사이의 정수를 입력 해주세요(등급 분류 불가)")
        print('_______________________________________')
        continue
    if(score>=90):
        print("{}점 이므로 A 학점 입니다.".format(score))
        print('_______________________________________')
    elif(score>=80):
        print("{}점 이므로 B 학점 입니다.".format(score))
        print('_______________________________________')
    elif(score>=70):
        print("{}점 이므로 C 학점 입니다.".format(score))
        print('_______________________________________')
    elif(score>=60):
        print("{}점 이므로 D 학점 입니다.".format(score))
        print('_______________________________________')
    else:
        print("{}점 이므로 F 학점 입니다.".format(score))
        print('_______________________________________')


#약수의 개수를 구하고 약수를 출력해주는 프로그램을 만들자(좀 까다롭지만 유용)
while True:
    num=int(input("정수를 입력 하시오(0은 종료키): "))
    if not num:
        break    #정수가 아니면 반복문을 탈출하는듯
    if num<0:
        print("양의 정수를 입력하시오")
        continue    #다시 처음으로 돌아간다.
    count=0    #약수의 개수를 세어주는 변수를 선언 한다.
    for i in range(1,num+1):
        if num%i==0:
            print('{0:5}'.format(i),end=' ')    #앞에 4칸을 띄워줌(마지막 인덱스인 [4]에 i가 들어가고 나머지는 공백으로 채움)
            count+=1
    print()
    print("{0}의 약수의 개수: {1}개 입니다.\n".format(num,count))