# https://www.acmicpc.net/problem/2302

# 고정석은 움직이지 않되 얼마나 더 바꿀수 있는지 계산을 하는 프로그램을 만들어라
# 단 움직일수있는 범위는 자신의 왼쪽 오른쪽 1칸 뿐이니 123이 321 로 바꿀수 없다는것을 알자
# 경우의수를 파악해서 점화식을 만들어 보자

"""
1칸 1
2칸 2
3칸 3
4칸 5
.
.
.
피보나치 수열인들함 한번 재귀함수를 만들어서 풀어봐야 하나? 아님 리스트를 생성하는 식으로 풀어보자
"""



''' 실패
def fib(n):
    
    if n == 0:    #종료조건1
        return 0
    elif n==1 or n==2:    #종료조건2
        return 1
    else:
        return fib(n - 1) + fib(n - 2)    #이전항 2개를 더한다는 조건이 핵심이다.

import sys

N = int(sys.stdin.readline())
fixed = int(sys.stdin.readline())
fixed_Table = []    #고정석 좌석
for _ in range(fixed):
    fixed_Table.append(int(sys.stdin.readline()))


if fixed==0:
    print(N)
    exit(0)
# 뭉태기는 fixed+1개 존재한다고 생각한다.

뭉태기list=[]

뭉태기list.append(fixed_Table[0]-1)# 첫 fix요소 - 1
뭉태기list.append(N-fixed_Table[-1])# 마지막 좌석번호 - 끝 fix요소

for i in range(len(fixed_Table)-1):    # 2칸짜리 고정석이면 0 이렇게 들어감
    # print(fixed_Table[i+1])
    # print(fixed_Table[i])
    # print('**********')
    뭉태기list.append(fixed_Table[i+1]- fixed_Table[i]-1)

#print("뭉태기 리스트", 뭉태기list)

King=1

for _ in range(len(뭉태기list)):
    King*=fib(뭉태기list[_]+1)

print(King)

'''

import sys

n = int(sys.stdin.readline())    #좌석의 개수 입력 (1부터 시작)
m = int(sys.stdin.readline())    #고정석의 개수 입력
vip = [int(sys.stdin.readline()) for _ in range(m)]    #고정석의 좌석번호가 입력됨(1부터)


#좌석이 1개만 있는경우 출력해준다

if n==1:
    print(1)
    exit(0)



dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1 # 1
dp[2] = 2 # 1 2, 2 1
# 1 2 3 5 8 .... 인덱스번호랑 좌석번호랑 같다고 취급하면 편함

# 점화식 : dp[n] = dp[n - 1] + dp[n - 2]
for i in range(3, n + 1):    # 피보나치 수열 초기화 해줌
    dp[i] = dp[i - 1] + dp[i - 2]


answer = 1 # 경우의 수
# vip의 유무에 따라 경우의 수를 도출

if m > 0:  #고정석의 개수가 0보다 크면 실행  
    pre = 0
    
    # 반복문을 통해 vip 사이에 그룹에 들어가는 경우의 수를 확인
    for j in range(m):   #고정석 2개면 0 1 2 이렇게 들어간다.
        now = vip[j] - 1 - pre # vip좌석번호 - 시작번호 -1 에 해당하는 피보나치 수열을 사용
        answer *= dp[now]    
        pre = vip[j]    #vip의 좌석 번호가 된다.

    answer *= dp[n - pre]    #마지막 뭉텅이까지 잊지말고 넣어준다.

else:     #고정석의 개수가 0개이면 실행
    answer = dp[n]
print(answer)