# 일반적으로 생각하면 시간 초과가 뜬다 이를 방지 하기 위해 딕셔너리를 사용 함










































import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))

_dict = {}  
for i in range(N):
    _dict[cards[i]] = 0  # 딕셔너리를 활용해서 출력

for j in range(M):
    if checks[j] not in _dict:
        print(0, end=' ')
    else:
        print(1, end=' ')