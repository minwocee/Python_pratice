import turtle
from time import sleep


def myturtle(x,y):
    turtle.goto(x,0)
    turtle.goto(x/2,y)
    turtle.goto(0,0)
    sleep(5)

turtle.shape("turtle")
x,y=map(int, input("삼각형의 밑변과 높이를 입력하시오(예시: 3 8):").split())

myturtle(x,y)
