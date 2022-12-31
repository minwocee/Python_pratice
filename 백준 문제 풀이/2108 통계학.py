# # 산술평균
# # 중앙값
# # 최빈값 (여러개 존재시 가장 작은 값중 2번쨰를 출력 한다)
# # 범위 출력한다

# import sys

# N= int(sys.stdin.readline()) # N 은 항상 홀수 이다.
# Table=[int(sys.stdin.readline()) for _ in range(N)]     # 리스트 만드는 함수 출력

# print('****************************************')
# # ***********************산술 평균을 출력 (소수점 아래 첫번째 자리에서 반올림을 실행 한다.)
# a=round(sum(Table)/N); print(a)

# # *****************************중앙값을 출력 
# Table.sort()
# print(Table[int((N+1)/2)-1])


# # ***********************최빈값을 출력

# """
# 1. 최빈값 수치가이 무엇인지 찾고
# 2. 최빈값으로 설정된 정수를 찾는다 (2개이상시 )
# """

# # 최빈값 찾기
# lis=list(set(Table))   # 사용한 요소 1개 1개들을 의미
# print(lis, 'qqqqqqqqqqqqqqqqqqqqqq')
# lis.sort()
# ans=[]

# for k in lis:
#     ans.append(Table.count(k))    # 각요소들의 등장 횟수 기록

# king = max(ans)

# if ans.count(king)==1:    #최빈값이 하나만 나오는 경우
#     for k in lis:
#         if Table.count(k)==king:
#             print(k)     # 1개있을떄 출력

# elif ans.count(king)>=2:
#     at=0
#     for k in lis:
#         if Table.count(k)==king:
#             at+=1
#             if at==2:
#                 print(k)    # 2개 있을떄 출력 완료

# # ************************범위를 출력
# if N==1:    #  요소가 하나 밖에 없을때
#     print(0)
# else:
#     print(max(Table)-min(Table))


""" 최빈값을 해결하지 못하였다 (다른분의 코드 참고)"""
'''
최빈값을 구하는 부분이 제일 까다로운 문제이다.

이 부분은 파이썬의 Counter를 이용하자.

 

Counter는 리스트의 각 숫자들의 등장횟수를 카운트하여 몇 회 등장했는지 딕셔너리로 표현한다.

그리고 Counter의 most_common(n)은 빈도수가 가장 많은 것 부터 n개의 수를 (숫자, 등장횟수)의 형태로 반환한다.

n을 생략한다면 리스트의 모든 수를 반환한다.

 

최빈값이 두 개 이상일 경우에는 두 번째로 작은 값을 출력하라고 했으므로

다음과 같이 알고리즘을 짰다.

tmp[0][1] == tmp[1][1] 이라면 최빈값 리스트의 첫 번째 수와 두 번째 수의 등장횟수가 같다는 것이므로

최빈값이 두 개 이상이 된다.

그래서 두 번째 값을 출력하면 된다.

 

그 외에는 tmp[0][0]을 출력하면 된다.
'''


import sys
from collections import Counter     # Conter와 Counter.most_common()을 활용하기 위해 포함

N = int(sys.stdin.readline())

numList = []
for i in range(N):
    numList.append(int(sys.stdin.readline()))

# 산술평균
print(round(sum(numList) / N))

# 중앙값
numList.sort()
print(numList[N//2])

# 최빈값 구하는 과정 
cnt = Counter(numList)    # Counter는 numlist 안에 담겨있는 요소들이 몇번 등장했는지 딕셔너리의 형태로 각각 세서 담아준다.
# Counter({-2: 1, 1: 1, 2: 1, 3: 1, 8: 1}) 이런식으로 딕셔너리 형태로 담겨져 있다. (정렬을 해놔서 순서대로 들어간다.)

tmp = cnt.most_common()    # 가장 많은 개수의수(최빈값)을 tmp에 (숫자, 등장횟수) 형태로 넣어주는 역할(등장횟수가 가장 큰순서대로 들어간다)

# most_common(n)은 빈도수가 가장 많은 것 부터 n개의 수를 (숫자, 등장횟수)의 튜플  형태로 반환한다. n을 생략한다면 리스트의 모든 수를 반환한다.
# Counter의 안에 내장된 함수인 most_common(n) 이다. (세트로 사용)

if len(tmp) > 1:    # N=2 이상인 경우
    if tmp[0][1] == tmp[1][1]:    #첫번쨰요소의 등장횟수와 두번쨰 요소의 등장 횟수가 같으면 두번째 숫자를 출력해야 한다
        print(tmp[1][0])    # (숫자, 등장횟수) 구조의 튜플임을 유의, [0](두번째) 숫자 출력
    else:
        print(tmp[0][0])    # 최빈값 가장 높은게 하나밖에 없는 경우 [0](첫번째) 숫자 출력
else:
    print(tmp[0][0])    # 입력한 숫자가 한개 N=1 인 경우 출력

# 범위 
print(max(numList) - min(numList))
