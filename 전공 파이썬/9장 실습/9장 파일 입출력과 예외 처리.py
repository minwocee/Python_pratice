#  <목차>
# 1. 파일 입출력
# 2. 예외처리


#    <파일 입출력 이란??
"""
파일을 사용하기 위해서는 파일을 열기, 읽기, 쓰기, 닫기 의 과정을 거쳐야 한다

* 파일 입출력을 위한 세 단계
1. open() 함수로 파일을 열어, 파일 객체를 생성함
2. 파일 객체를 이용해 입력 또는 출력을 수행 한다.
3. 파일 객체의 close 메소드로 파일을 닫는다.

* open()함수의 파일모드 6가지
- r : 읽기 모드 (기본값이며 생략이 가능)
- w : 쓰기 모드 (해당 파일이 존재 하지 않으면 새로운 파일을 생성하고, 해당 파일이 존재하면 기존 파일의 내용에 수정본을 덮어 씌운다)
- a : 추가(append) 모드
- x : 배타적(exclusive) 쓰기 모드(파일이 존재하면 오류가 발생, 없으면 새로운 파일을 생성함)
- t : 텍스트 모드 (기본값이며 생략 가능)
- b : 이진(binary) 모드  rb, rt, wb, wt 4가지 경우 존재

* with문 사용: 본문이 다 실행된 후에 자동으로 파일을 닫아줌(open()함수와 짝)
(예시1) with open('파일이름', '파일모드') as 변수명: 
                                                문장 블록

* 형식1: f = open('파일이름', '파일모드')
(예시1) f= open('list.txt', 'w')    -->   list.txt파일을 쓰기 모드로 열기
(예시2) f= open('list.txt', 'r')    -->   list.txt파일을 읽기 모드로 열기

"""

# # 예제 9-1 (파일 생성후 쓰기, 읽기 ,닫기 과정)
# file = open('test.txt', 'w')    # 쓰기 모드 시작(test.txt 파일이 없으므로 생성함, 이미 존재하면 덮어씌움)
# file.write("hello world!")    #text.txt 파일에 문자열을 입력해준다

# file = open('test.txt', 'r')    # 방금 만든 text.txt 파일을 읽는다
# read = file.read()    # 읽은 내용(문자열)을 read 라는 변수에 담는다

# print(read)    # read 변수의 내용물 출력
# file.close()



# # 예제 9-2 append모드 사용
# file = open('test.txt', 'a')    #기존 파일에 내용을 추가함
# file.write("파이썬이 너무 쉬워요~")

# file = open('test.txt', 'r')
# read = file.read()

# print(read)
# file.close()


# # 예제 9-3 오버라이딩(덮어씌우기) 확인 과정

# file = open('test.txt','w')
# file.write('hello my new world')

# file = open('test.txt', 'r')
# read = file.read()

# print(read)
# file.close()

# # 예제 9-4 배타적 x 사용 (기존 파일이 존재하면 오류알림, 없으면 새 파일을 생성함)
# with open("test.txt1", 'x') as file:    #이때 오류가 발생한다(test.txt가 이미 존재하는 파일이기 때문)
#     file.write("qwer")

# with open("test.txt1", 'r') as file:    #클로즈 메서드 사용 할필요 없음
#     print(file.read())

# # 예제 9-7
# with open('note.txt', 'w') as f:    # 3줄을 입력 하는 과정
#     f.write("123456789\n")
#     f.write("123456789\n")
#     f.write("123456789\n")
#     f.write(f"{1234}\n")    #f-string을 활용해 정수를 넣음
#     f.write(f"{5678}\n")    #f-string을 활용해 정수를 넣음
#     f.write(f"{9101112}\n")    #f-string을 활용해 정수를 넣음

# with open('note.txt', 'r') as f:
#     print(f.read())

# with open('note.txt', 'r') as f:
#     for msg in f:    #위와 같은 방식으로 출력하는 법 (한줄 한줄씩 출력함)
#         print(msg)




# #          교재에는 없는 CSV(comma-separated values) 파일 다루는법 (엑셀 파일)
# import csv
# listing = [['말리부','쉐보레', 22985] , 
# ['말리부1','쉐보레1', 22985] ,
# ['말리부2','쉐보레2', 22985] ,
# ['말리부3','쉐보레3', 22985] ,
# ['말리부4','쉐보레4', 22985] ,
# ['말리부5','쉐보레5', 22985] ]

# with open('cars.csv', 'w', newline='') as f:    #newline은 한줄씩 나오게 하기 위해서 사용
#     car_writer=csv.writer(f)
#     car_writer.writerows(listing)

