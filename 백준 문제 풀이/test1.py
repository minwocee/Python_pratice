# 산술평균
# 중앙값
# 최빈값 (여러개 존재시 가장 작은 값중 2번쨰를 출력 한다)
# 범위 출력한다

import sys

N= int(sys.stdin.readline()) # N 은 항상 홀수 이다.
Table=[int(sys.stdin.readline()) for _ in range(N)]     # 리스트 만드는 함수 출력

print('****************************************')
# ***********************산술 평균을 출력 (소수점 아래 첫번째 자리에서 반올림을 실행 한다.)
a=round(sum(Table)/N); print(a)

# *****************************중앙값을 출력 
Table.sort()
print(Table[int((N+1)/2)-1])


# ***********************최빈값을 출력

"""
1. 최빈값 수치가이 무엇인지 찾고
2. 최빈값으로 설정된 정수를 찾는다 (2개이상시 )
"""

# 최빈값 찾기
lis=list(set(Table))   # 사용한 요소 1개 1개들을 의미
lis.sort()
ans=[]

for k in lis:
    ans.append(Table.count(k))    # 각요소들의 등장 횟수 기록

king = max(ans)

if ans.count(king)==1:    #최빈값이 하나만 나오는 경우
    for k in lis:
        if Table.count(k)==king:
            print(k)     # 1개있을떄 출력

elif ans.count(king)>=2:
    at=0
    for k in lis:
        if Table.count(k)==king:
            at+=1
            if at==2:
                print(k)    # 2개 있을떄 출력 완료

# ************************범위를 출력
if N==1:    #  요소가 하나 밖에 없을때
    print(0)
else:
    print(max(Table)-min(Table))



