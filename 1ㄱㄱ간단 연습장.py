

"""(4주차 사이버 강의) #산술 연산자 모음"""


# print(1+1)
# print(1-5)
# print(5/2)
# print(5//2)    #몫나눗셈
# print(2**10)    #2의10승 거듭제곱 실행
# print(15%4)    #15나누기 4의 나머지 3
# print(4.3-2.7)    #1.6이 나와야 하는데 실수의 저장 방식에의해 1.5999999999999996 가 출력됨(나중에 알아보자)

# s1= 'computer'
# s2= 'engineering'

# print(s1+' '+s1+'.')
# print(s2*3)
# print('-'*20)
# l1=[1,2,3]
# l2=[4,5,6]
# print(l1+l2)
# print(l1*3)

# a=int(input("첫번쨰 정수를 입력하시오: "))
# b=int(input("두번쨰 정수를 입력하시오: "))

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)

# print(f"{a} + {b} = {a+b}")    #앞에 f(format)를 붙이면 좀더 간단
# print("{0} + {1} = {2}".format(a,b,a+b))    #정석의 format 방식

# print(f"{a}-{b}")
# print(f"{a}*{b}")
# print(f"{a}/{b}")
# print(f"{a}//{b}")
# print(f"{a}%{b}")
# print(f"{a}**{b}")

print(9/-2)    #-4.5
print(9//-2)    #-5
print(9%-2)    #나머지 연산 결과는 -1, (-5(몫)*-2 + -1(나머지)), 나누는수(-2)에 뭘 곱해야 9가되는지 생각

print(-9/2)    #-4.5
print(-9//2)    #-5
print(-9%2)    #나머지 연산 결과 +1, (-5(몫)*2 + 1(나머지)), 나누는수(2)에 뭘 곱해야 -9가되는지 생각


#복합 대입 연산자 모음(연산한 결과를 다시 변수에 넣는게 포인트이다.)
x=5
x+=2
print(x)

x-=2
print(x)

x*=2
print(x)

x/=2    #여기서 x가 실수형으로 변경 됨
print(x)

x**=2
print(x)


x //=2
print(x)

x%=2
print(x)

# # 예제 3-7 yyyymmdd를 입력받고 출력
# birth=int(input("yyyyddmm을 입력하시오: "))
# year=birth//10000
# month1=birth%10000//100
# date=birth%100

# print(year,month1,date)

# a,b,c=map(str,input("yyyymmdd를 입력하시오: ").split())
# print("%s년 %s월 %s일"%(a,b,c))

# #예제 섭씨온도를 화씨온도로 변환

# c=float(input("섭씨온도('C)를 입력 하세요: "))
# print("화씨온도 변환 결과: {}".format((9/5)*c+32))


#관계연산자 활용법
print(2000>2001)
print(2000<2001)
print(2020==2021)
print(2020!=2021)
print('abcd'=='abcd')
print(2020==2020.0)    #True 출력 됨
print(2020 is 2020.0)    #is 는 같은 객체를 가르키는건지 확인할때 사용

print('a'<'b')    #유니코드표 참고해서 결과 출력
print('ab'<'abc')

no1= 1
no2 =1
st1='life'
st2='life'

print(no1==no2)
print(no1 is no2)    #주소값이 같은지 비교(래퍼런스)
print(st1==st2)
print(st1 is st2)    #주소값이 같은지 비교함(id)
print(id(st1))

# #논리연산자 활용
# num=int(input("조건을 확인하고자 하는 수를 입력 하세요: "))
# print((num>2020) and (num<2030))     #두가지 조건을 모두 만족해야 True르 반환 하는 and 논리 연산자

# #윤년 계산 프로그램
# year=int(input("연도를 입력 하세요: "))
# print((year%4==0) and (year%100 !=0) or (year%400==0))    #윤년을 판별하는 3개의 조건


#비트(bit)연산자 활용****좀 어려운 부분 비트의 각 자리수마다 연산을 진행한다고 생각하면 편함
"""
&: 비트단위 and 연산
|: 비트단위 or 연산
^(xor): 비트단위 xor 연산(두개의 값이다를 때 참인 xor 연산)
~: bit 단위로 not 연산(1의 보수)를 한다.
<<: 왼쪽 쉬프트 연산자(변수의 값을 왼쪽으로 저장된 비트 수만큼 이동, 1bit이동시 이진수 저장방식이기 때문에 2배씩 늘어난다.) (a<<b: a*2^b)
>>: 오른쪽 쉬프트 연산자(변수의 값을 오른쪽으로 저장된 비트 수만큼 이동, 1bit이동시 이진수 저장방식이기 때문에 2배씩 줄어든다.) (a>>b: a/2^b)
"""
a=int(input("첫번째 수를 입력 하세요: "))
b=int(input("두번째 수를 입력 하세요: "))
print(f"a = {a} -> {bin(a)}")    #bin()함수: 입력한 10진수를 2진수를 변환 하여 출력함
print(f"b = {b} -> {bin(b)}")    
print(f"a & b = {a&b} -> {bin(a&b)}")
print(f"a | b = {a|b} -> {bin(a|b)}")
print(f"a ^ b = {a^b} -> {bin(a^b)}")
print(f"~a = {~a} -> {bin(~a)}")

c=int(input("숫자를 입력 하세요: "))
print()
print("<<연산 실행결과")
c=c << 1    #비트 왼쪽으로 한칸 증가(2^1 배증가)
print(f"{c} -> {bin(c)}")
c=c << 2    #비트 왼쪽으로 두칸 증가(2^2 배 증가)
print(f"{c} -> {bin(c)}")
c=c << 3    #비트 왼쪽으로 3칸 증가(2^3 배 증가)
print(f"{c} -> {bin(c)}")

print(">>연산 실행결과")
c=c >> 1    #비트 오른쪽으로 한칸 증가(2^-1 배증가)
print(f"{c} -> {bin(c)}")
c=c >> 2    #비트 오른쪽으로 두칸 증가(2^-2 배 증가)
print(f"{c} -> {bin(c)}")
c=c >> 3    #비트 오른쪽으로 3칸 증가(2^-3 배 증가)
print(f"{c} -> {bin(c)}")

#2의 보수를 이용한 뺄셈
a1= int(input("첫번째 수를 입력 하시오: "))
b1= int(input("두번째 수를 입력 하시오: "))
c1=a1-b1
d1=a1 +(~b +1)
print(f"a1 - b1 = {c1}")
print(f"a1 + (~b + 1) = {d1}")

