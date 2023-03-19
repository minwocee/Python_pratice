# https://www.acmicpc.net/problem/14391

# 딱봐도 최적화 문제이다(그리디)

# 가로로 자를 경우에는 왼쪽에서 -> 오른쪽으로 숫자를 읽으면 된다.
# 세로로 자를 경우에는 위에서 -> 아래로 숫자를 읽으면 된다.
# 단 023 같은 경우는 23으로 해석하면 된다. (나중에 0을 제거하는 과정을 거치면 된다.)


def rkfh(Field):
    ans=0
    
    for _ in Field:
        clk=False
        ak=_
        
        for k in _:
            if k=='0' and clk==False:
                ak.remove('0')
            else:
                clk=True
        
        ans+=int(ak[0])        
    return ans




def tpfh(Field,M):
    ans=0
    
    for m in range(M):
        
        for _ in Field:    # 필드에서 한줄 씩 가져 온다.
            ak+=_[m]
        # 여기 마저 작업하기
                   
        P=ak
            
        for k in ak:
            if k=='0' and clk==False:
                P.remove('0')
            else:
                clk=True
        
        ans+=int(P[0])
    
    return ans

import sys

# 최대 4*4로 진행 된다.
N,M=map(int,sys.stdin.readline().split())    # 높이,가로 길이 입력 받는다.

Field=[list(sys.stdin.readline().strip().split()) for _ in range(N)]



print(rkfh(Field), tpfh(Field,M))
# 가로로 자르는 경우의수


# 세로로 자르는 경우의 수