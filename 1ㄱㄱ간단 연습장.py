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