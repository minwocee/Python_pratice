# 모든 경우의 수를 해결하는 브루트 포스 알고리즘을 배워보는 문제

# N(3<= N <=100): 모든 카드의 개수
# M(10<= M <= 300,000)


""" 방법1 무지성 for문 돌리기 (내 수준에서 해결, 시간복잡도 엄청 올라감 비효율의끝판왕)"""
#굳이 summ을 활용해서 다 더할필요 없다. arr[] + arr[] + arrp[] > Score 이런식으로 비교를 해보자 

import sys

def find_max(Table):
     max_score=0    #3장을 뽑아서 나온 수의 합이 점수 M이상이면 안됨 가까우면 좋은것
     for a in range(N):
        
         for b in range(a+1,N):
            
             for c in range(b+1,N):   
            
                if Table[a]+Table[b]+Table[c]<=M:     # 만약 요소 3개의 합이 M보다 작으면거나 같으면 조건 발동
                    max_score=max(max_score, Table[a]+Table[b]+Table[c])      #최대값을 찾는다!

     return max_score


N, M =map(int,sys.stdin.readline().split())
Table=list(map(int,sys.stdin.readline().strip().split()))     #테이블을 정수형태로 입력받음

print(find_max(Table))

"""방법2 combination(순열)라이브 러리를 활용하는 방법"""
import sys
from itertools import combinations      #itertools 라이브러리에서 combination(조합, 순서가 없음) 기능만 가져온다. 

def find_max(Table):
    big_num=0     #현재 랭킹 1위를 저장할때 쓰는 변수
    for i in combinations(Table,3):    #Table 배열에서 3개를 뽑아둔 순열(순서가 없음)을 각각 튜플 형태로 반환해서 넣어준다!.
        summ=sum(i)     #이번 도전자라고 생각
        if big_num<summ<=M:    #3개가 동시에 비교가 가능한게 정말 신기하네요 (파이썬은 이게 된다 and 안쓰고도 가능)
            big_num=summ     #랭킹 1위 최신화
    return big_num    #랭킹 1위 반환


N, M =map(int,sys.stdin.readline().split())
Table=list(map(int,sys.stdin.readline().strip().split()))     #테이블을 정수형태로 입력받음

print(find_max(Table))



"""추가적인 팁 (파이썬에서 모든 경우의 수를 for문을 사용하지 않고 바로 만들어주는 함수 사용법)"""
from itertools import permutations     #순열을 의미한다 (순서가 존재한다)
from itertools import combinations

Table=['A','B','C']
print(list(map(''.join, permutations(Table))))    #원소가 3개 사용하는 모든 경우의수 리스트
print(list(map(''.join, permutations(Table,2))))   #원소가 2개 사용하는 모든 경우의수 리스트
print(list(map(''.join, permutations(Table,1))))   #원소가 1개 사용하는 모든 경우의수 리스트

print(list(map(''.join, combinations(Table))))    #원소가 3개 사용하는 모든 경우의수 리스트
print(list(map(''.join, combinations(Table,2))))   #원소가 2개 사용하는 모든 경우의수 리스트
print(list(map(''.join, combinations(Table,1))))   #원소가 1개 사용하는 모든 경우의수 리스트




