# with open('cars.csv', 'r') as f:
#     car_reader = csv.reader(f)
#     for row in car_reader:
#         names = row[0]    #2차원 리스트의 첫번째 요소  [n][0]
#         makers = row[1]    #
#         print(names, makers)







# 2. 오류와 예외 처리
"""
<오류란? >
-프로그램이 정상적으로 동작하지 않는 현상을 의미


<예외란?>
-프로그래밍 언어의 규칙에 맞더라도 실행하는 도중에 잘못된 입력값이 들어오거나 비정상 적으로 종료하는 경우에 발생
-프로그램이 정상적으로 실행되지 않고 오류가 발생하는 것을 의미


<오류의 종류>
-문법 오류(syntax error): 파싱 에러 라고도 함, 문법을 틀렸을때 발생 혹은 오타발생시
(SystaxError: invalid syntax)

-런타임 오류(run-time error): 문법은 맞지만 실행하는 도중에 발생하는 오류
(1을 0으로 나누면?
Traceback: 역주행해서 오류가 난 부분을 찾음
ZeroDivisionError. division by zero)

-논리 오류(logical error): 문법은 맞지만 실행하는 도중에 발생하는 오류


<다양한 에러 메세지들>
SyntaxError: invalid syntax 구문 오류: 문법에 맞지 않는다

IndentationError: expected an indented block  들여쓰기 오류: 들여쓰기를 해야 한다

NameError: name 'true' is not defined  이름 오류: 이름 'true'가 정의되지 않았다


TypeError: unsupported operand type(s) for +: 'int' and 'str'
유형 오류: 연산자 +가 피연산자 유형 'int'와 'str'를 지원
하지 않는다

TypeError: can only concatenate str (not "int") to str
유형 오류: 문자열(str)은 단지 문자열하고만 연결할 수 있
다

TypeError: 'int' object is not callable 유형 오류: 'int' 유형 객체는 호출할 수 없다

TypeError: meth2() takes 1 positional arguments but 2 were given
유형 오류: meth2() 함수는 인자 1개를 전달받는데 2개가 전
달되었다

ValueError: invalid literal for int() with base 10: 'a' 값 오류: 'a'는 int() 함수의 10진법으로 해석할 수 없다

ZeroDivisionError: division by zero 영 나눗셈 오류: 영(0)으로 나눌 수 없다



<예외처리(Exeption Handling)>
-예외는 프로그램이 정상적으로 실행되지 않고 오류가 발생하는것을 의미하는데, 이런 예외에 대응하도록 하는것

형식1:
try:
    (예외가 발생할수 있는 코드 블록)
except:   
    (예외가 발생했을때 실행할 코드 블록)
else:
    (예외가 발생하지 않으면~ 실행하는 코드 블럭)
finally:
    (예외 발생 여부와 상관없이 무조건 실행할 코드 블록)

형식2
try:
    (예외가 발생할수 있는 코드 블록)
    raise 예외객체(예외내용)     # 사용자가 강제로 예외를 발생시킴(except: 에서 실행됨)
except:   
    (예외가 발생했을때 실행할 코드 블록)
else:
    (예외가 발생하지 않으면~ 실행하는 코드 블럭)
finally:
    (예외 발생 여부와 상관없이 무조건 실행할 코드 블록)
"""

# # 예제 9-7
# def divide(x,y):
#     try:    #이걸 실행한다
#         result=x/y
#     except ZeroDivisionError:    # 이 에러가 발생하면 실행함
#         print("0으로 나눌수 없습니다(제로 디비전 오류 발생)", ZeroDivisionError)
#     else:    #아무 에러 없이 실행
#         print("정상적으로 나눗셈이 실행 되었습니다 결과는 ",result)
#     finally:    #최종 실행
#         print("\n나눗셈 프로그램을 종료 합니다")

# import sys

# x= int(sys.stdin.readline())
# y= int(sys.stdin.readline())
# print()
# divide(x,y)
        

# 예제 9-8 의도적으로 오류를 발생(raise) 후 처리

x=int(input("짝수를 입력 하시오"))

try:
    if x%2!=0:
        raise Exception("짝수를 입력 하세요")
    if x==0:
        raise Exception("0을 입력했군요")

except Exception as e:    #as 사용해야 위의 문자열들이 정상적으로 출력된다
    print("예외가 발생했습니다", e)    #

else:
    print("잘하셨습니다. 입력한 수는 짝수 입니다.")

finally:
    print("\n프로그램을 종료 합니다")
















