# 나중에 최빈값만 다시 짜보자



















def tops(mlist):
    count=1
    top=0
    
    for i in range(len(mlist)-1):
        if mlist[i]==mlist[i+1]:
            count+=1
            top = max(top, count) # 여기서 구현 최적화
        elif mlist[i]!=mlist[i+1]:
            top = max(top, count) 
                
        count=1
    return top

def 산술평균 (list_):
    return round(sum(list_)/len(list_))


def 최빈값 (mlist):    #이때 mlist는 이미 정렬을 마친 상태이다
    
    top=tops(mlist)
    
    count=1
    reals=[]    #정답리스트

    for i in range(len(mlist)-1):    #최빈값과 비교해서 정답리스트에 넣어줌
        if mlist[i]==mlist[i+1]:
            count+=1
        elif mlist[i]!=mlist[i+1]:
            if top==count:
                reals.append(mlist[i])
            count=1
                                               
    # answer=list(set(mlist))
    # answer.sort()

        #if top==mlist.count(answer[i]):    #이 부분 다시 짜야함
        #    reals.append(answer[i])

    if len(reals)==1:
        return reals[0]
    else:
        return reals[1]
            


import sys

N=int(sys.stdin.readline().strip())

mlist=[int(sys.stdin.readline().strip()) for _ in range(N)]

mlist.sort()

if len(mlist)==1:
    print(산술평균(mlist))
    print(mlist[0])
    print(mlist[0])
    print(0)
else:
# 산술평균을출력
    print("%d" % 산술평균(mlist))


# 중앙값을 출력
    print("%d" % mlist[round(len(mlist)/2)])


# 최빈값을 출력 NULL
    print(최빈값(mlist))

#범위 출력
    print(max(mlist)-min(mlist))
