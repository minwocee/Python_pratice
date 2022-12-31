# https://www.acmicpc.net/problem/2609


# 두개의 자연수를 입력받아 최대공약수와 최소 공배수를 출력하는 프로그램 


def 최대공약수(A,B):    #공통의 약수중에서 가장 큰수
    if A==B:     #둘이 같은 수일 경우
        return A
    elif A>B:    # 10 5 인 경우
        for k in range(B,0,-1):
            if A%k==0 and B%k==0:   #나누어 떨어지면 최소 공배수
                return k
    else:
        for k in range(A,0,-1):
            if A%k==0 and B%k==0:   #나누어 떨어지면 최소 공배수
                return k

def 최소공배수(A,B): # 2*N==3*N이 되는 배수중에서 가장 작은 정수
    if A==B:
        return A

    
    for i in range(1,A*B+1):    # 1~ A*B 까지 하나씩 넣어주면서
        if i%A==0 and i%B==0:    # 해당 요소가 A,B 둘다 나누어 떨어지는 경우
            return i    # i를 출력 한다.



import sys

A,B = map(int, sys.stdin.readline().split())

print(최대공약수(A,B))   # 해결 완료
print(최소공배수(A,B))