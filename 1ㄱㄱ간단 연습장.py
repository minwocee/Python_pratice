
from time import sleep
import turtle
turtle.shape("turtle")

#1문제 출제 반지름을 입력받고 
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





