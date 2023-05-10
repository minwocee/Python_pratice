#https://www.acmicpc.net/problem/16938

'''
문제
알고리즘 캠프를 열려면 많은 준비가 필요하다. 그 중 가장 중요한 것은 문제이다. 오늘은 백준이를 도와 알고리즘 캠프에 사용할 문제를 고르려고 한다.

백준이는 문제를 N개 가지고 있고, 모든 문제의 난이도를 정수로 수치화했다. i번째 문제의 난이도는 Ai이다.

캠프에 사용할 문제는 두 문제 이상이어야 한다. 문제가 너무 어려우면 학생들이 멘붕에 빠지고, 문제가 너무 쉬우면 학생들이 실망에 빠지게 된다. 따라서, 문제 난이도의 합은 L보다 크거나 같고, R보다 작거나 같아야 한다. 또, 다양한 문제를 경험해보기 위해 가장 어려운 문제와 가장 쉬운 문제의 난이도 차이는 X보다 크거나 같아야 한다.

캠프에 사용할 문제를 고르는 방법의 수를 구해보자.
'''

# 2문제 이상은 꼭 골라야 한다.
# 첫째 줄에 N, L, R, X가 주어진다.  (문제개수, 문제난이도합(최소치), 문제난이도합(최대치), 탑-바텀>=X)

#둘째 줄에는 문제의 난이도 A1, A2, ..., AN이 주어진다.

# 이때 가능한 조합의 수를 알아보자


'''
제한
1 ≤ N ≤ 15
1 ≤ L ≤ R ≤ 10^9    
1 ≤ X ≤ 10^6    어려운문제 - 쉬운문제
1 ≤ Ai ≤ 10^6   난이도 정수 범위
'''
import sys

# 문제를 고르는 경우의 수는 2~N개 까지 가능 함
# 그렇다면 바로 순열로 풀면 될듯

from itertools import combinations
N,L,R,X=map(int,sys.stdin.readline().split())# 문제수, 최저난이도합, 최고 난이도합, 탑-바텀>=X
Field = list(map(int,sys.stdin.readline().split()))    # 필드를 입력 받는다.
             
             
# 튜플 형태로 조합을 반환한다. 그럼 비교만 하면 끝이다 이말이야

cnt=0 
# 몇개를 뽑는지 정하는 반복문
for i in range(2,N+1):
    F=list(combinations(Field, i))  # 튜플 형태로 조합을 반환한다. 그럼 비교만 하면 끝이다 이말이야
    
    for comb in F:    #튜플의 내용물을 하나씩 꺼내준다.
        if (L<=sum(comb)<=R) and (max(comb)-min(comb)>=X):
            cnt+=1

print(cnt)