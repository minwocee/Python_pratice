
N,M=map(int, input().split())    #7명, 11일
firstlist=list(map(int,input().split()))    #N명 만큼 초기 배치를 넣음(이 규칙대로 인덱스 참고) 5 6 2 1 7 3 4

a = []    # 전체리스트속 리스트를 생성(이중 배열)
 
for i in range(M):
    line = []              # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(N):
        line.append(0)     # 안쪽 리스트에 0 추가
    a.append(line)         # 전체 리스트에 안쪽 리스트를 추가
 
"""
1일째: 5 6 2 1 7 3 4    (최초 선언 규칙)
2일째: 7 3 6 5 4 2 1
3일째: 4 2 3 7 1 6 5
"""

rulelist=[]
for i in range(N):     #sl에 쓰레기값 넣음
    rulelist.append(0)

for i in range(N):     #tl에 쓰레기값 넣음
    rulelist[i]=firstlist[i]
print(rulelist, "움직이는 규칙들 정상적으로 삽입 완료")    #5 6 2 1 7 3 4

for i in range(1,M):    #M=11 1,2,3,4...11
    for p in range(N):
        c=firstlist[p]
        a[i][p]=rulelist[c-1]
    
    for q in range(N):    #룰 리스트를 업데이트
        rulelist[q]=a[i][q]

print(a[-1])
   


