import sys

N=int(sys.stdin.readline().strip())    #숫자 입력 받음

mlist=[sys.stdin.readline().strip().split('.')[1] for _ in range(N) ]    #리스트 컴프렌션

checklist=sorted(set(mlist))

[print(checklist[i], mlist.count(checklist[i])) for i in range(len(checklist))]    #리스트 컴프렌션