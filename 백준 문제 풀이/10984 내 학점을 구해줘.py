# https://www.acmicpc.net/problem/10984
def avg(flo):

    return (sum(flo)/len(flo))

import sys


T=int(sys.stdin.readline())

for _ in range(T):

    N=int(sys.stdin.readline())

    #학점 입력받기 시작
    비중=[]
    학점=[]
    for __ in range(N):
        x,y=map(str,sys.stdin.readline().strip().split())

        비중.append(int(x))
        학점.append(float(y))


    sum2=0
    for q,p in zip(비중, 학점):
        sum2+=q*p

    print(sum(비중) ,round(sum2/sum(비중),1))

