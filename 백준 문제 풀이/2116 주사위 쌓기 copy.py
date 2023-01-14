import sys

N= int(sys.stdin.readline())

Table = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

print(Table)

# 매핑 정보
mapping ={0:5, 1:3, 2:4 ,3:1 ,4:2 ,5:0}

ans=[]

for i in range(6):# 바텀을 정한다. 0~5
    result = [] #각 주사위마다 옆면의 최대값 1개를 저장해둘 리스트 선언
    temp = [1, 2, 3, 4, 5, 6]
    bottom=Table[0][i]#밑바닥 설정
    top=Table[0][mapping[i]]
    temp.remove(bottom)
    temp.remove(top)#해당 수가 없다 발생함
    result.append(max(temp))

    
    for k in range(1,N):#이제 2층부터 계산을 실시한다. 1~5
        temp = [1, 2, 3, 4, 5, 6]
        bottom=top
        top=Table[k][mapping[i]]#위 설정
        temp.remove(bottom)
        temp.remove(top)
        
        result.append(max(temp))

    ans.append(sum(result))

print(max(ans))
        
    
