# # https://www.acmicpc.net/problem/10250

# import sys

# _ = int(sys.stdin.readline())
# # 한번 zip 함수를 사용해볼까유

# for __ in range(_):
#     k='%05d' % 2   #앞자리수는 0으로 채우되, 5칸을 할당 한다. 숫자는 2를 대입 00002 출력 완료
#     print(k)
#     Hotel_height, Hotel_max_room, now_client = map(int, sys.stdin.readline().split())
#     Table=[list(range(str)) for i in range(1,Hotel_height+1)]

# (1 ≤ H, W ≤ 99, 1 ≤ N ≤ H × W)
    
import sys

Tae=int(sys.stdin.readline())

for q in range(Tae):
    H, W, N=map(int,sys.stdin.readline().split()) 
    r=1    # 해당 층을 의미하는 변수
    mlist=[]
    for _ in range(W):
        k=100    # 객실 한칸씩 옆으로 늘어날때마다 100씩 증가 한다.
        for __ in range(H):
            mlist.append(k+r)
            k+=100
        r+=1

    print(mlist[N-1])


"""
핵심은 호텔을 90도 틀어서 생각하는 거였다 
1열 2열 3열을 아래에서 부터 채우는 방식이라 처음에 좀 해멨는데 우리가 생각하는 행과 열을 바꿔서 생각하면 편리하였다. 
# 단 층마다 100 200 300 이런식으로 올라가는 점을 기억 해야 한다.


"""




