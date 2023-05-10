# https://www.acmicpc.net/problem/5575


#모든 시간을 초로 환산한다.
def time_count(L):   #출근, 퇴근의 시각이 나온다.
    start=0
    end=0

    start+=L[0]*216000
    start+=L[1]*3600
    start+=L[2]*60

    end+=L[3]*216000
    end+=L[4]*3600
    end+=L[5]*60

    ans=end-start

    r1=ans//216000
    r2=(ans%216000)//3600
    r3=(ans-r1*216000-r2*3600)//60

    return r1,r2,r3



import sys


A=list(map(int, sys.stdin.readline().split()))
B=list(map(int, sys.stdin.readline().split()))
C=list(map(int, sys.stdin.readline().split()))

sa=time_count(A)
sb=time_count(B)
sc=time_count(C)

print(sa[0],sa[1],sa[2])
print(sb[0],sb[1],sb[2])
print(sc[0],sc[1],sc[2])





