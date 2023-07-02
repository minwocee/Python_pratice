import sys

N = int(sys.stdin.readline())

mlist = list(map(int, sys.stdin.readline().split()))

# 정렬을 할 필요는 없다고 생각한다.
a,b=0,1    # a포인터,b포인터 생성 (c포인터는 유동적으로 바꿀 예정 이다.)
ans_cnt = 0
mlist.sort()
print(mlist, '정렬된 리스트')
def binary(lis, kin, a1, b1):
    start = 0
    end = len(lis)-1  
    while(start<end):
        #print('시작숫자', lis[start])
        #print('끝숫자', lis[end])
        middle = (start+end)//2
        #print('중간숫자', lis[middle])
        
        
        if kin+lis[middle]==0:
            return 1
        elif kin+lis[middle]<0:
            start = middle+1
        else:
            end = middle-1
        
    return 0
    

for A in range(0,N-2):
    for B in range(A+1, N-1):
        serch_list = mlist[B+1:]
        ans_cnt+=binary(serch_list,king, mlist[A], mlist[B])
    
print(ans_cnt)

