N,M=map(int,input().split())


garolist={}

for _ in range(N):
    x,y,p,q=map(int,input().split())   #4줄 입력받음

    for i in range(x,p+1):
        for k in range(y,q+1):
            garolist.update((i,k))

        
    
print(garolist.items)




# garolist.sort()
# serrolist.sort()

# counter=0
# sum=100
# for i in range(len(garolist)-1):    #자신과 다음 숫자를 비교하는 반복문
#     if garolist[i]==garolist[i+1]:
#         counter+=1
        

#     elif garolist[i]!=garolist[i+1]:
#         if counter>M:
#             sum-=1
#         counter=0

# ocounter=0
# osum=100
# for i in range(len(serrolist)-1):    #자신과 다음 숫자를 비교하는 반복문
#     if serrolist[i]==serrolist[i+1]:
#         ocounter+=1
        

#     elif serrolist[i]!=serrolist[i+1]:
#         if ocounter>M:
#             osum-=1
#         ocounter=0

# print(osum*sum)
