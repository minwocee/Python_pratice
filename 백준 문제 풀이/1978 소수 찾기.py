# https://www.acmicpc.net/problem/1978

# 주어진 수중에서 소수가 몇개인지 찾는 문제
# 소수: 1과 자기 자신만을 약수로 가지는 문제
# 정수 1은 소수로 치지 않는다.
# 시간복잡도는 N^2이 된다.
def sosu_counter(n):    # 일일이 전부 나눠보는 문제
    if n==1:
        return 0
    cnt=0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1
            if cnt==3:
                return 0
    return 1



import sys

N = int(sys.stdin.readline())
Table=list(map(int, sys.stdin.readline().split()))

cnt=0
for king in Table:
    if sosu_counter(king) == 1:
        cnt+=1
print(cnt)













