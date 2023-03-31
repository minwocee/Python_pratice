# https://www.acmicpc.net/problem/11568

# LIS (가장 긴 연속 수열을 찾는 문제, DP의 대표적인 활용법)

# 2가지 방법이 존재, 1번: N^2 시간복잡도, 2번: NlogN 시간 복잡도


# 1번부터 시연 시작
'''
8 9 1 2 10 을 예시로 들자

자료의 개수: 5개

간단히 말해 k번째 필드 값이 어느 위치에 존재 하는지 알면 됨

ex) 4번 인덱스인 2는, 필드값 0 보다 크고, 8보다 작기에, dp[4]=dp[0]+1이다.

ex) 5번 인덱스인 10은, 필드값 9보다 크기에 dp[5]=dp[2]+1 이다.


Index  0  1  2  3  4   5
------------------------
Field  0  8  9  1  2  10      #맨 앞에는 0이 있다고 생각
----------------------------
DP     0  1  2  1  2  3

'''
# 어떻게 이런 생각을 사람들은 할수 있는 거지?

# 1번 방법을 구현 한다.
import sys

N=int(sys.stdin.readline())
Field=[0]
Field1=list(map(int,sys.stdin.readline().split()))
Field.extend(Field1)

dp=[0]*(N+1)

for O in range(1,N+1):    # 바깥값을 고정치
    
    king=Field[O]    # 앞에서 부터 선택한 O 번째 요소값!
    
    # 이제 해당 요소값이 앞에서 부터 탐색했을 떄 어디에서 막히는지만 알면 됨
    
    for I in range(1,N):
        if Field[I]<= king < Field[I+1]:
            dp[I]=dp[I]+1
            break
        elif max(Field)==Field[I]:    #해당 값이 최대값이면
            dp[I]=max(dp)+1
            break
        
print(dp)

#https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4#s-3.1