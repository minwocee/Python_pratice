# 11주차 실습 22.11.12
"""
목차
1. 표준 모듈 사용
2. 외부 모듈
3. 모듈 만들기ㅇㅇ
"""

# 1. 표준 묘듈
"""
모듈(module): 파이썬 코드를 논리적으로 묶어서 관리하고 사용할수 있도록 하는 파이썬 코드 집합이라고 생각
*추가 기능을 지원해주는 플러그 인이라고 생각)

파이썬 표준 라이브러리(Python Standard Library, PSL): 파이썬에 기본적으로 설치된 모듈, 패키지, 내장함수를 묶어서 지칭

표준 모듈: PSL안의 모듈, 파이썬에서 제공하는 모듈

사용자 정의 모듈: 직접 만들어서 사용하는 모듈

써드파티(3rd party): 외부회사나 단체에서 제공하는 모듈
"""

# 표쥰 모듈 사용
"""
형식1: import 모듈1(,모듈2,모듈3...)    *괄호는 생략이 가능함-동시에 여러개 import 해주기 위해서
-import된 모듈내의 함수는 호출시 (모듈이름.함수이름) 으로 사용한다
(예시: import math 이후에 A=math.factorial(5)식으로 사용 된다.)

형식2: from 모듈이름 import 함수이름   *모듈에서 1개의 함수만 사용하는 경우
-이떄 선언한 함수는 "함수이름만 사용함"
(예시: from math import comb;   b=comb(5,2)  *b=math.comb(5,2)꼴로 사용시  NAMEERROR 발생)

형식3: from 모듈이름 import *
-모듈의 모든 변수, 함수, 클래스를 직접 사용하기 위해서 사용
-import 모듈이름과 다른점은 "모듈이름.함수이름" 형태가 아닌 "함수이름"만 사용해도 된다는 장점이 있다.

형식4: from 모듈이름 import 함수1,함수2,함수3...
-하나의 모듈안의 여러 함수를 사용할때 작성함

형식5: import 모듈이름 as 별칭 혹은 from 모듈이름 import 함수이름 as 별칭
-numpy를 np라고 하는것처럼 모듈을 별칭으로 바꿔서 부를수 있음(alias)

형식6: from 모듈이름 import 변수 as 이름1 , 함수 as 이름2 , 클래스 as 이름3
-모듈내에서 각 변수, 함수, 클래스 등을 콤마로 구분하여 별칭을 지정하여 사용함
* import로 가져온 모듈(변수, 함수, 클래스)를 해제할때는 del을 사용하고, 해제된 모듈을 다시 가져오려면 importlib.reload()를 사용한다.
"""

#예제 8-1     (math 모듈 내의 사용가능한 함수들을 출력한다.)
import math
print(dir(math))


#예제 8-2      (팩토리얼 함수를 직접 만들고 출력하는 과정)
def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

print("5!: ", factorial(5))


#예제 8-3
import math
a=math.factorial(5)
print("5!: ",a)


#예제 8-4
from math import comb
b=comb(6,2)    #6C2 실행한 결과   (math.comb(6,2)사용시 오류)
print("6 combination 2=",b)


#예제 8-6    (원주율을 출력하는 단계)
from math import *   
print(pi)


#예제 8-7   (별칭 사용법)
from math import pow as p ,sqrt as s    #제곱과 루트 사용
a=p(2,3)    #math.pow 라고 사용하지 않아도 된다
b=s(4)
print("2의 3승:",a)
print("4에 루트를 씌운 결과:",b)


#예제 8-11    (del 사용해 모듈 해제)
del math
#print(dir(math))    #오류발생함(del로 모듈 해제 하였기때문)



#                    <외부 모듈>
"""
외부 모듈: 외부에서 불러오는 파이썬 파일

random 모듈: 임의의 수를 새엇ㅇ하거나 리스트 내의 요소를 무작위로 선택하거나 섞는 함수를 포함
-choice(list): 주어진 리스트의 아이템을 무작위로 선택
-randint(1, 1000): 1부터 1000 까지의 의 수중에서 임의의 난수를 반환
-random(): 0~1.0 사이의 임의의 난수를 반환한다.
-randrange(n,m): n이상 m미만의 임의의 난수(정수)를 반환한다.
-shuffle(list): 주어진 리스트의 내용을 섞는다
-sample(): 지정된 개수의 요소를 입의로 선택한다
"""

# 8-13 랜덤모듈 사용
import random
print(random.random())    #0~1.0사이의 임의의 실수를 반환
print(random.randint(1,6))    #1,2,3,4,5,6 중에 하나가 반환됨
print(random.randrange(1,6))  #1,2,3,4,5 중에 하나가 반환됨
num_list=[10,20,30,40,50]
random.shuffle(num_list)    #리스트를 무작위로 섞는다
print(num_list)    #리스트가 섞여서 출력된다
print(random.choice(num_list), "무작위로 선택된 리스트 요소 1개")
print(random.sample(num_list,3), "무작위로 선택된 리스트 요소 3개")




