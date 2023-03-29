# https://www.acmicpc.net/problem/17269


import sys

N,M = map(int, sys.stdin.readline().split())
N_,M_=sys.stdin.readline().strip().split()


mlist=[3	,2	,1,	2	,4,	3,	1	,3,	1,	1,	3,	1,	3	,2,	1	,2,	2,	2,	1,	2,	1,	1,	1,	2,	2	,1]

myd={}

cnt=65


for i in mlist:
    myd[chr(cnt)]=i
    cnt+=1
    
# 매핑 완료 이제 탐색 시작함

Field=[]
A=max(N,M)

cnt_1=0
cnt_2=0

for i in range(A):
    if cnt_1<N:
        Field.append(N_[i])
        cnt_1+=1
        
    if cnt_2<M:
        Field.append(M_[i])
        cnt_2+=1
        

#Field 설정 완료


ans=[]

for i in Field:
    ans.append(myd[i])
    
#print(ans)


while(len(ans)!=2):
    x=[]
    for i in range(len(ans)-1):
        x.append((ans[i]+ans[i+1])%10)
    ans=x


if ans[0]==0:
    print(str(ans[1])+'%')
else:
    print(str(ans[0])+str(ans[1])+'%')   
