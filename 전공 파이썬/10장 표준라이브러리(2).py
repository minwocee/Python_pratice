# 예제 10-37 numpy에서의 array 생성과 출력
import numpy as np

a= np.array([0,1,2,3,4,5])

print(a[0])
print(a[4])


#예제 10-38    numpy array에서의 2차원 리스트 출력 과정 
import numpy as np

a=np.array([0,1,2],[3,4,5])
print(a)
print(a[0,0])    #첫번쨰 리스트의 첫번째  요소 출력 일반 파이썬에서 [0][0]
print(a[0,1])    #첫번쨰 리스트의 두번째  요소 출력('1'출력됨)
print(a[-1,-1])     #마지막 리스트의 마지막 요소 출력('5'출력됨)


#예제 10-39 행렬 방식으로 생각하기
import numpy as np

a=np.array([0,1,2,3],[4,5,6,7])
"""
[0,1,2,3]
[4,5,6,7]
"""
print(a)
print(a[0,:])     #':'기호는 전체를 의미, 첫번째 행 전체를 출력한다. ([0 1 2 3] 출력됨)
print(a[:,1])     #모든 행의 두번째 요소를 출력 ([1 5] 출력됨)
print(a[1,1:])    #두번째 행의 두번째 열부터 끝까지 출력([5 6 7] 출력됨)
print(a[:2,:2])   #모든행에서 [0:2]범위의 원소 출력([[0 1 2] [4 5 6]]출력됨, 대괄호가 3개 사용된다.)


# Boolean 값이 조건에 적용되는 배열 (True일 때만 출력이 되는 구조이다.)
import numpy as np

a= np.array([0,1,2,3,4,5,6,7,8,9])
idx=np.array([True,False,True,False,True,False,True,False,True,False,])

print(a[idx])   # [0 2 4 6 8] 이 출력으로 나온다(짝수일때만 실행이 된다.)


# Boolean 값이 조건에 적용이 되는지 알아옵는 예제
import numpy as np

a=np.array([0,1,2,3,4,5,6,7,8,9])

print(a%2)     #모든 배열의 요소마다 나머지 연산을 실행한다. (출력: [0,1,0,1,0,1,0,1,0,1])
print(a%2 ==0)     #[True,False,True,False,True,False,True,False,True,False,] 출력된다.
print(a[a%2==0])     #이러면 배열에서 짝수인 경우에만 출력이 된다. [0,2,4,6,8]



#예제 10-42  배열의 요소가 다른 배열의 인덱스 번호가되서 출력이 되는 경우 
import numpy as np

a= np.array([11,22,33,44,55,66,77,88,99])
idx=np.array([0,2,4,6,8])    #idx배열의 내용물이 인덱스 번호로 설정이 된다.
print(a[idx])      #[11 33 55 77 99]가 출력이 된다.


#예제 10-43
import numpy as np
a= np.array([11,22,33,44,55,66,77,88,99])
idx = np.array([0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2])
print(a[idx])     #[11 11 11 11 11 11 22 22 22 22 22 22 33 33 33 33 33] 출력된다.

# 예제 10-44 다차원 배열의 요소 출력하기

import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
print(a[:,[True,False,True,False]])    #모든 행으의 0번, 2번인덱스 요소만 출력함[[ 1  3] [ 5  7] [ 9 11]] 출력된다.
print(a[[2,0,1],:])    #3행 모든요소, 1행 모든요소, 2행 모든요소를 출력하는 예제이다.[[[ 9 10 11 12] [ 1  2  3  4] [ 5  6  7  8]]]  출력된다.


# 예제 10-45  np.zeros() 함수를 사용한 0으로 배열을 초기화 하는법
import numpy as np
a=np.zeros(5)
print(a)     #[0. 0. 0. 0. 0.] 

# 예제 10-46 np.zeros() 함수를 사용한 2차원의 배열을 초기화 하는법
import numpy as np
b=np.zeros((2,3))     #2행3열로 이루어진 2차원 배열을 형성함
print(b)     # [[0. 0. 0.] [0. 0. 0.]]

# 예제 10-47   배열에 들어가는 자료형의 타입을 설정해주는방식 (정수형 데이터 타입 설정)
import numpy as np
c=np.zeros((5,2), dtype="i")     # 5행 2열의 이차원 배열을 생성함(메모리에 들어가는 용량을 선택함)
print(c) 
"""
[[0 0]
 [0 0]
 [0 0]
 [0 0]
 [0 0]]
 이 출력된다.
"""
print(c.dtype)     # C의 데이터 타입을 출력함 int32가 출력됨 int는 4byte이고 이게 8번 반복된다.


# 예제 10-48    dtype을 유니코드로 설정함
import numpy as np
d= np.zeros(5, dtype="U4")     # 4개의 유니코드 문자가 자료형으로 지정됨
print(d)    # ['' '' '' '' ''] 가 출력됨 (5개의 문자열에 NULL값 들어가있음)


# 예서 10-49    dtype으로 배열의 메모리를 할당하고 , 요소를 초기화 하는 과정
import numpy as np
d = np.zeros(5,dtype="U4")
print(d)
d[0]="abc"
d[1]="abcd"
d[2]="ABCDE"     # 해당 배욜의 요소 설정
print(d)    #['abc' 'abcd' 'ABCD' '' ''] 출력된다.   d[2]에서 알파벳 E가 잘린다(U5라면 안잘림, 4개의 문자까지만 허용한다는 의미)


