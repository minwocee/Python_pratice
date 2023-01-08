import sys
from itertools import permutations
N=int(sys.stdin.readline())# 총 좌석의 개수
fixed=int(sys.stdin.readline())# 고정석의 개수

Table=list(range(1,N+1))
ans=[]
start=0
end=0
for _ in range(fixed):
    fixed_spot=int(sys.stdin.readline())    #고정석의 좌표를 입력 받는다.
    end=fixed_spot-1
    ans.append(Table[start:end])
    start=fixed_spot

ans.append(Table[start:len(Table)])
#print(ans, '슬라이싱 결과')
# 일단 슬라이싱을 해보자


combined=[]  #NCR의 결과를 담을 리스트

for i in range(len(ans)):
    if len(ans)>=3:
        combined.append(len(list(permutations(ans[i],2))))

k=1
#print(combined, '콤바인드 결과')
for i in combined:
    k*=i
print(int(k/fixed))

