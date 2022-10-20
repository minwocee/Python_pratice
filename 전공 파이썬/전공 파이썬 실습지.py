#2장 온라인 강의 정리

#예약어 키워드 목록을 출력 해보저
import keyword    
print(keyword.kwlist)    #이미 공식적으로 사용하고 있는 키워드 리스트를 출력한다.

import builtins
print(dir(builtins))    #이미 공식적으로 사용하고 있는 내장 함수명을 출력 해준다.(dir:디렉터리의 약자), abs부터 내장함수 이름들임

#True=100    (예약어를 변수명으로 사용해서 에러발생)
#6eleven=24    (숫자가 변수의 이름 맨앞에 들어가므로 오류가 발생한다.)

#간단한 삼격형의 넓이 구하는 방법
myheight=10
mybase=4
myarea = mybase * myheight
print("삼각형의 넓이는?: ",myheight)

#None 자료형이란?
no=None
print(no)
print(type(no))    #type()함수: 괄호에 들어간 변수명의 자료형 타입을 반환한다.

#bool형 자료형 이란?
b1=True
b2= False
print(type(b1))
print(type(b2))
#b3=true    #오류 발생(T를 대문자로 써야 예약어로써의 기능이 실행됨)
#print(type(b3))     

#실수 자료형 이란?
a=123
a=-178
a=0    #가장 마지막 변수 초기화 한것이 적용 된다.
print(a)
print(type(a))

팔진수=0o177    
print(int(팔진수))   #8진수-->10진수로 형변환 완료후 출력함

십육진수=0x8ff
print(int(십육진수))    #16진수-->10진수로 형변환 완료후 출력

#a=09  (오류 발생, 그냥 9로 대입해야 함)

부동소수점형변수=1.23e-2 #1.23 * 0.01 이랑 같음

e=2+3j    #실수+허수인 복소수e,  코딩시에는 복소수i 가 아닌 복소수j 로 사용한다.
print(e.real)    #실수부 출력
print(e.imag)    #허수부 출력
print(type(e))    #class complex 출력

#문자열(string)자료형의 표현법(큰따옴표와 작은 따옴표)
print("작은 따옴표 '를 출력")    #작은따옴표를 출력
print('작은 따옴표 "를 출력')    #큰따옴표를 출력
print("역슬래시를 이용해 \" 를 출력 해보자")

print("보안의 \n3요소")    #\n: 줄바꿈(엔터)
print("""기밀성
무결성
가용성""")    #큰따옴표 3개를 연속으로 사용해 3줄을 각각 출력해준다.

#이스케이프 문자의 다양한 활용법(시험떄 다시 확인해보자)
print('hello, \nworld!')
print('hello, \tworld!')
print('hello, \\world!')
print('hello, /world!')
print('welcome to, my\'world!')
print('\"\"')
print('hello, \rworld!')    #캐리지 리턴뒤에붙은 문자열이 가장 앞으로 옴(기존 문자랑 겹칠시 인덱스 부분만큼 대체함)
print('12345 \r678')    
print('hello, \fworld!')
print('hello, \aworld!')
print('hello, \bworld!')
print('hello, \vworld!')
print('8진수 -> \141')    #알파벳 a가 해당
print('16진수-> \x61')    #알파벳 a가 해당
print('유니코드 : \N{LINE FEED}')    #line feed: 줄바꿈 하라는 의미
print('16비트 16진수로 유니코드 표현: \u0061')    #알파벳 a가 해당
print('32비트 16진수로 유니코드 표현: \u00000061')    #알파벳 a가 해당


#문자열 포멧팅(자릿수 설정하기)
print("본인의 나이는 %d 이다" % 24)
print("본인의 이름은 %s 이다."%'천민우')
print("내 전공은 %s 이고 학번은 %d 이다."%('컴퓨터 공학과',20180876))

