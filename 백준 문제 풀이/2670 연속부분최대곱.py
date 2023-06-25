# 2차원 DP로 풀다가 메모리 초과 발생...
'''
import sys

N = int(sys.stdin.readline())

arr = [float(sys.stdin.readline()) for _ in range(N)]

# 2차원 DP 설정
DP = [[0]*N for _ in range(N)] 

# 대각선 부분을 초기화 하자
for i in range(N):
    DP[i][i] = arr[i]
    
# 이제 한줄씩 2차원 DP를 채워주자(MAX(이전값, 현재의 계산[i:j]값))

def check_sum(i,j):
    king = 1
    for _ in range(i,j+1):
        king*=arr[_]
    return king

for I in range(0, N):    #행
    for J in range(1+I,N):    #열
        DP[I][J] = max(DP[I][J-1], check_sum(I,J))

king = 0
for I in range(N):
    king = max(king, max(DP[I]))

print("%0.3f" % king)
'''

# 1차원 DP로 풀어보자
import sys

N= int(sys.stdin.readline())
arr = [float(sys.stdin.readline()) for _ in range(N)]

for i in range(1,N):
    arr[i] = max(arr[i], arr[i]*arr[i-1])
    
print("%0.3f" % max(arr))