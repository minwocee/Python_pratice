'''
import time


# 현재 시간의 Hour을 불러준다.
hour = int(time.strftime("%H", time.localtime(time.time())))

if hour < 12:
    if hour < 6:
        print("00시 ~ 06시 사이 입니다.")
    else:
        print('06시 ~ 12시 사이 입니다.')
else:
    if hour < 18:
        print("12시 ~ 18시 사이 입니다.")
    else:
        print("18시 ~ 24시 사이 입니다.")


# 윤년 판별기
year = int(input(""))

if ((year % 400)==0) or (year % 100 !=0 and year %4 ==0):
    print(f"{year}년은 듄연 입니다.")
else:
    print(f"{year}년은 윤년이 아닙니다.")




array=[10,'python', True, (1,2)]

arr=array[::-1]    #거꾸로 뒤집음

print(arr)



for i in range(0,11,1):
    if i%2==0:    #짝수가 맞으면 실행한다.
        print(i)




i=2000

while i<=2023:
    
    if (i%400 ==0) or (i % 100 !=0 and i %4 ==0):
        print(i)
    i +=1
    

for i in range(2000,2023):
    if (i%400 ==0) or (i % 100 !=0 and i %4 ==0):
        print(i)


def nickname(nick):
    if nick =='바보':
        print("저는 바보가 아닙니다.")
        return 

    print(f'나의 별명은 {nick} 입니다.')


nick =input()
nickname(nick)


def add(a,b):
    return [a,b,a+b]

ary=add(1,2)
print(f"{ary}{}")


#에스테리크 사용해서 매개변수가 여러개를 받고 싶은 상황을 해결한다.
def cal(choice, *ary):
    if choice =='add':
        ex =0
        print(type(ary))
        for i in ary:
            ex +=i
        return


    elif choice =='mul':
        ex =1
        for i in ary:
            ex *= i
        return ex

print(cal('add', 1,2,3,4,5,6,7,8,9,10))


for i in range(1,11):
    print(i,end=' ')



# 사용자 입출력
name = input()
age = int(input())

print(f"저는 {age}세 {name}입니다.")    


# Class

class Calculator:
    def __init__(self):
        self.result =0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -=num
        return self.result

calll_1=Calculator()
print(calll_1.add(3))
print(calll_1.add(5))

print(calll_1.result)



# 상속관계

# 부모
class Calculator:
    def __init__(self):
        self.result =0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -=num
        return self.result

# 자식(부모의 능력 + 자신만의 능력)
class extra(Calculator):
    def mul(self,num):
        self.result *=num
        return self.result

    def add(self, num):
        self.result +=num*2
        return self.result

call =extra()
call.add(3)
call.mul(3)
print(call.result)


import mod1    # 불러오다.

print(mod1.add(1,2))
print(mod1.mul(1,2))


#모듈 생성과 관리
from mod1 import add

print(add(1,2))

from mod1 import *    # 전체 함수를 불러오겠다. (이렇게 하면 mod1.XXX 이런 형식을 쓸 필요 없음)



circle1 = circle()

print(circle1.circle_area(5))
'''

#예외처리

a=int(input())
b=int(input())


try:
    result =a/b
    print(result)

except ZeroDivisionError:    #구문에서 오류 발생시 실행한다.
    print('0으로 나눌수 없습니다.')
else:#오류가 나지 않으면 실행함
    print("오류가 없이 잘 끝났네요")
finally:# 오류 발생 여부에 관계없이 실행
    print('프로그램이 종료 되었습니다.')
