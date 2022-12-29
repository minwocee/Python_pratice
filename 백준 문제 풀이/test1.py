# 산술평균
# 중앙값
# 최빈값 (여러개 존재시 가장 작은 값중 2번쨰를 출력 한다)
# 범위 출력한다

import sys

N= int(sys.stdin.readline()) # N 은 항상 홀수 이다.
Table=[int(sys.stdin.readline()) for _ in range(N)]     # 리스트 만드는 함수 출력

print('****************************************')
# 산술 평균을 출력 (소수점 아래 첫번째 자리에서 반올림을 실행 한다.)
a=round(sum(Table)/N); print(a)

# 중앙값을 출력 
Table.sort()
print(Table[int((N+1)/2)-1])


# 최빈값을 출력
T=list(set(Table))    # 순수하게 1개씩 어떤 값이 남아 있는지 알기 위해 출력 한다.
T.sort()
ans_list=[]

for a in T:
    ans_list.append(Table.count(a))     # T리스트의 순서대로 해당 요소의 최빈값들이 들어가게 된다.

king = max(ans_list)    # 최대값 저장 소

if ans_list.count(king)==1:
    print(T[ans_list.index(king)],'xxxxxx')    #최빈값이 하나 밖에 없으면 해당 요소 출력 한다.
else: #여러개 존재시 두번쨰걸로 출력을 하는 방법
    p = ans_list.index(king)     
    print(T[ans_list.index(king, p,len(T))],'zzzz') 



# 범위를 출력
if N==1:    #  요소가 하나 밖에 없을때
    print(0)
else:
    print(max(Table)-min(Table))



