import turtle
from time import sleep

def Triangle_draw(x,y):
    turtle.goto(x,0)
    turtle.goto(x/2,y)
    turtle.goto(0,0)
    sleep(5)

def Triangel_area(x,y):
    return (x*y)/2

turtle.shape("turtle")
x,y=map(int, input("삼각형의 밑변과 높이를 입력하시오(예시: 3 8):").split())

Triangle_draw(x,y)
print("삼각형의 넓이: ",Triangel_area(x,y))
