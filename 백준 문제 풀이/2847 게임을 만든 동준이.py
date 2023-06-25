import sys

N = int(sys.stdin.readline())

arr = [int(sys.stdin.readline()) for _ in range(N)]

cnt = 0
# 역순으로 접근한다.
for i in range(N-1, 0, -1):
    now = arr[i]
    next = arr[i-1]
    
    # 만약 오름차순을 만족하지 않으면 강제로 낮춘다.
    if next - (now-1) > 0:
        cnt +=next - (now-1)
        arr[i-1] = arr[i]-1
    
print(cnt)
    
