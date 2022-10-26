#                                <함수의 기초 구조>
from ast import Num
from math import prod


def print_star10time():    #별을 10개 출력하는 함수를 만둠
    print("*"*10)

print_star10time()    #함수를 실행한다



#                   <2개의 매개 변수화 반환(return)이 존재하는 함수 구조>

def plus(x,y):
    return (x+y)

hap=plus(100,200)

print(hap)


#doc string: 함수에 대한 주석(추가설명)을 출력하는 역할 사용법: print(함수명.__doc__)

def mul(x,y):    #함수의 다음줄에 """사용해서 doc string적어줌
    """두 매개변수를 곱해서 반환해주는 함수 입니다"""    #나중에 doc string으로 출력할 예정
    return x*y

print(mul(10,20))
print(mul.__doc__)    # mul 함수에 관한 설명을 출력 해줌(복잡한 함수 정의시에 좋음)

# 함수에서 return값이 2개일수도 있다. (이때는 결과들을 튜플로 묶어서 반환됨)

def plusmul(x,y):
    return x+y,x*y

print(plusmul(10,10))     #튜플 형태로 반환이 된다.


#           <함수는 4가지 형태가 존재한다.>
# 1. 매개변수(입력값) X return X 인 경우

# 2. 매개변수(입력값) X return O 인 경우

# 3. 매개변수(입력값) O return X 인 경우

# 4. 매개변수(입력값) O return O 인 경우
# -보편적인 함수 형태이며, 전달인자(매개변수, return값)


#             < 다양한 자료형(int, 문자열, tuple) 삽입이 가능한 함수의 특징>
def print_two(x):
    return print(x*2)

print_two(5)   #정수 삽입
print_two("abc")   #문자열 삽입
print_two((1,2,3))    #튜플 삽입

#반환형이 없는 함수를 만들어 보자
def hap(x,y):
    print(f"{x}+{y}의 은 {x+y}입니다")

hap(10,20)
print(hap(10,20))    #return이 없기에 None이 출력 된다.



#                    < 입력값이 없는 형태를 만들어 보자>
def hi():
    return 'Hi 파이썬 프로그래밍'

had=hi()

print(had)

#                               <입력값과 반환값 모두 없는것>
def hi():
    print("hello")

hi()


#                                 <매개변수와 가매개변수란>

def student_info(name, phone, id_defalut="비공개"):    # id_defalut를 "비공개"로 설정함(이때 기본값 세팅됨)
    #기본값 세팅된 매개변수는 값이 없는 매개변수 앞으로 못온다 def student_info(name, id_defalut="비공개", phone) 은 신텍스에러 발생함
    print('이름: ', name)
    print('연락처: ', phone)
    print('주민번호: ', id_defalut)

student_info('김철수','010-1234-4567')    #매개변수 2개만 설정
# 이름:  김철수
# 연락처:  010-1234-4567
# 주민번호:  비공개          *****매개변수 지정한게 출력됨

student_info('김철수','010-1234-4567',"990819-17896546") 
# 이름:  김철수
# 연락처:  010-1234-4567
# 주민번호:  990819-17896546     *****새로 입력한 변수가 기존값을 대체함



#                              <가매개변수>

#  매개변수로 들어올 값이 몇개인지 모를때 사용됨(여러개를 튜플로 묶어줘서 사용함!!)
# 가매개변수에 들어온 값들을 더해주는 함수를 만들어 보자 

def allplus(*arg):    #매개변수앞에 *(에스테릭) 을 붙여주면 가매개변수라는뜻
    sum=0
    for i in arg:
        sum+=i
    return print(sum)


allplus(1,2,3,4,5)    # 1+2+3+4+5= 15 가 정상적으로 출력 된다.
allplus(1,2,3,4,5,6,7,8,9,10)    # 1~10까지의 합을 구한다


# 매개변수와 가매개변수를 같이 사용 가능하지만 조건1: 1개만 사용가능 조건2: 일반매개변수의 가장 뒤에 적어줘야함

# 활용 예제1


def gugudan(x,*y):
    for i in y:    # y는 투플의 형태로 차례대로 들어가게 된다.
        print(f"{x} * {i} = {x*i}")

gugudan(5,1,2,3,4,5)    
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25


#                                 <지역변수와 전역변수>

# 지역변수: 해당 블록에서만 생존함
# 전역변수 (static, 정적인 or 고정된): 소스코드 전체에서 생존함

#                                      <특징>
# 지역변수와 전역변수(static)의 이름이 같을수도 있음 
# 지역변수가 전역변수(static)보다 우선시됨!!!!
# 전역 변수(static)를 지역변수 대신 사용하고싶을때 전역변수를 변경하지 않고 사용만 하면 문제없음
# 전역변수를 함수 내에서 변경시에는 global 키워드를 붙여줘서 전역변수인걸 알려줘야함
# -함수내 전역변수 선언: global 변수_이름

# 예제 문제 1번

#def FA():
#     num=20    #지역변수 num
#     print(num)

