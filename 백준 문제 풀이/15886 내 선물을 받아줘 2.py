# https://www.acmicpc.net/problem/15886

# 가장 많이 이동하는 칸을 출력하는 문제 인것같다.



import sys

N= int(sys.stdin.readline())
Action = list(sys.stdin.readline().strip())

cnt = 0
for i in range(N-1):
    if Action[i] == 'E' and Action[i+1] == 'W':
        cnt+=1

print(cnt)
# EW 쌍의 개수만 체크 해보자
        


