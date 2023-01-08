import sys

N=int(sys.stdin.readline())
mlist=[]

for _ in range(N):
    a,b,c=map(int,sys.stdin.readline().split())
    mlist.append([c,a,b])    #점수 참가국 학생번호 순으로 들어간다.

mlist.sort()

#이제 순위 계산을 출력 한다.
cnt=0
contry_conter=[0]*N   #나라의 수만큼 해당 배열을 초기화한다.
for i in range(N-1,-1,-1):    #8 7 6 5 4 3 2 1 순으로 들어간다. 
    if cnt >2:
        break
        
    contry_conter[mlist[i][1]-1]+=1
    
    if contry_conter[mlist[i][1]-1]>=3:
        continue
    cnt+=1
    
    print(mlist[i][1],mlist[i][2])
    

