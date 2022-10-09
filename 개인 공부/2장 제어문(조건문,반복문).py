#조건문과 반복문을 학습 해보자.  2022.08.20 작성

'''
[if-else 문 사용법]
<형식>
if 조건식 :
    문장1 (참일시 실행됨)
else :
    문장2 (거짓일시 실행됨, else는 생략이 가능하다)
'''
#예시
a=100
if a>10:
    print("a는 10보다 큰수입니다.")
else:
    print("a는 10보다 작다고 생각 합니다.")

#[2만원 이상 구매시 배송비를 무료로 해주는 프로그램을 만들어 보자]
price=int(input("구매한 품목의 가격을 입력해주세요: "))

if price>20000:
    print(f"배송비 무료이므로 총 결제 금액은 {price}입니다.")
else:
    print(f"배송비 2500원 추가됩니다. 총 결제 금액은 {price+2500}입니다.")
    print(f"{20000-price}만큼만 더 금액을 충족하시면 배송비가 무료입니다.")
#충족해야할 조건이 여러개일때는 들여쓰기를 통해 블록을 만들어 준다.

'''
<관계 연산자(결과는 boolean값으로 표기)>
!=,==, +=, -=,<=,>= 등 존재한다. 기존의 C언어 문법과 동일 
'''
#예시(제곱근에 루트를 씌워서 같은지 확인하는 프로그램)
from math import sqrt   #수학 라이브 러리 에서 루트(sqrt)를 사용하는 함수를 불러와 준다.
n=sqrt(3.0)

if (n*n)==3.0:
    print("sqrt(3.0)**2은 3.0과 같다.")
else:
    print("거짓 입니다.")

#[활용: 초등학생들을 위한 산술 계산 프로그램을 생성 해보자]\
import random

x=random.randint(1,100)     #1~99까지의 숫자중 랜덤으로 변수에 넣어 준다.
y=random.randint(1,100)

print(f"{x} + {y} = ?")
a=int(input())

if (x+y)==a:
    print("정답 입니다. 축하드립니다.!")
else:
    print("땡 입니다. 아쉽네요!")

#[조건 연산자(흔히 삼항 연산자라고도 C언어 에서는 불림)]
#<예시>
a=12;b=10
x= a if(a<b) else b    #조건식이 참이면 x에 a를 대입, 거짓이면 x에 b 를 대입
print(x)
#형식: (참일시 실행) if(조건문) else (거짓일시 실행)  조건문의 참 거짓에 따라 대입되는 변수가 달라진다.


#<예시2> 절대값을 반환하는 프로그램을 만들어 보자
k1=-56
k2= k1 if k1>0 else k1*(-1)     #음수일떄 -1을 곱해서 절대값을 나타내준다.
print(k2)

#[활용: 사용자로 부터 정수를 입력받고 짝수or 홀수인지 구분하는 프로그램을 만들어 보자]

numb= int(input("정수를 입력하면 짝수or홀수를 구분해 드립니다: "))

if (numb%2)==0:
    print("짝수 입니다.")
else:
    print("홀수 입니다.")

#[활용2: 100만원 이상 구매시 15퍼 할인과 사은품을 주는 프로그램을 만들자(100만원 아래면 10퍼 할인)]\
Price=int(input("오늘 구매하신 물건의 가격을 입력해 주세요: "))

if Price>100:
    print(f"금일 구매한 금액의 15% 할인을 해드립니다~ 총 결제금액:{Price*0.85} ")
    print("추가로 고객센터에서 사은품도 챙겨서 가세요~")
else:
    print(f"10퍼센트 할인 해드립니다 총결제 금액은 {Price*0.9}입니다.")

'''
<논리연산자 and, or, not>
x and y  (x와 y가 모두 참이여야 실행)
x or y   (x와 y중 둘중에 하나만 참이여도 실행)
not x    (x가 거짓이면 참, 참이면 거짓)
'''
#예시: 구매금액 20000원 이상, 성결 카드면 배송비가 무료인 상품 
price2=25000
cardname="sungkyul"
if (price2>=20000 and cardname=="sungkyul"):     #2가지 조건을 모두 만족해야 실행되는 조건문and
    print("학생은 배송비가 무료입니다!")

#[활용: 현재 물의 상태를 출력해주는 프로그램을 만들어 보자 (고체,액체,기체)]

temp=float(input("현재 물의 온도는 몇도 인가요?: "))
if temp<=0:
    print("고체 입니다.")
if temp>0 and temp<99:    #논리연산자 and 사용
    print("액체입니다.")
if temp>=99:
    print("기체상태 입니다.")

#[활용3: 동전 던지기 게임을 만들어 보자]
coin=random.randrange(2)    #0이상 2미만인 정수를 생성한다.

if coin == 0:
    print("짝수 입니다.")
else:
    print("홀수 입니다.")

#if-elif문 활용(연속 if문) 학점을 주는 프로그램을 만들어 보자
stuscore=int(input("학생의 점수를 입력 해주세요: "))

if stuscore>=90:
    print("A학점 입니다.")
elif stuscore>=80:
    print("B학점 입니다.")
elif stuscore>=70:
    print("C학점 입니다.")
elif stuscore>=60:
    print("D학점 입니다.")
else :
    print("자네는 F야")


#[기본적인 반복문을 배워보자(for, while 등)]
'''
<그전에 파이썬에서의 리스트(list)의 이해>
리스트란 항목들을 저장하는 자료 구조
ex) slist=["국어","영어","수학"]  인덱스 [0] ,[1],[2] 에 각자 국어 영어 수학 문자열이 들어간다.
'''


