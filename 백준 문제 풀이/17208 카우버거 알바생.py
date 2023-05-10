# https://www.acmicpc.net/problem/17208
# N(1 ≤ N ≤ 100), x, y (1 ≤ x, y ≤ 300)
# 조합으로 풀면 몇의 시간 복잡도? 2^100-1임 조합은 불가능함
import sys
''' 
# 주문수, 치즈버거, 감튀 순 입력 받는다.
Order, Cheeze, Photato =map(int ,sys.stdin.readline().split())

# [[2, 5], [1, 2], [3, 3], [2, 1]]
Order_list =[]

# 가능한 주문들만 모아 둔다.
for _ in range(Order):
    a,b = map(int,sys.stdin.readline().split())
    if a>Cheeze or b>Photato:
        continue
    Order_list.append([a,b])

if len(Order_list) ==0:
    print(0)
    exit()
   
# [[1, 2], [3, 3], [2, 1]]
# print(Order_list)

A = sorted(Order_list, key= lambda x:x[0])
B = sorted(Order_list, key= lambda x:x[1])

# X좌표 정렬
#print(A)

# B좌표 정렬
#print(B)

cntA=0
cntB=0

check =0
for i in A:
    if check<Cheeze:
        check+=i[0]
        cntA+=1
    
    if check>Cheeze:
        check-=i[0]
        cntA-=1
        break

check =0
for i in B:
    if check<Photato:
        check+=i[1]
        cntB+=1
    
    if check>Photato:
        check-=i[1]
        cntB-=1
        break
print(min(cntA, cntB))
'''

# 모든 경우의 수를 비트화 한다. bin(42), int('0b101010', 2)를 이용하면 2진수 변환을 쉽게 가능하다
# bit_num = len(Order_list) # 사용해야 하는 비트의 개수를 의미 한다.

# Dp = [0] * (2**bit_num)

# # 101 이면? bit2는 문자열로 들어오는 2진수 이다.
# def 계산(bit2):
#     bit = bit2.split('b')[1]
    
    
#     return (good, cnt)

# dp를 사용한 피보나치 수열의 구현


import sys; ssr = sys.stdin.readline 

N, M, K = map(int, ssr().split())
arr = [list(map(int, ssr().split())) for _ in range(N)]
graph = [[[0 for _ in range(K + 1)] for _ in range(M + 1)] for _ in range(N + 1)]

# 왜 -1이냐고? 인덱스 번호는 0부터 체크 하기 때문임
# 주문번호, 치그버거 현재누적주문 빠져 나간양, 감튀 현재 누적주문 빠져 나간양
stack = [[-1, 0, 0]]
while stack:
    
    # 스택에서 뺀다.
    n, m, k = stack.pop()
    
    # 주문 
    if n >= N - 1: continue
    
    tn = n + 1
    tm = m + arr[tn][0]
    tk = k + arr[tn][1]
    
    if tm <= M and tk <= K and graph[tn][tm][tk] < graph[n][m][k] + 1:
        graph[tn][tm][tk] = graph[n][m][k] + 1
        stack.append([tn, tm, tk])
    tn = n + 1
    tm = m
    tk = k
    
    if tm <= M and tk <= K and graph[tn][tm][tk] <= graph[n][m][k]:
        graph[tn][tm][tk] = graph[n][m][k]
        stack.append([tn, tm, tk])
    
ans = 0
for i in range(N + 1):
    for j in range(M + 1):
        for k in range(K + 1):
            ans = max(ans, graph[i][j][k])
print(ans)