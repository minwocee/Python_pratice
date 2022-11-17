# 2개의 행렬 A,B를 계산하는 아주 간단한 코드이다
































A=[]    
B=[]
Y,X=map(int, input().split())

for i in range(Y):
    P=list(map(int, input().split()))
    A.append(P)

for i in range(Y):
    K=list(map(int, input().split()))
    B.append(K)

for i in range(Y):
    for _ in range(X):
        print(A[i][_]+B[i][_],end=" ")
    print()


    

