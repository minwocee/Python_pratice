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