print("현재 태풍이 올 확률은 %d %%이다."%(100))    # %% 입력시 %문자 그대로 출력이 가능하다.
print("내 수명은 %5.2f 이다." % 85.1234)    # %5.2f 의 의미: 총 5자리의 수를 출력하는데 그중 2자리는 소수점 아래로 사용한다
print("나의 키는 %6.3f 이다." % 177.123456)    # %6.3f : 실수중 6자리를 사용하는데 그중 3자리는 소수점 아래표기시 활용한다.
print("코드네임 %03d 이다." % 7)    #03d의 의미: 3자리 까지 정수를 표현하는데 만약 빈자리가 생기면 0으로 채워라는 의미
print("00년생의 주민번호 %06d 이다." % 908)    #06d의 의미: 6자리 정수를 출력하는데 빈자리가 생기면 0으로 채워라

print("오늘은 몇일?: %s"%7)    #뒤에오는 정수를 문자열로 형변환 해서 들어간다.
print("오늘의 강수량은 ?: %s"%11.7)    #뒤에오는 정수를 문자열로 형변환 해서 들어간다.

print("%20s" % "컴퓨터 공학과")    #오른쪽에 붙어서 출력
print("%-20s" % "컴퓨터 공학과")    #왼쪽에 붙어서 출력
print("원주율 값: ㅣ%10.5fㅣ"%3.141592175)    #앞에 공백 3개 두고 출력된다.
print("원주율 값: ㅣ%-10.5fㅣ"%3.141592175)    #왼쪽에 붙어서 공백이 없어진다.(소수점 자리 뒤에 공백 3칸 추가됨)
print("원주율 값: ㅣ%0.5fㅣ" % 3.141592175)    #정수 부분은 유지하고, 소수점 아래 5자리 까지만 출력(소수점 슬라이스)

#문자열 연결하기
print("안녕"+"하세요")
print("반갑습니다","교수님","출력합니다~")
print(("hello"+"world")*3)



""" ***************************3장 실습정리장****************************"""

#인덱싱의 기초

from operator import index


mystr="Computer Programing"    #문자열형 변수를 넣어준다.(이때 첫번째 글자는 인덱스 0번 마지막 글자는 인덱스 19번or -1번 )
"""0~19번 인덱스 번호 == -17~-1 인덱스 번호와 같다"""

print(mystr[0],mystr[1],mystr[2],mystr[3],mystr[4],mystr[5])    #각 인덱스의 글자 C o m p u t 가 출력 된다.(이때 쉼표를 사용해서 공백을 추가)) 

print(mystr[0]+mystr[1]+mystr[2]+mystr[3]+mystr[4]+mystr[5])     #+를 사용해 문자을 붙여주므로 Comput 가 출력이 된다.

print(mystr[0:8])    #인덱스 슬라이싱, 인덱스 0번부터 7번까지 출력해준다. (이때 마지막 범위인 인덱스[8]번은 제외인것을 기억 하자)

print(mystr[:8])    #8번째 인덱스 전까지 문자열을 출력하는 의미

print(mystr[0:])    #0번째 인덱스부터 끝까지 모두 출력 한다는 의미 이다.

print(mystr[:])    #범위가 다 생략되어 있으면 모든 글자를 출력 한다.

#문자열 함수 사용법
"""
capitalize(): 괄호안 단어의 첫글자를 대문자로 변환하혀 반환
count(x): x가 문자열 안에서 몇번 등장하는지 개수를 세고 반환
find(x): x가 문자열 안에서 처음 나오는 위치를 찾아서 반환 한다.(만약 없으면 -1을 반환한다.) 이때 인덱스 번호로 말하니 주의(0부터 시작 함)
rfind(x): x를 문자열 뒤에서 부터 찾아 반환 한다.
index(x): x가 문자열 안에서 처음 나오는 위치를 반환 한다.(만약 없으면 오류가 발생)
lower(): 문자열의 알파벳을 모두 소문자로 치환
upper(): 문자열의 알파벳을 모두 대문자로 치환

"""

k1="hello World"

print(k1.capitalize())    #첫 글자 h 가 H 로 변환후 출력 됨

print(k1.count("o"))     #알파벳 o 가 2번 사용됨

print(k1.find("W"))    #W의 위치인 인덱스 번호 6번이 출력 됨

print(k1.rfind("l"))     #뒤에서 부터 알파벳 l을 찾고 인덱스 번호를 출력 한다.

