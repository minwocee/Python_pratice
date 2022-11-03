import sys    #파이썬 입력 속도 증가시키는 함수

N=int(sys.stdin.readline().strip())    #sys.stdin.readline()으로 입력 받고 .strip()으로 엔터키문자 제고


mlist=[]    #확장자들이 들어가있는 리스트(아직까지는 중복된 확장자와 알파벳별 정렬이  안된 상태)

for _ in range(N):    #나중에 조금더 줄여보도록 하자
    mlist.append((sys.stdin.readline().strip().split('.'))[1])

checkli=list(set(mlist))     #중복을 제거후, 알파벳 정렬을 마친 확장자들의 모음

for i in range(len(checkli)):
    print(checkli[i], mlist.count(checkli[i]))

