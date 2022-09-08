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