import sys

N, M=map(int, sys.stdin.readline().split())#강의개수, 바구니 개수

Table=list(map(int,sys.stdin.readline().split()))

# 이떄 12345, 67, 89 이렇게 나뉜다. 3개를 나눔
# 참고로 1부터 9까지의 합은 

mlist=[0]*M

King=sum(Table)/M    #평균 구하기

ind=0
for _ in Table:
    mlist[ind]+=_
    if mlist[ind]>=King:
        ind+=1

print(mlist)









