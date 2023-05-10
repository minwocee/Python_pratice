# https://www.acmicpc.net/problem/5588

import sys
from collections import Counter

my=int(sys.stdin.readline())



# 내가 찾고자 하는 별자리
my_table=[]
for _ in range(my):
    my_table.append(list(map(int, sys.stdin.readline().split())))

ans=int(sys.stdin.readline())
ans_table=[]



# 실제 하늘의 별자리 리스트
for _ in range(ans):
    ans_table.append(list(map(int, sys.stdin.readline().split())))

#정상적으로 입력 완료

check=my_table[0]    #최초에 입력받은 테이블을 기준점으로 삼는다.(아무거나 잡고 이동헀을떄, 전체점들을 이동하는데 이동한 점들이 모두 실제 별자리에 있으면 답이다.)

cnt=0

answerx=[]
answery=[]
for ans in ans_table:    # 실제 하늘의 별자리 리스트
    x,y=ans[0]-check[0], ans[1]-check[1]    #x축, y축 이동 거리 측정완료

    
    for myt in my_table:    # 내가 원하는 별자리들 
        if [myt[0]+x, myt[1]+y] not in ans_table:    # 이동거리가 일치하는게 하나라도 어긋나면, 다른 탐색
            break
        else:    
            cnt+=1
            answerx.append(x)
            answery.append(y)


# Counter로 구한 최빈값을 max값으로 활용한다.
A=Counter(answerx)
topx=A[0]
for i in list(Counter(answerx)):
    if topx<A[i]:
        topx=A[i]
        qow=i



B=Counter(answery)
topy=B[0]
for i in list(Counter(answery)):
    if topy<B[i]:
        topy=B[i]
        qow2=i

print(qow, qow2)



'''
#counter 사용해서 출력하는법이 뭐였더라 최빈값을
cntx=[Counter(answerx)]
cnty=[Counter(answery)]

cntx_key=list(cntx.keys())

max_x=cntx(cntx_key[0])


for _ in cntx_key:
    if cntx[_]<max_x:
        max_x=cntx_key




cnty_key=list(cnty.keys())

max_y=cnty(cnty_key[0])


for _ in cnty_key:
    if cnty[_]<max_y:
        max_y=cnty_key

print(max_x, max_y)
   
'''