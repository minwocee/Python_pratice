#https://www.acmicpc.net/problem/14921

# 단순하지만 재미있는 문제 이다.
'''
2 ≤ N ≤ 100,000    자료의 개수 제한
-100,000,000 ≤ Ai ≤ 100,000,000    용액의 정수 범위
Ai-1 ≤ Ai    반드시 오름차순으로 자료가 들어온다는 의미 이다.
'''
# 우선 시간제한이 1초이다. 이말은, 
'''
import sys

N=int(sys.stdin.readline())    # 자료의 개수를 입렫 받음

Field=list(map(int, sys.stdin.readline().split()))
'''

'''
# 기본적인 투 포인터 예제 문제를 작성해보자
interval_sum=0
cnt=0
end=0
Field=[1,2,3,2,5]
N=5   #데이터의 개수
target=5    # 찾고자하는 구간수열을 5로 둔다.

for start in range(N):    # start 값은 for문을 활용해서 자동으로 올라가게 한다.
    
    while end<N and interval_sum<target:    #end가 자료의 개수를 초과하는걸 막고, 구간의 합이 target을 벗어나기 전까지 실행한다.
        interval_sum+=Field[end]    # 초기 end값은 0, 각 구간을 
        end+=1    # 구간합이 타겟보다 적으므로, 더 자료가 필요함 end +1 해주기
    if interval_sum==target:
        cnt+=1
    interval_sum-=Field[start]    # 구간합을 만족하거나, 구간합이 타겟보다 커진경우 start인덱스 실제 값을 빼준다.(이제 볼 필요가 없기 때문)

print(cnt, '해당 구간의 개수')

'''

# 다른분의 블로그 참고: https://baby-ohgu.tistory.com/21

import sys
N=int(sys.stdin.readline())
Data = list(map(int, sys.stdin.readline().split()))

L, R = 0, N-1    # 양 끝단 값을 L,R에 설정한다.

ans=Data[L] + Data[R]    # 양 끝값의 절대값의 합 (절대값이 0에 가까울수록 좋은것임)

while L<R:
    sub=Data[L]+Data[R]
    #print(sub, 'sub의 값 출력') 
    #print(L,R,'좌우의 값 확인')
    #print("****************")
    if abs(ans)>abs(sub):    # 절대값을 비교했을 때 0에 더 가까운수 가 있다면 ans 업데이트
        ans = sub    # 0에 가까운값을 업데이트 한다
    
    if sub<0:    # 음수값이 나온다면, 음수값을 한칸 줄여야 한다.
        L+=1
    else:    # 양수값이 나온다면, 양수값을 한칸 적게 옮긴다.
        R-=1

print(ans)