mlist=[]    #공백의 리스트를 생성한다
mlist.append(1)    #append()함수를 사용해서 리스트에 정수 1을 추가한다
mlist.append(2)    #append()함수를 사용해서 리스트에 정수 1을 추가한다
mlist.append(3)    #append()함수를 사용해서 리스트에 정수 1을 추가한다
mlist.append(4)    #append()함수를 사용해서 리스트에 정수 1을 추가한다
print(mlist)    #리스트의 내용물들을 출력한다.

#이때 인덱스의 번호는 0~3까지이며 마지막 인덱스는 -1로도 입력이 가능하다.

#[리스트를 사용한 for 반복문]
for i in mlist:
    print(f"안녕하세요 저는 {i}번째 반복 입니다.")     #리스트의 항목이 4개 있으므로 4번이 반복되는 구조 이다.\

for i in [1,2,3,4,5,6]:
    print(f"저는 {i}번째 반복 입니다. 반갑 습니다.")    #6개의 항목이 있는 리스트 이므로 6번 반복된다.


#[range() 함수를 사용한 for 반복문]
#range(5)--> 0,1,2,3,4 의 정수가 순차적으로 생성하는 함수 이다.  보통은 반복문에서 range함수를 사용한다.
for k in range(5):
    print(f"{k}번째 반복되는 문장 입니다. 감사 합니다.")
'''
<range() 함수의 추가적인 이해>
형식: range(시작값, 멈추는값(포함X), 증가량)

<예시>
range(5)        0,1,2,3,4 생성
range(1,5)      1,2,3,4 생성
range(1,10,2)   1,3,5,7,9 생성됨 (중가량이 2씩 들어남)  
'''
#추가적인 활용
#end를 통해 띄어쓰기 하나씩 넣어준다. 모든수를 가로롤 출력해줌
for i in range(1,6,1):     #1,2,3,4,5
    print(i, end=" ")    

print("\n")
 #10부터 역순으로 줄어드는 구조 10~1까지
for i in range(10,0,-1):   
    print(i, end=" ")

#1부터 n까지의 합 출력
n=100
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

#구구단 출력 프로그램
gugu=int(input("출력을 원하시는 구구단을 입력하세요: "))
for i in range(1,10):
    print(f"{gugu} * {i} = {gugu*i}")

#for 문을 사용해 팩토리얼계산 프로그램을 만들어 보자
pt=int(input("팩토리얼 계산을 원하는 수를 입력 해주세요: "))

summ=1
for i in range(1,pt+1):    #pt+1을 붙여주는걸 기억하자(마지막 숫자는 포함이 안된다.)
    summ*=i
print(summ)

summ1=1
for i in range(10,0,-1):    #역순으로 팩토리얼을 계산하는 프로그램을 생성한다.
    summ1*=i
print(summ1)


'''
[while문 사용법]
while (조건문):
    (원하는 반복설정)

의미: 특정 조건을 만족 시킬때 까지 실행을 한다.
'''
#예시: 몸무게가 100kg 넘을때 몸무게를 늘려보자
weigh=30
while 100>weigh:
    weigh+=1
    print(f"현재의 몸무게 {weigh}")

#예시2 1부터 10까지의 합을 계산하는 while 반복문(뭔가 시험에도 나올것 같음)
i=1    #1,2,3,4,5,6...더해주는 숫자들
sum=0    #총합을 저장하는 숫자들
while i<=10:
    sum+=i
    i+=1    #덧셈의 증가량을 1,2,3,4,5,6... 씩 증가 시켜주는 역할을 한다.
print(sum)

#[else를 사용한 루프 탈출식]
o=1

while o<10:
    print("루프를 탈출 중 입니다.")    #9번 반복됨
    o+=1    #1씩 증가시켜 준다.
else:
    print("루프를 탈출 하였습니다.")    #10번째에 출력

#[활용: while 을 활용한 구구단(9단)을 출력 해보자]
dan=9
i=1
while i<10:
    print("%d * %d = %d"%(dan,i,dan*i))
    i+=1

#[활용2 랜덤한 수를 만들고 그수를 맞추는 퀴즈를 내는 프로그램을 제작]
ansnum=random.randint(1,100)    #1부터 100까지의 정수중 임의의 수를 만든다.
plat=0
try1=1
'''
while plat!=ansnum:
    plat=int(input("1~99 까지의 정수중 하나를 입력하세요: "))
    if plat<ansnum:
        print("좀더 큰수를 적어주세요...")
    if plat>ansnum:
        print("좀더 작은수를 적어주세요...")
    if plat==ansnum:
        print("정답 입니다 축하드립니다!!!!")
        print(f"시도한 횟수 {try1}")
    try1+=1
'''
#[활용3 초등학생을 위한 산술 계산 프로그램(단 틀리면 학습을 중단 한다.)]

answer=-1
playerinput=-1
count=-1
while answer==playerinput:
    x=random.randint(1,100)
    y=random.randint(1,100)
    answer=x+y
    print(f"{x} + {y} = ?")
    playerinput=int(input("알맞은 정답을 입력 하시오: "))
    count+=1
print("연속 정답 횟수: %d"%count)


#[활용4 비밀번호가 맞을때 까지 반복을 하는 프로그램 제작]
truepasswd= "helloworld"
inputpasswd=" "

while truepasswd!=inputpasswd:
    inputpasswd=input("알맞은 비밀번호를 입력하시오: ")
print("정답입니다. 로그인 성공")


#[활용5 for를 중첩으로 사용해 크리스마스 트리를 만들어 보자]
k=10
for i in range(1,9):
    print("_"*k,end="")
    print("x"*(2*i-1),end="")
    print("_"*k)
    k-=1
    