print(k1.index("W"))    #W의 위치인 인덱스 번호를 찾는다.(find와 기능은 같다.)

print(k1.upper())     #문자열을 모두 대문자로 바꿔주고 출력

print(k1.lower())    #문자열을 모두 소문자로 바꿔주고 출력


"""     또다른 문자열 함수들
replace(a,b): 문자열에서 a를 찾아 b로 변경해준다.
strip(): 문자열 좌우의 공백 문자를 없앤 것을 반환한다.
lstrip(): 문자열 왼쪽의 공백 문자를 없앤것을 반환한다.(left strip)
rstrip(): 문자열 오른쪽의 공백 문자를 없앤 것을 반환한다.(right strip)
split(x): x를 기준으로 문자열을 여러개로 나눈다.
splitlines(): 개행을 기준으로 문자열을 여러개로 나눈다.
join(strs): 시퀸스(strs)에 포함된 문자열들을 이 문자열을 구분자로 연결한다.
isalpha(): 문자열이 문자(알파벳, 한글 등 )으로만 되어 있는지 검사 한다. 문자만
isnumeric(): 문자열이 숫자로만 구성 되어 있는지 검사한다. 숫자만 
isalnum(): 문자열이 문자와 숫자로만 구성 되어 있는지 검사한다. 문자&숫자만
format(): 데이터를 양식화 한다. (추후 값을 대괄호 안에 대입한다고 보면 된다.)---예시 활용 
len(): 문자열의 길이를 반환 한다.
ord(): 문자의 아스키 코드를 반환 한다.
hex(): 정수를 입력 받아서 16진수로 바꿔준다.
oct(): 정수를 입력 받아서 8진수 문자열로 변환
chr(): 아스키 코드를 입력 받아서 그 코드에 해당하는 문자를 반환 한다.
"""

k2= "sungkul computer"

print(k2.replace("u", "12345"))     #모든 u 를 12345로 대체함

print(k2.strip())    #양쪽의 공백문자를 제거 함

print(k2.lstrip())    #왼쪽의 공백문자를 제거 함

print(k2.rstrip())    #오른쪽의 공백문자를 제거함

print(k2.split())    #괄호안(공백)을 기준으로 문자열을 구분 해준다. (이때 공백 문자는 생략하고 구분한다.)

print(k2.split("u"))    #알파벳 u 를 기준으로 문자열을 구분 해준다. (이때 u는 생략하고 구분한다.)

print("www.sungkul.ac.kr".split('.'))    # . 을 기준으로 문자열을 분리해서 출력해줌

poem=""" 위국헌신
군인본분
나라가 위기에 빠지면
군인으로써 목숨을 바친다"""

print(poem.splitlines())    #한행(줄)을 기준으로 문자열을 분리해서 출력한다.

print('!'.join(k2))    #문자 사이 사이 마다 느낌표를 삽입해준다.(맨앞과 맨뒤에는 안들어감)

print("Helloworld".isalpha())    #문자로만 구성이 되어있는지 확인한다.(공백문자가 있으면 False 로 뜬다.)

print("20180876".isnumeric())    #문자열이 숫자로만 구성 되어 있는지 확인한다.

print("123 abc".isalnum())    #문자열이 문자와 숫자로만 구성되어 있는지 확인한다.(공백문자는 False로 뜬다.)

"""format() 활용"""
str99= "department of {}"    #대괄호 자리에 삽입을 예정
print(str99.format("computer"))    #format을 사용해 computer 를 그자리에 넣어준다.

str100= "depart {1} {0}"    #인덱스{0}에 "Hello", 인덱스 {1}에 "world"가 들어감(인덱스 번호를 지정해서 대각선 방향으로 둘이 들어감) 
print(str100.format("Hello", "world"))

str3= "hello {str1} {str2}"
print(str3.format(str1="wor", str2="ld"))    #바로 변수 만들어서 포멧팅 해줌

strr = "성결대학교 {:20}"    #20칸을 확보해주겠다는 의미(문자열이 20칸보다 짧으면 공백으로 채워줌)

print(strr.format("컴퓨터 공학과") + '/')    #/슬래시를 사용해 마지막 글자가 어디인지 표시해줌