# def FB():
#     print(num)    #나중에 전역변수가 들어감

# num=10    #전역 변수num
# FA()    #20 출력
# FB()    #10 출력


# 예제 문제 2번    ****global 좀 까다로움

def FC():    #이 함수가 만약 실행이 된다면 전역함수가 다시 정의된다는걸 유의
    global num    #함수내에서 전역변수를 바꿔서 전역으로  사용하겟다고 선언한것이다!!!
    num=20
    print("FC의 num값:",num)

num=10    # 전역변수

FC()    # 여기서 global num이 들어간 함수를 사용했기에 전역변수가 20으로 바뀌었다!

print("전역변수 num의 값:", num)    # 20이 출력된다, global num이 없으면 그냥 전역변수 10 출력됨

# 계산기를 함수를 사용해서 만들어 보자

# def calc(x,y,op):
#     result=0

#     if op=="+":
#         result=x+y
#     elif op=="-":
#         result=x-y
#     elif op=="*":
#         result=x-y
#     elif op=="/":
#         if var2==0:
#             return "error"
#         else:
#             result=x/y
#     elif op=="**":
#         result=x**y

#     return result


# res,var1,var2,oper=0,0,0,""

# while True:
#     oper=input("연신자를 입력 하시오 (+,-,*,/,**)  *q입력시 종료됨*: ")
#     if oper=='q':
#         print("연산을 종료 합니다.")
#         break
#     var1=int(input("첫번쨰 숫자를 입력 하시오: "))
#     var2=int(input("두번쨰 숫자를 입력 하시오: "))
#     res=calc(var1,var2,oper)
#     if res=="error":
#         print("0으로 나누면 오류가 발생 합니다.")
#     else:
#         print(f"{var1} {oper} {var2}= {res}")



#                      <lamda 함수 사용법>  *** 어려움***

# 형식: (lambda 인자 : 표현식)(조건)
# print(  (lambda x,y:x*y)(2,5)   )

# 특징1: 일회용 함수임(한번 사용하고 메모리에서 삭제), 일반 함수는 계속 남아있음
# 특징2: 어려개의 매개변수를 가질수 있으나, 반환값은 반드시 한개이다.
# 특징3: 함수가 필요한곳 어디서든 자유롭게 생성하고 사용이 가능 하다.


# 활용예제 1
def add(x,y):
    return x +y

print(add(2,5))    #2+5=7이 반환됨

#이번엔 lambda함수를 사용해보자

print((lambda x,y:x+y)(2,5))    #7이 출력됨,훨씬더 간단하다 훨

print((lambda x,y:x*y)(2,5))    #10이 출력 됨


# lambda의 추가 기능들 (반드시 뒤에 리스트가 들어오는걸 유의하자)

# filter(함수, 리스트): 리스트에 있는 원소들을 함수에 적용하여 결과가 참인 값들로 새로운 리스트 생성
# map(함수, 리스트): 리스트에 있는 원소들을 함수에 적용한 후 새로운 리스트에 저장하고 반환
# reduce(함수, 리스트): 리스트에 있는 원소들을 누적적으로 함수에 적용한후 반환
# (reduce는 from functools import reduce 적어줘야하고) 





# reduce 를 사용하지 않는 경우 팩토리얼 구하는법

product=1

mlist=[1,2,3,4]

for i in mlist:
    product*=i
print("팩토리얼 결과:",product)    #24 반환

# reduce를 사용하는 경우
from functools import reduce

product2 = reduce((lambda x,y:x*y),[1,2,3,4])    #24 반환(근데 reduce없어도 돌아감)
print("product2=",product2)


#예제 6-19
def cube(y):
    return y*y*y

g=lambda x:x*x*x   # 즉석에서 바로 함수 생성함
print("print(g(7)) = ", g(7))    #7의 세제곱

print("print(cube(5)) = ",cube(5))    #5의 세제곱

# lambda 함수와 함꼐 사용한 filter()함수
li=[5,7,22,97,54,62,77,23,73,61]
print("li = ",li)
final_list_filter = list(filter(lambda x:(x%2!=0),li))    # 홀수만 필터 씌워서 검색함
print("final_list_filter:", final_list_filter)


# lambda 함수와 함께 사용한 map() 함수

li=[5,8,10,20,50,100]
final_list_map=list(map(lambda x: x*2,li))   #map은 리스트가 map 함수 앞에 들어간다 map(int,input().split())
print("final_list_map: ", final_list_map)

#lambda 함수와 함꼐 사용한 reduce()함수

li=[5,8,10,20,50,100]
sum= reduce(lambda x,y:x+y,li)
print("리스트의 모든 합: ", sum)    

mul= reduce(lambda x,y:x*y,li)
print("리스트의 모든 곱: ", mul)

mstr= reduce(lambda x,y:y+x,"abcde")    #edcba가 출력이 된다.
print("리스트의 모든 합: ", mstr)

#31:02 부터 계속 정리 시작하자