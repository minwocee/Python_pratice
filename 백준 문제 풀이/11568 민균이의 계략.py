# https://www.acmicpc.net/problem/11568


# 간단히 말해서 앞에서부터 나올수 있는 오름 차순의 순서대로 판별을 하면 된다.


# 시간복잡도 1초 10^8

# N은 1000까지 따라서 N^2=10^6까지 허용이 가능 그럼 무난하게 브루트포스로 갈까

# 투포인터로도 구현이 가능할듯

# 모르겠네
'''
의사코드
ans_real=0
for i in range(N):    #원소의 탐색 범위를 제한하는 기능
    cnt=Field[i]
    for k in range(i,N):
        if cnt<Field[k]:
            ans+=1
            cnt=Field[k]
            
    ans_real=max(ans,ans_real)
        

'''


'''
import sys

N=int(sys.stdin.readline())
Field=list(map(int,sys.stdin.readline().split()))

ans_real=1
for i in range(N):    #원소의 탐색 범위를 제한하는 기능
    ans=1
    cnt=Field[i]
    for k in range(i,N):
        if cnt<Field[k]:
            ans+=1
            cnt=Field[k]
            
    ans_real=max(ans,ans_real)
    
print(ans_real)
'''

# 그럼 투포인터 기법을 쓰자
'''

ans=1
의사코드

While end!=N-1 

시작, 끝 인덱스 설정 해줌 (둘다 0으로 초기)

끝값을 1 올리고 오름차순인지 비교 (만약 오름차순이 아니면, start+1)

매 연산 결과 마다 ans=max(end-start+1, ans) 해주고 답 출력 하지


'''

# Dp를 쓰는 문제

# Longenst increasing Sequence 문제 줄여서 LIS 문제 (DP 에서 자주 나오는 문제중 하나)

import sys

N=int(sys.stdin.readline())    # 자료의 개수

card = list(map(int, input().split()))    # 카드가 담긴 테이블   0-index

ans=[]    # 연승 스트릭을 담을 리스트 이다.

for start in range(N):   # 시작점 잡는 기준
    king = card[start]    # 기준점 잡는곳
    cnt=1
    
    for end in range(start,N):
        if king<card[end]:
            cnt+=1
            king=card[end]
    ans.append(cnt)        
    
print(max(ans))
    