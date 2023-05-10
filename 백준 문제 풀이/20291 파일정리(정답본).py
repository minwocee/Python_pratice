import sys 

N=int(sys.stdin.readline().strip())    #sys.stdin.readline()은 입력을 받고 strip()은 개행문자를 제거

mlist=[sys.stdin.readline().strip().split('.')[1] for _ in range(N)]
#리스트 컴프리 헨션 사용해서 스플릿 한후 뒤에것 인덱스를 선택함


mlist.sort()    #정렬
mlist.append(0)    #아래의 반복문을 쓰기위해 쓰레기값 더함(i+1)을 방지하기 위해

counter=1    #카운터 세는 변수

for i in range(len(mlist)-1):    #자신과 다음 숫자를 비교하는 반복문
    if mlist[i]==mlist[i+1]:
        counter+=1
    elif mlist[i]!=mlist[i+1]:
        print(mlist[i],counter)
        counter=1