strr = "성결대학교 {:<20}"    #20칸 공간내 왼쪽으로 정렬 
print(strr.format("컴퓨터 공학과") + '/')

strr = "성결대학교 {:>20}"    #20칸 공간내 오른쪽으로 정렬
print(strr.format("컴퓨터 공학과") + '/')

strr = "성결대학교 {:^20}"    #20칸 공간내 가운데로 정렬 
print(strr.format("컴퓨터 공학과") + '/')

strr = "성결대학교 {:%<20}"    #20칸 공간내 왼쪽으로 정렬(정렬후 남는 부분은 %로 채운다.) 
print(strr.format("컴퓨터 공학과") + '/')

strr = "성결대학교 {:$>20}"    #20칸 공간내 왼쪽으로 정렬 (정렬후 남는 부분은 $로 채운다.)
print(strr.format("컴퓨터 공학과") + '/')

strr = "성결대학교 {:#^20}"    #20칸 공간내 왼쪽으로 정렬 (정렬후 남는 부분은 #로 채운다.)
print(strr.format("컴퓨터 공학과") + '/')

pi= "{:.7f}"    #소수점 아래 7자리 까지 표기
print(pi.format(3.141592653))
pi= "{:10.4f}"    #전체 10자리로 설정하되 소숫점 아래는 4자리 까지만 표기한다.
print(pi.format(3.141592653))

L1="computer love me"
L2=[2019, 2020,2021]

print(len(L1))    #문자열의 길이 반환

print(len(L2))    #리스트의 요소의 개수를 반환

print(ord('a'))     #a의 아스키 코드를 반환
print(ord('ㄱ'))    #ㄱ의 아스키 코드를 반환
print(chr(97))    #아스키 코드 97번을 문자로 반환(a)
print(chr(12593))    #아스키 코드 12593번을 문자로 반환(ㄱ)

print(hex(1))    #정수1을 16진수로 변환
print(hex(2))    #정수2를 16진수로 변환
print(hex(3))    #정수3을 16진수로 변환
print(hex(10))    #정수10을 16진수로 변환

print(oct(1))    #정수1을 8진수로 변환
print(oct(2))    #정수2을 8진수로 변환
print(oct(3))    #정수3을 8진수로 변환
print(oct(10))    #정수10을 8진수로 변환

#형변환(int(), float().str()), 자료형을 활용할때 동일한 자료형이 아니면 type error 가 발생하므로 형변환을 실행

print(str(100)+'1')    #문자열 형변환 실행

print(int("100")+1)    #정수형 형변환 실행

print(float(100))    #실수형 형변환 실행


"""4주차 2022.09.21작성"""


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


"""
22.10.02 작성한 실습5주차
"""
#if문 활용예제
k=int(input("1부터 100사이의 정수를 입력 하시오: "))

if k<100:
    print("입력한 정수가 100보다 작음")
    print(f"a = {k}")

if k>=100:
    print("프로그램 종료") 

#예제 4-2 if-else 활용

k=int(input("1부터 100사이의 정수를 입력 하시오: "))

if k<100:
    print(f"입력한 a의 값은 {k}이며 100보다 작음")
    print("프로그램 종료") 
else:
     print(f"입력한 a의 값은 {k}이며 100보다 크다")
     print("프로그램 종료") 


#중복 if-else문 활용
k=int(input("1부터 100사이의 정수를 입력 하시오: "))
if k>=0:
    if k==0:
        print("입력한 정수는 0임")
    else:
        print("입력한 정수는 %d이고 양수임"%k)
else:
    print("입력한 정수는 %d이고 음수임"%k)

#나이와 점수에 따라 합/불을 정하는 프로그램
age, score=map(int,input().split())

if age>20:
    if score>80:
        print("합격입니다")
    else:
        print("점수가 너무 낮아 불합격 입니다.")
else:
    print("나이가 너무 어려서 불합격 입니다.")


#-10에서 10까지의 정수를 입력받고 크기를 측정한다.
for i in range(5):
    i=int(input("-10에서 10 사이의 정수를 입력 하세요: "))
    
    if i<-10:
        print(f"입력한 정수는 {i}이고 -10보다 작음")
    elif i>=-10 and i<=10:
        print(f"입력한 정수는 {i}이다.")
    elif i>10:
        print(f"입력한 정수는 {i}이고 10보다 크다")
    elif i==0:
        print("입력한 정수는 %d이다."%i)


