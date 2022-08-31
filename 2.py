N=int(input())
mylist=[]
mylist=list(map(int,input().split()))    #리스트에서 스페이스 간격으로 넣어줄때는 이렇게 넣어 보자

k=max(mylist)

for i in range(N):
    mylist[i]=(mylist[i]/k)*100

print(sum(mylist)/len(mylist))