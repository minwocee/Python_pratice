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