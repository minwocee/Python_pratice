#교양 파이썬 22.09.06  응용문제1
from turtle import *
color('red', 'yellow')

begin_fill()

while True:
    forward(100)
    left(170)
    if abs(pos())<1:
        break
end_fill()