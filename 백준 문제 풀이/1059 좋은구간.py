#https://www.acmicpc.net/problem/1059

'''
import sys

L=int(sys.stdin.readline())   #집합의 크기
S=list(map(int, sys.stdin.readline().split()))#집합 내용물
n=int(sys.stdin.readline())

S.append(0)
S.sort()

if n in S:
    print(0)
    exit(0)


st=0
end=0

for i in range(L-1):
    if S[i]<n<S[i+1]:
        st=S[i]
        end=S[i+1]
        break


#print(st,end,'초과/미만 범위')

start=st+1    #포함 범위
ends=end-1    #포함 범위

mlist=list(range(start, ends+1))    #최종 합격자들

print(st,end)

#print(mlist, '실제 값 들어가는 배열')
#print(mlist, '범위')


cnt=0
for i in mlist:
    if i>=n:
        cnt+=1



summ=(n-min(mlist))*cnt + (cnt-1)
print(summ)
'''

import sys

L=int(sys.stdin.readline())   #집합의 크기
S=list(map(int, sys.stdin.readline().split()))#집합 내용물
n=int(sys.stdin.readline())

# 가장 중요한점: 암묵적으로 0이 들어가 있다고 생각 해야 한다.

S.append(0)    #0을 추가 한다.(이게 코드에서 정말 핵심 이라고 생각함)
S.sort()

# 범위에 걸치는 경우는 0
if n in S:
    print(0)
    exit(0)


st=-1
ed=-1
for i in range(len(S)-1):
    if S[i]<n<S[i+1]:
        st=S[i]
        ed=S[i+1]


mlist=list(range(st+1, ed))

#print(mlist)    [9, 10, 11, 12]
cnt=0

for i in range(len(mlist)-1):

    for k in range(i+1,len(mlist)):
        if mlist[i]<= n <=mlist[k]:
            cnt+=1

print(cnt)



















