#[파이썬의 기초 2022.08.18.16:00 작성]

#형식: print("문자열")    의미: 괄호내부의 입력한 문자열을 출력한다.
print("Hello Python world!")    

#Hello 의 문구를 10번 반복해서 출력한다.
print("Hello"*10)    

#띄어쓰기없이 문자열을 붙여준다. +사용
print("Hello"+"Python"+"World")    

#단어들끼리 띄어쓰기를 해서 출력.  ,사용
print("Hello", "Python", "World")    

#3곱하기 3의 결과를 출력한다.
print(3*3)    

#형식: type(변수)    의미: 괄호 내부의 자료형을 알려주는 함수.
type(12.34)    

#형식: id(변수)    의미: 괄호 내부의 변수의 주소값을 알려준다.
x=3
id(x)    

#[사각형의 면적을 구하는 문제]
a=10; b=30; print("사각형의 면적:", a*b)

#[몫과 나머지 연산]
p=7; q=4
print("7/4의 몫:", p//q)
print("7/4의 나머지:", p%q)

#파이썬에서 사용 가능한 할당 연산들
x=y=z=0    #x,y,z를 한번에 0으로 초기화.
x,y,z,=1,2,3    #x=1; y=2; z=3과 같은말이다.
x,y=y,x    #x와 y의 값을 교환해주는 수식.

#[다양한 복합 대입 연산자]
#x+=y x-=y x/=y x%=y

#지수 계산
print(2**5)    #2의 5승을 계산, 형식:  x**y  의미:  x의 y승 이라는 뜻

#은행 복리 계산
a=100    #원금
r=0.05   #이자율 0.05퍼센트
year=10    #10년을 맡긴다.
print(100*(1+r)**10)    #보통은 지수의 곱이 가장 먼저 계산이 이루어짐
#우선순위를 기억하기 어렵다면 괄호를 사용하자 (_)

#[변수의 자료형을 변환]
a=3.14    #실수형으로 a를 설정
a1=int(a)    #실수a를 정수형로 변환해줌
print(a1)    #정수 3 출력

#[tip] 컨트롤키+방향키: 한줄씩 아래로 화면을 내리거나 올린다, 알트키+방향키: 윗줄과 아랫줄의 내용을 바꾼다. 

#[반올림 함수 round()]
price=12345
tax= price*0.075
print(tax)
tax=round(tax,2)    #소수점 아래 2번쨰 자리 까지만 변수에 넣는다.(3번째 자리에서 반올림 이루어짐)
print(tax)

#[큰따옴표와 작은 따옴표의 사용]
print("넌 '이미' 죽어있다.")    #문자열 내의 작은 따옴표가 정상적으로 출력이 이루어 진다.

#[문단 주석 """ ]
"""
난 집에 너무 가고 싶지만
아직 공부를 덜 했기 떄문에 
갈 수가 없다 ㅠㅠ
"""

#[숫자와 문자열의 차이]
print(100+200)    #300 출력
print("100"+"200")    #100200 출력
print("topgun"+str(2))    #정수2를 문자열로 변환하여 붙여주었다.
price=int("100")    #문자열 100을 정수 100으로 변환을 완료 하였다.
print(price)

#[특수한 문자열]
"""\n \t \\ \" \'"""

#[문자열이 배열에 들어가는 원리]
hername= "woo young woo"
print(hername[0])    #문자열의 첫번째 글자w가 출력 됨
print(hername[-1])    #문자열의 마지막 글자o가 출력 됨
hername1=hername[0]+ hername[-1]
print(hername1)    #wo 출력

#[파이썬에서 문자열은 모든것이 객체이다.(정수, 실수, 문자열)
#객체(object)란 프로그래밍에서 관련있는 변수와 함수를 하나로 묶은것

#[문자열을 소문자로 모두 바꿔주는 함수, 문자열 내의 특정 문자를 바꿔주는 함수]
hisname="Harry poter"
lower_hisname= hisname.lower()    #문자열 내의 모든 글자를 소문자로 바꿔준다.
print(lower_hisname)
newname=hisname.replace("poter", "orsbon")    #문자열 변수내의 포터를 오스본으로 변경 해준다.
print(newname)

#[로봇 야구 기자를 만들어 보자]
#경기장 이긴팀 진팀 스코어
baseball_place= input("오늘 경기는 어느 지역에서 진행이 되었나요?: ")
winteam= input("오늘 경기에서 이긴 팀은 어디 인가요?")
loseteam= input("오늘 경기에서 패배한 팀은 어디 인가요?")
gamescore= int(input("몇점 차이로 이긴건가요?"))
print(f"금일 {baseball_place}에서 {winteam}이 {loseteam}을 상대로 {gamescore}점 차이를 내면서 경기에서 승리 하였 습니다.")
#f를 앞에 넣어주면 문자열에서 바로 사용이 가능 하다.

