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









