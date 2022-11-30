"""
<목차>
1. 수학(math) 라이브러리
2. 인터넷 엑세스(URL lib) 
3. 시간과 날짜(time, datetime)
4. Numpy   #통계자료 사용시
5. BeautifulSoup  #데이터 분석용
6. Matplotlib  #그래프같은 식 시각적표현
"""

#math 라이브러리

# 예제 10-1
print(abs(-3))   #-3의 절대값 3을 반환
print(max(1,2,5))    #요소중 가장 큰 값을 반환함
print(min(-1,-3,-9))    #요소중 가장 작은 값을 반환
print(pow(2,10))    #a^b를 반환함 2의 10승-->1024
print(round(2.5))    #정수자리까지 반올림을함


# 예제 10-2
import math

print(math.pi)
print(math.e)
print(math.tau)

# 예제 10-3
import math
print(math.fabs(-2.123))     #실수의 절대값을 반환함
print(math.ceil(2.1))    #가장 가까운 정수값을 올림반환함  2.000001 이면 3 반환(조금이라도 실수 존재시 올림)
print(math.ceil(-2.1))     #가장 가까운 정수값을 올림반환함
print(math.floor(2.9))    #가장 가까운 정수값을 버림반환함    2.99999이면 2반환(조금이라도 실수 존재시 버림)
print(math.floor(-2.1))    #가장 가까운 정수값을 버림반환함

# 예제 10-7
#입력받은 값이 m * 2**e와 같은 값을 가지는 형태의 m과 e를 반환함
print(math.frexp(100))    #부동소수점을 분리하는 기능 (0.78125(m), 7(e))
print(math.modf(10.71))     #(소수부분, 정수부분)으로 나눠서 반환함 (0.7100000000000009, 10.0)

#예제 10-8
print(math.ldexp(0.78125,7))  #입력받은 (m,e)를 m * 2**e 공식을 적용해서 알려줌 frexp를 역순으로 접근
print(math.gcd(12,18))    # 입력받은 두 수의 최대 공약수를 구해짐



#인터넷 엑세스(URL 라이브러리) 웹 문서들을 확인시 주로 사용

#HTTP 상태코드 받아오는법
import urllib.request
address = urllib.request
check = address.urlopen("https://www.naver.com/")
print(check.status)    #200 OK는 정상적으로 잘 받아왔다는 뜻이다.


#객체 받아오기
address = urllib.request
print(address.urlopen("https://www.naver.com/"))    


#웹 페이지정보 읽어오기    #html 문서 소스코드를 가져온다.
address = urllib.request
check = address.urlopen("https://www.naver.com/")
print(check.read())    

#HTML 소스코드를 인간이 보기 쉽게 깔끔하게 보여준다.
url = "https://www.naver.com/"
site = urllib.request.urlopen(url).read().decode('utf-8')
print(site)

#웹문서를 파싱할때 쓰는 코드
parse = urllib.parse.urlparse("https://www.naver.com/", scheme='http') #스키마를 통해 형식을 지정함
print(parse)




# <시간과 날짜(time, datetime)라이브러리 사용>
import time

t=time.time()
print(t)    #1669547798.3676822 라고 반환됨(유닉스형식의 시간표기법)
#timestamp 컨버터를 통해서 변환해야 한다() 결과: 2022년 11월 27일 일요일 오후 8:16:38.367 GMT+09:00


#GMT 시간을 이용해 그리니티 시간 출력
t=time.time()     #유닉스의 시간표기법으로 담김
time_utc = time.gmtime(t)   #GMT 시간 변환
print(time_utc)    
#time.struct_time(tm_year=2022, tm_mon=11, tm_mday=27,
#tm_hour=11, tm_min=21, tm_sec=33, tm_wday=6, tm_yday=331, tm_isdst=0) 으로 변환된다.

#현지 지역 시간으로 변환하는법

t=time.time()
time_local=time.localtime(t)
print(time_local) # time.struct_time(tm_year=2022, tm_mon=11, tm_mday=27, tm_hour=20, tm_min=24, tm_sec=1, tm_wday=6, tm_yday=331, tm_isdst=0)
#한국 시간에 맞게 변횐됨


#Y-M-D 형식에 맞게 변환해 출력하는법
print(time.strftime("%Y-%m-%d",time.localtime(time.time())))   #2022-11-27 출력됨
print(time.strftime("%c",time.localtime(time.time())))    #Sun Nov 27 20:27:32 2022  출력됨
print(time.strftime("%X",time.localtime(time.time())))    #20:29:11 출력됨




#여기서부터는 datetime 라이브러리를 사용
import datetime
print(datetime.datetime.today())    #2022-11-27 20:34:33.302933  출력됨(연월시분초)


# 예제 10-23
import datetime 
d=datetime.datetime(2022, 11,27)
print("-"*20)
print(d.strftime("%Y-%m-%d"))    #2022-11-26
print(d.strftime('%c'))    #Sat Nov 26 00:00:00 2022  보여줌

# 예제 10-25

import time
t = time.time()
time.sleep(3)    #10초뒤 코드가 다시 실행됨

t2 = time.time()
spendtime = t2-t    #측정시간을 계산한다.
spendtime = int(spendtime)

print("첫번째 측정 시간: ", t)
print("두번째 측정 시간: ", t2)
print("기다린시간 {}초".format(spendtime))

#디데이 계산
import datetime
today = datetime.datetime.today()
Dday = datetime.datetime(2022,12,3,8,10,00)    #2022년 12월 3일 08시 10분
how=Dday-today    #현재로부터 해당시간까지 남은 시간을 계산
print(how)



# #구분해서 연도~초까지 출력하는 방법(현재 오류가 발생함)
# tm=time.time()
# print(tm.tm_year)
# print(tm.tm_mon)
# print(tm.tm_mday)
# print(tm.tm_hour)
# print(tm.tm_min)
# print(tm.tm_sec)






#                                      <통계를 위한 Numpy 라이브러리>

# numpy.array()함수 사용
import numpy as np    #numpy 라이브러리 설치해야함

ar = np.array([0,1,2,3,4,5,6,7,8,9])    #적은메모리로 데이터를 빠르게 처리 가능
print(ar)
print(type(ar))    # <class 'numpy.ndarray'> 출력됨(배열 형식으로 만듬)

# numpy의 효율성을 알아보자
data = [0,1,2,3,4,5,6,7,8,9]
answer=[]
for di in data:
    answer.append(2*di)
    print(answer)

import numpy as np

data = [0,1,2,3,4,5,6,7,8,9]
x = np.array(data)
print(x)
print(x * 2) # 배열 통째로 연산을 진행하는 효율적인 방식이 가능하다.(리스트처럼 반복형을 쓸 이유가 없다.)


# Boolean도 배열 동시 적용이 가능함
a = np.array([1,2,3])
b = np.array([10,20,30])

print(2*a+b)
print(a==2)    # [False True False] 형식으로 반환된다.
print(b>10)
print((a==2)&(b>10))      # [False True False] 형식으로 반횐된다. (a배열과 b배열을 동시에 비교해줌)

# 행열 프로그램도 제작이 가능 34:21