#리스트에 특정 요소가 있으면 작동하는 프로그램 생성(if 요소 in 리스트)
pocket=[]
pocket.append(input("내 지갑에 현재 있는것은? (money, card...) : "))
if "money" in pocket:
    print("택시타고 가자")
elif "card" in pocket:
    print("버스타고 가자")
else:
    print("아무것도 없으니 걸어가자...")


#학생들의점수에 따른 학점을 부과하는 프로그램을 작성 해보자:
score=int(input("학생의 점수를 입력 하시오: "))

if score>=90:
    grade='A'
elif score>=80:
    grade='B'
elif score>=70:
    grade='C'
elif score>=60:
    grade='D'
else:
    grade='F'
print("당신의 점수는 {0} 이며 등급은 {1} 입니다.".format(score, grade))

#윤년을 계산하는 프로그램 만들기
year=int(input("윤년 계산을 원하는 연도를 입력하시오(예시: 1999, 1989 ....): "))

if((year%4==0) and (year % 100 !=0) or (year%400==0)):
    print(year,"은 윤년이 맞습니다.")
else:
    print(year,"은 윤년이 아닙니다.")

#for 문을 활용한 팩토리얼을 계산하는 법

N=int(input("팩토리얼 계산을 원하는 0 이상의 정수를 입력 하시오: "))

for i in range(N):
    if(N==0):    #0!=1이므로 이 경우는 특수하게 처리한다.
        sum=1
        break
    sum=sum*i

print("입력한 정수는",N,"이며 팩토리얼 연산 결과는 :",sum)

#1~100까지의 홀수, 짝수의 합
even,odd=0,0
print("1부터 100까지의 짝수항, 홀수항의 합을 구해보자\n")
for i in range(1,101):
    if(i%2==0):    #짝수인 경우
        even+=i
    else:
        odd+=i
print("짝수항의 합:",even)
print("홀수항의 합:",odd)

#range를 활용해서 리스트를 생성하는법
L1=list(range(10))    #이러면 리스트에 0~9까지 들어감
print(L1)
print(list(set(L1)))    #이건 중복을 제거한후 다시 리스트로 변환해서 넣어주는 과정


#이중으로 for 문을 사용해 구구단을 출력하자
for i in range(2,10):
    for k in range(1,10):
        print(f"{i} * {k} = {i*k}", end=" | ")
    print("")


#일반 리스트와 튜플의 값을 출력해보자
Lis1=["one","two","three"]
for i in range(Lis1):
    print(Lis1)
Lis2=[(1,5),(2,6),(3,7)]
for(a,b) in Lis2:
    print(a+b)

#일반 리스트와 튜플의 값을 출력해보자
Lis1=["one","two","three"]
for i in Lis1:
    print(i)


Lis2=[(1,5),(2,6),(3,7)]    #튜플 형태로 리스트에 저장이 되어 있다.
for(a,b) in Lis2:
    print(a+b)

#학생의 점수
score=[90,20,10,100,80]
for i in score:
    if i>=70:
        print(f"{score.index(i)+1}번 학생은 합격이며 점수는 {i}입니다.")
    else:
        print(f"{score.index(i)+1}번 학생은 탈락이며 점수는 {i}입니다.")


#continue 를 사용한 반복문건너뛰기

score=[90,20,10,100,80]
for i in score:
    if i<70:
        continue    #불합격자들은 건너뛰고 합격자만 메세지를 출력함
    print(score.index(i)+1,"번 학생은",i, "점으로 합격입니다.축하드립니다.")

#트리 만드는 방법1(반복문 2개 사용)
N=int(input("숫자를 입력 하시오: "))
for i in range(1,N+1):
    for k in range(i):
        print("*",end="")
    print("")

#트리 만드는 방법2(반복문 1개 사용)
N=int(input("숫자를 입력 하시오: "))
for i in range(1,N+1):
    print("*"*i)