#                          <sys 모듈>
"""
System specific parameters and functions 모듈
파이썬 인터프리터가 제공하는 시스템과 관련된 정보를 제공
-copyright: 현재 설치된 파이썬의 저작권을 반환한다.
-exc_info: 현재 발생중인 예외 정보를 반환한다.(예외가 없으면 none을 반환, 익셉션 인포)
-exit: 현재 프로세스를 강제로 종료한다.
-getdefaultencoding(): 현재 사용중인 문자열 코딩 방법을 반환(utf-8, ASCII등)
-getrefcount(): 객체를 참조하는 카운트(개수)를 반환한다.

-getwindoswversion(): 현재 윈도우 버전을 반환
-modules: 현재  import한 모듈 이름을 반환한다.
-path: 모듈의 설치 경로를 반환한다.
-prefix: 파이썬이 설치된 경로를 반환한다.
-version: 현재 파이썬 버전을 반환한다.(인터프리터 버전+ 빌드넘버 사용된 컴파일러에 대한 문자열)
-version_info: 현재 파이썬 버전을 반환한다.(major, minor, micro, release level, serial에 대한 tuple)
"""

#예제 8-14     (모듈,파이썬의 설치된 경로를 반환)
import sys
print(sys.path)   #모듈의 설치 경로
print("-"*10)
print(sys.prefix)    #파이썬의 설치 경로
print("-"*10)
print(sys.version_info)    #현재 파이썬 버전을 반환
print("-"*10)
print(sys.copyright)    #현재 설치된 파이썬의 저작관 반환
print("-"*10)
print(sys.getwindowsversion())    #현재 설치된 윈도위 버전 반환





#                      <OS(운영체제 관련)모듈>
"""
OS(Miscellaneous Operating system interface)는 운영체제와 관련된 기능을 가진 모듈

-chdir(디렉토리 이름): 디렉토리 위치를 변경한다.
-environ: 시스템의 환경 변숫값을 보여준다
-getcwd(): 현재 디렉토리 위치를 반환한다
-listdir(): 현재 디렉토리의 파일과 디렉토리 리스트를 반환한다.
-mkdir(디렉토리 이름): 새로운 디렉토리를 만든다

-name: 파이썬이 실행되는 운영체제의 이름을 반환한다.(nt, posix, mac 등)
-popen(시스템 명령어): 시스템 명령어를 수행하고 그 결과를 반환한다.
-rename(파일이름, 새로운 파일이름): 파일을 새로운 이름으로 변경한다.
-system(시스템 명령어): 시스템의 명령어를 수행한다.
-unlink(파일이름): 파일을 삭제한다.
"""

# 예제 8-16
import os
print(os.getcwd())    #현재 디렉토리 위치 반환
print('-'*20)
print(os.listdir())    #현재 디렉토리의 파일과 디렉토리 리스트를 반환한다.
print('-'*20)
print(os.name)    #현재 파이썬이 실행되는 운영체제의 이름을 반환
print('-'*20)




#                     <calendar 모듈>
"""
calendar 모듈은 달력 기능을 제공

-calendar(연도): 주어진 연도의 달력을 출력한다
-monthrange(연도, 월): 주어진 연도, 월이 어느 요일에 시작해서 며칠까지 있는지를 튜플 형태로 반환한다.
-prmonth(연도, 월): 주어진 연도의 월에 대한 달력을 출력한다.
-weekday(연도, 월, 일): 주어진 날짜가 어떤 요일인지를 반환(월요일: 0 ~ 일요일 6 을 반환함)

"""

#예제 8-17
import calendar
print(calendar.monthrange(2022,11))    #주어진 년도의 월이 몇일부터 몇일까지 존재하는지 반환 (1,30)이 나옴
print("-"*20)
print(calendar.weekday(2022, 11 ,12))    #5를 반환(토요일)
print("-"*20)
print(calendar.prmonth(2022,8))   #해당 년도의 월의 캘린더 모양으로 출력
print("-"*20)
print(calendar.calendar(2022))    #2022년도 달력 전체를 출력함




#                 <pickel 모듈>
"""
pickel은 데이터의 자료형을 유지하면서 파일로 저장하고 로드할수 있도록 도와주는 모듈

dump(데이터, 파일 변수): 데이터를 파일로 저장한다.
load(파일 변수): 저장된 내용을 다시 로드한다.
"""

# #예제 8-18     (실행시 현재 디렉토리에 문서파일이 하나 생김)
# text="파이썬 프로그래밍!"
# with open("python.txt", "W") as p:
#     p.write(text)

#예제 8-19
list=['a','b','c']
with open('list.txt', 'w') as f:
    f.write(list)    #문자열형이 아니기에 텍스트 파일로 만들떄 오류가 발생한다

#예제 8-20
import pickle

list=['a','b','c']
with open('list.txt', 'wb') as f:
    pickle.dump(list,f)




#              <tempfile 모듈>
"""
tempfile 은 임시로 사용할 파일을 생성시키는 모듈

-mktemp(): 중복되지 않는 임시 파일의 이름을 생성한다.
-NamedTemporaryFile(): 임시 파일을 생성하고 close()가 호출되면 파일 객체를 자동으로 삭제한다.
"""

# # 예제 8-22
# import tempfile

# filename = tempfile.mktemp()    #임시파일 문자열이생성됨(돌릴떄 마다 바뀜)
# print(filename)



#                         <모듈 만들기>
"""
코드 작성시 공통되는 부분을 모듈로 작성하여 사용
코드 재사용이 가능
"""
#예제 8-23
#다른 파일에다 만들어야 하는 내용(이름: mymod.py)
PI=3.141592

class Circle:
    def com1(self,r):    #원의 넓이 구하는 클래스
        return PI*(r**2)

def com2(a,b):
    return 2*a*b


import mymod    #내가 직접 만든 모듈

print(PI)
a=mymod.Circle()
print("반지름이 5일때 원의 넓이 =", a.com1(5))   #원의 넓이를 반환