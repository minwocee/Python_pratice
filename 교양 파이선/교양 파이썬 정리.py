#교양 파이썬 22.09.06 (1주차) 응용문제1
from time import sleep
from turtle import *
color('red', 'yellow')    #테두리는 빨간색, 속은 노랑색으로 채운다.

begin_fill()

while True:
    forward(100)
    left(170)
    if abs(pos())<1:    #abs(): 절대값 만들어 주는 함수, pos():포지션, 현재 위치 좌표
        break
end_fill()
sleep(3)

#집 만들기 코드
import turtle
turtle.shape("turtle")
print("20180876")
turtle.forward(150)
turtle.right(60)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.left(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.up()
turtle.goto(80,-60)
turtle.down()
turtle.right(60)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
sleep(3)    #3초동안 대기하라는 의미
print("천민우")


""" ***********************2022.09.13(화)************************작성"""


x=float(input("정수: "))
y=x+1
print(y)

x,y=y,x    #파이썬 내부에서 임시로 변수를 생성해서 편리하게 바꿔줌(파이썬의 편리성)
#정석: t=x; x=y; y=t


x1="3.14"
x2=float(x1)
x3=int(x2)    #실수에서 정수로 변환시 소수점 부분 손실 발생
x4=str(x3)
print(x1,x2,x3,x4)

print(type(x4))     #해당 변수의 데이터 타입 출력
s1=int(input("국어 점수를 입력 하시오: "))
s2=int(input("컴퓨터 점수를 입력 하시오: "))
s3=int(input("영어 점수를 입력 하시오: "))
s4=int(input("과학 점수를 입력 하시오: "))
print("평균: ",(s1+s2+s3+s4)/4)

print("%d %d %d %d" % (s1,s2,s3,s4))
print(f"{s1} {s2} {s3} {s4}")    #format의 약자, 대괄호 안의 변수의 형식을 정의한다.

height=int(input("높이를 입력 하세요: "))
bottom=int(input("밑변을 입력 하세요: "))
print("넓이는 %f 입니다." % (height*bottom/2))

#집가기전 연습 문제 풀이
from time import sleep    #time API에서 sleep을 사용하기 위해 임포트 함
import turtle
turtle.shape("turtle")

#1문제 출제 반지름을 입력받고 거북이로 그림 그리기
r1=float(input("반지름: "))
circle=r1*r1*3.14
print(circle)
turtle.circle(r1)
sleep(3)
turtle.clear
#2.사각형을 입력하고 그림 그리기
s1=float(input("가로를 입력 하시오: "))
s2=float(input("세로를 입력 하시오: "))
print(s1*s2)

turtle.reset
turtle.forward(s1)
turtle.right(90)
turtle.forward(s2)
turtle.right(90)
turtle.forward(s1)
turtle.right(90)
turtle.forward(s2)
sleep(100)

"""    9/27 실습 문제 풀이"""
for i in range(0,5,1):
    month=int(input("현재 몇월 인가요?"))    #12개월을 3개로 나누어 상반기 중반기 하반기로 분류
    if month>=1 and month<4:
        print("상반기 입니다.")
    elif month>=4 and month<8:
        print("중반기 입니다")
    elif month>=8 and month<=12:
        print("하반기 입니다.")
    else:
        print("1부터 12까지의 수를 입력하세요...")

a,b,c,d,e=0,0,0,0,0
for i in range(10):
    size=int(input("사이즈르 입력 하시오: "))
    if size<=85:
        a+=1
    elif size<=90:
        b+=1
    elif size<=95:
        c+=1
    elif size<=100:
        d+=1
    elif size>100:
        e+=1
print(f"{a}  {b}  {c}  {d}  {e}")

#옷 사이즈 측정하는 프로그램
size=list(range(10))

for i in range(10):
    num=int(input("치수를 입력 하시오: "))

    if num<=85:
        size.append("XS")
    elif num<=90:
        size.append("S")
    elif num<=95:
        size.append("M")
    elif num<=100:
        size.append("XL")
    else:
        size.append("XXL")
print(size.count("XS"),size.count("S"),size.count("M"),size.count("XL"),size.count("XXL"))


#삼각형 그리는 터틀 그래픽
import turtle

def Triangle_draw(x,y):
    turtle.goto(x,0)
    turtle.goto(x/2,y)
    turtle.goto(0,0)
    
def Triangel_area(x,y):
    return (x*y)/2

turtle.shape("turtle")
x=int(input("삼각형의 밑변의 길이를 입력하시오: "))
y=int(input("삼각형의 높이를 입력하시오: "))

Triangle_draw(x,y)
print("삼각형의 넓이: ",Triangel_area(x,y))

#홀짝 판별하는 시스템
def pzn(x):
    return x%2

N=int(input("짝수-홀수 판별을 원하는 수를 입력 하세요: "))

if pzn(N)==0:    
    print("짝수 입니다")

if pzn(N)==1:
    print("홀수 입니다.")

# 2개의 정수와 연산자를 입력받는 프로그램을 만들기
def fadd(x,y):
    sum=x+y
    return sum

def fsub(x,y):
    sum=x-y
    return sum

def fmult(x,y):
    sum=x*y
    return sum

def fdiv(x,y):
    sum=x/y
    return sum

x=int(input("첫번째 숫자를 입력하시오: "))
y=int(input("두번째 숫자를 입력하시오: "))

operate=input("연산사를 입력 하시오(예시: +,-,*,/): ")

if(operate=="+"):
    print(fadd(x,y))
if(operate=="-"):
    print(fsub(x,y))
if(operate=="*"):
    print(fmult(x,y)) 
if(operate=="/"):
    print(fdiv(x,y))





