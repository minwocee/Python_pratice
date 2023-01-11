import sys

N=int(sys.stdin.readline())

Table = list(map(int, sys.stdin.readline().split()))

sosu=[]
# 소수 구하는 공식 (소수가 1개라도 없으면 -1 출력)--> 모든수가 소수가 아니면 -1 출력

cnt=0
cnt2=0
for id in Table:
    cnt=0
    for _ in range(2,id):
        if id%_==0:    #나눠지면 소수가 아님
            cnt+=1
    
    if cnt==0:
        sosu.append(id)

    if cnt>=1:
        cnt2+=1

    

if cnt2 == len(Table):    #모든수가 소수가 아니면
    print(-1)
    exit(0)



from math import lcm
# 하나하나씩 비교를 해봐야 하나 리스트는 안됨 브루트 포스 식으로 해야할듯

first=sosu[0]



for _ in range(1,len(sosu)):   # 1 ~ 2
    first=lcm(first,sosu[_])

print(first)


    

