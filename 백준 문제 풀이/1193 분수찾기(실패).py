#우리가 구해야 몇번째줄 몇번째칸에 있는지를 구하는게 핵심이다






















def counter(int_N):
    가중치=1
    track=0
    while(int_N>가중치):

        int_N-=가중치
        가중치+=1
        track+=1   #1,2,3... 가중치가 늘어남(이게 몇번째 줄에 있는지 알려줌, 분모)
    return track+1,int_N    #줄위치, 줄위치에서의 세부 위치 (리턴값이 2개이다)

import sys

N=int(sys.stdin.readline().strip())

print(f"{counter(N)[1]}/{counter(N)[0]+1-counter(N)[1]}")    #각각의 분모와 분자에 알맞은 수를 넣는다


