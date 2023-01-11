import sys

N=int(sys.stdin.readline())
mlist=[]

for _ in range(N):
    a,b,c=map(int,sys.stdin.readline().split())
    mlist.append([c,a,b])    #(점수, 참가국, 학생번호) 순으로 들어간다.

mlist.sort()

#이제 순위 계산을 출력 한다.
cnt=0
contry_conter=[0]*N   #나라의 수만큼 해당 배열을 초기화한다.(나라의 수가 2개이상이면 정지를 하기위해서 만든 체크섬)
for i in range(N-1,-1,-1):    #8 7 6 5 4 3 2 1 순으로 들어간다.
    if cnt >2:    # 1등 2등 3등 발표가 끝나면 종료
        break
        
    contry_conter[mlist[i][1]-1]+=1    #
    
    if contry_conter[mlist[i][1]-1]>=3:    #해당 나라가 2번 시상을 하면 넘긴다.
        continue
    cnt+=1
    
    print(mlist[i][1],mlist[i][2])    # 나라, 선수번호 출력 
    

