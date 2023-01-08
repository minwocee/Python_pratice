import sys

정사각형=int(sys.stdin.readline())

mlist=[list(map(str, sys.stdin.readline().strip().split())) for _ in range(정사각형)]


king=0
cnt=0 #전체 관점
for _ in mlist:    #2차원 리스트 내용물 들어감
    #print(_)
    if '5' in _:
        king=(_.index('5'),cnt) #튜플 형태로 좌표 전달 (x,y)
        break 
    cnt+=1


slave=0
cnt=0 #전체 관점
for _ in mlist:    #2차원 리스트 내용물 들어감
    if '2' in _:
        slave=(_.index('2'),cnt) #튜플 형태로 좌표 전달 (x,y)
        break 
    cnt+=1

"""불필요한 행자르기 시전"""
top=max(king[0],slave[0])   # 둘중에 더 큰게 오른쪽
bottom = min(king[0], slave[0])    # 둘중에 더 작은게 왼쪽

mlist2=[absol[bottom:top+1] for absol in mlist]

"""불필요한열 자르기 시전"""
top=max(king[1],slave[1])   # 둘중에 더 큰게 밑줄에 존재
bottom = min(king[1], slave[1])    # 둘중에 더 작은게 윗줄에 존재


cnt=list(range(bottom,top+1))
#print(cnt)

temp=0

ans=[]
for _ in mlist2:
    if temp in cnt:
        ans.append(_)
    temp+=1



'''현재 ans에는 자르기 완료한 깔끔한 상태가 되었다.'''
# for _ in ans:    # 2차원
#     print(_)


# 이제 거리가 5 이상인지 점검을 실시해보자

"""
1.
0***0
0****0   #이 개념으로 거리를 구하는게 맞다
0*****0
"""

cnt1=0
if ((len(ans[0])-1)**2 + (len(ans)-1)**2)<25:    #두사람의 거리가 5 이하이면 *중요* 위의 개념을 인지 하자 , 인덱스 번호와 len의 차이 
    print(0)
    exit(0)
    
else:     #거리가 5이상은 충족함, 그럼 이들 사이에 1의 개수가 3개 이상인지 검사를 실행
    # 다른학생들의 개수를 세는 변수
    for _ in ans:
        for i in _:
            if i=='1':
                cnt1+=1
                if cnt1>=3:
                    print(1)
                    exit(0)    #강제 종료
                
        
if cnt1<3:
    print(0)