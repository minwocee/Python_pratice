# 2차원 배열을 활용(딕셔너리도 써보자)






# 검은색이 핵심
# 교집합을 리스트로 생성해서 결과 리스트에 넣고 정렬하고 연속된 리스트가 가려지는 기준을 넘으면
# 10000개에서 -1을 실행한다





















def dark_area(x1,y1,x2,y2):
    darkpp=[]
    
    for y in range(y1,y1+y2+1):
        for x in range(x1,x1+x2+1):
            darkpp.append(y*100+x)
            
    return darkpp







import sys

N, M=map(int,sys.stdin.readline().strip().split())    #색종이개수, 가려지는 기준


answer=[]
for i in range(N):
    x1,y1,x2,y2=map(int,sys.stdin.readline().strip().split())    #좌표 입력받음
    answer+=dark_area(x1,y1,x2,y2)

print(101*101)
print(101*101-len(set(answer)))


# counters=1
# allting=0
# for i in range(len(answer)-1):
#     if answer[i]==answer[i+1]:
#         counters+=1
#     elif answer[i]!=answer[i+1]:
#         if counters>M:   #보이지 않는 경우
#             allting+=1
#         counters=1
            


# print(allting)