# 예시 10-50    모든 숫자를 one으로 초기화함
import numpy as np
e= np.ones((2,3,4), dtype="i8")    #3행 4열의 배열을 2층으로 쌓아서 만듬(층, 행, 열) , 64bit 인트값임


# 예시 10-51    모든
import numpy as np
b=np.zeros((2,3))    # 2행 3열의 0으로 초기화한 배열을 생성한다.
f=np.ones_like(b,dtype="f")    # 실수형의데이터 타입 선언
print(b)    # [[0. 0. 0.] [0. 0. 0.]]
print(f)    # [[1. 1. 1.] [1. 1. 1.]] 출력된다.


# 예시 10-52  모든 상황을 
import numpy as np
g=np.empty((4,3))    #그냥 공백만 할당됨(그냥 메모리 주소만 나옴)
print(g)

# 31:14
# 예시 10-53
import numpy as np
g=np.full((2,3), 10)    #2행 3열의 배열의 요소를 모두 10으로 채움
print(g)


# 예제 10-54 arange 생성기(range를 통한 배열 생성기)
import numpy as np
print(np.arange(10))
print(np.arange(2,19,2))    #초기값, 종료값(n-1까지만 값에 들어감), 증감폭
print(np.arange(19, 2, -2))
"""
[0 1 2 3 4 5 6 7 8 9]
[ 2  4  6  8 10 12 14 16 18]
[19 17 15 13 11  9  7  5  3]
"""


# 예제 10-55 
import numpy as np
print(np.linspace(10,20,5,endpoint = False))
print(np.linspace(1,2,5,retstep = True))
"""
[10. 12. 14. 16. 18.]
(array([1.  , 1.25, 1.5 , 1.75, 2.  ]), 0.25)
"""


# 예제 10-55
import numpy as np

print(np.linsapce(10,20,5, endpoint = False))
print(np.linsapce(1,2,5, retstep = True))


# 예제 10-56 
import numpy as np

print(np.logspace(1,10,10,base=2))

# 예제 10-57 
import numpy as np
print(np.eye(3))   #2차원 3*3 생성
print(np.eye(3, k=1))     #2차원 3*3 생성
print(np.eye(3), k=-1)    #2차원 3*3 생성, 대각선 아래로 1만큼 이동


# 예제 10-58
import numpy as np
print(np.arange(26))
print(np.arange(20).reshape(4,5))





#                      <BeautifulSoup> 웹 정보의 크롤링을 하는 라이브러리
# 10-59 형식
from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("https://cc.sungkyul.ac.kr/")    #웹페이지 불러오기

soup=BeautifulSoup(target,'html.parser')
title=soup.findAll('p',{"class":"subject"})

for i in range(15):
    print(title[i].text)

# bs.py
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')

print('*'*100)
print(bs.html)
print('*'*100)
print(bs.h1)
print('*'*100)
print(bs.body)
"""                                  <출력결과>
<html>
<head>
<title>A Useful Page</title>
</head>
<body>
<h1>An Interesting Title</h1>
<div>
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
</div>
</body>
</html>
****************************************************************************************************
<h1>An Interesting Title</h1>
****************************************************************************************************
<body>
<h1>An Interesting Title</h1>
<div>
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
</div>
</body>
"""


#                                       <Matplot 라이브러리>

# y=10*x 의 일차함수 그래프 그리기(구글코랩 활용)
import matplotlib.pyplot as plt      # 그래프 표션시 
import numpy as np     # 통계학 계산

x=np.arange(1,10)
y=10*x
plt.plot(x,y)
plt.show()


# y=10*x의 직선 그래프를 붉은색으로 설정된다.
import numpy as np
import matplotlib.pyplot as plt

plt.plot(x,y,'r')     #그래프 색상을 붉은색으로 설정함.
plt.xlabel('X Line', fontsize='18')     #해당 선에대한 라벨을 출력.
plt.ylabel('Y Line')
plt.show()


# 시간과 행복도를 나타내는 그래프
import numpy as np
import matplotlib.pyplot as plt

hours=[9,10,11,12,13,14,15,16,17,18,19,20]
happiness=[9.8,9.9,9.2,8.6,8.3,9.0,8.7,9.1,7.0,6.4,6.9,7.5]
plt.plot(hours,happiness)
plt.xlabel('hours', fontsize='18')     #해당 선에대한 라벨을 출력.
plt.ylabel('happiniess',fontsize='18')
plt.show()



# 두개의 직선이 교차하는 그래프
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,5,0.5)     #0.5 간격으로 증감폭을 잡는다.
y=x*10
y2=50-(x*10)

plt.plot(x,y,'r',label='red')    #나중에 라벨을 수정해보자
plt.plot(x,y2,'k',label='black')     #나중에 라벨을 수정해보자
plt.legend(loc='upper right')
plt.show()


# 여러개의 그래프를 생성하고 비교가 가능한 구조(소비자별 돈의 씀씀이 분석)
import numpy as np
import matplotlib.pyplot as plt

days=[0,1,2,3,4,5,6]
money_spent1=[10,12,12,10,14,22,24]

money_spent2=[11,14,15,15,22,21,12]
money_spent3=[11,15,18,15,23,29,18]

plt.plot(days, money_spent1, label='ME')
plt.plot(days, money_spent2, label='K')
plt.plot(days, money_spent3, label='R')

plt.xlabel('DAYS', fontsize='18')     #해당 선에대한 라벨을 출력.
plt.ylabel('SPEND MONEY',fontsize='18')

plt.legend(loc='upper left')
plt.show()

# 