#for문 1번 사용해서 역으로 만드는 트리 생성하기

x=int(input("가로의 길이: "))

for _ in range(x,0,-1):
    print("x"*_)

#직사각형의 가로와 세로를 입력받고 점을 찍으주는 프로그램

x=int(input("가로의 길이: "))
y=int(input("세로의 길이: "))

for i in range(x):
    for k in range(y):
        print("x", end="")
    print('')


#더 간단하게 만드는 직사각형의 가로와 세로를 입력받고 점을 찍으주는 프로그램

x=int(input("가로의 길이: "))
y=int(input("세로의 길이: "))

for _ in range(y):
    print("*"*x)

#가운데로 정렬해서 만드는 트리를 만들어 보자(어려움)

x=int(input("밑변의 길이: "))

for i in range(1,x+1):
    print(((x-i)*' ')+'x '*i)    #빈칸의 배열+점의 배열을 합한 원리이다.

#5의 배수를 제거해서 출력하는 프로그램

N=int(input("출력을 원하는 숫자를 입력 하시오: "))

for i in range(1,N+1):
    if not (i%5==0):    #if not을 사용하 특정조건이 아닐시 실행하는 조건을 걸어줌 if (i%5==0)이면 continue로 써도 가능
        print(i,end=" ")

#예제 4-27 비트연산해서 출력하는것 (어려움)
x=int(input("숫자를 입력 하세요: "))
a=1

for i in range(0,11):
    print('{0:6,}'.format(a<<i),end=' ')
print()


#while 활용법
x=int(input("출력 횟수를 지정 해주세요: "))
sum=0
while(sum<x):
    print("Hello world")
    sum+=1

#4-30 예제
i,hap=0,0
num1=int(input("시작 값을 입력 하시오: "))
num2=int(input("끝값을 입력 하시오: "))
num3=int(input("증감값을 입력 하시오: "))
i=num1

while i<num2+1:
    hap+=i
    i+=num3
print("{}에서{}까지 {}씩 증가시킨 값의 합계: {}".format(num1,num2,num3,hap))


#while 활용법2
import random
i,count=0,0
while i !=1:
   i=random.randint(1,101)
   print(i)
   count+=1
print("드디어 끝났네요 시도횟수: ", count) 

#무한루프 활용

sum=0

while(True):
    a=int(input("첫번째 수를 입력 하시오 (0을 입력하면 종료됨): "))
    if(a==0):
        break
    b=int(input("두번째 수를 입력 하시오: "))
    print("두수의 합: {}".format(a+b))

#while 활용 학점 분류

while(True):
    score=int(input("학생의 점수를 입력 하시오: "))
    if(score>100 or score<0):
        print("0~100 사이의 정수를 입력 해주세요(등급 분류 불가)")
        print('_______________________________________')
        continue
    if(score>=90):
        print("{}점 이므로 A 학점 입니다.".format(score))
        print('_______________________________________')
    elif(score>=80):
        print("{}점 이므로 B 학점 입니다.".format(score))
        print('_______________________________________')
    elif(score>=70):
        print("{}점 이므로 C 학점 입니다.".format(score))
        print('_______________________________________')
    elif(score>=60):
        print("{}점 이므로 D 학점 입니다.".format(score))
        print('_______________________________________')
    else:
        print("{}점 이므로 F 학점 입니다.".format(score))
        print('_______________________________________')


#약수의 개수를 구하고 약수를 출력해주는 프로그램을 만들자(좀 까다롭지만 유용)
while True:
    num=int(input("정수를 입력 하시오(0은 종료키): "))
    if not num:
        break    #정수가 아니면 반복문을 탈출하는듯
    if num<0:
        print("양의 정수를 입력하시오")
        continue    #다시 처음으로 돌아간다.
    count=0    #약수의 개수를 세어주는 변수를 선언 한다.
    for i in range(1,num+1):
        if num%i==0:
            print('{0:5}'.format(i),end=' ')    #앞에 4칸을 띄워줌(마지막 인덱스인 [4]에 i가 들어가고 나머지는 공백으로 채움)
            count+=1
    print()
    print("{0}의 약수의 개수: {1}개 입니다.\n".format(num,count))
