# #https://www.acmicpc.net/problem/10836

# import sys

# 격자, 경과일 = map(int, sys.stdin.readline().split())    

# Table = [[1]*격자 for _ in range(격자)]   #1로 초기화된 격자를 만들었다.

# for i in range(경과일):    
    
#     # 우선 격자 크기에 맞는 1로 초기화된 배열을 만들어 보자
    
#     # +0 +1 +2 의 개수가 차례대로 들어가게 된다.
#     zero, one, two = map(int,sys.stdin.readline().split())
#     """
#     [[0][1][2]
#     [3][4][5]
#     [6][7][8]]
#     어떻게 인덱스를 뽑아낼것인가
#     0, 0+격자,0+2격자 
#     """
#     밥줄=[]
#     # 
#     #for _ in range(2*격자-1):     #2*격자-1가 밥줄 리스트의 길이라고 생각하자 격자의 길이만큼 밥줄을 입력함
#     for _ in range(zero):
#         밥줄.append(0)
#     for _ in range(zero):
#         밥줄.append(1)
#     for _ in range(zero):
#         밥줄.append(2)
    
#     # 이제 밥줄을 만든 리스트를 생성 완료 하였다 [0,0,0,1,1,1,2,2,2] 꼴이다.

#     #열 밥주기 완료
#     for i in range((격자*격자)-1-격자,0,-격자):
#         Table[i][0]=Table[i][0]+(밥줄.pop(0))
#     #행밥주기 완료
#     for i in range(격자):
#         Table[i][0]=Table[i][0]+(밥줄.pop(0))
#     print(Table)
# """
# 2 3
# 1 1  
# """
    
# import sys


# def around_grow(array):    #
#     for i in range(1, m):
#         for j in range(1, m):
#             array[i][j] += array[0][j] - 1


# def grow(array, grow_array):  # 
#     cnt = 0
#     for j in range(m - 1, -1, -1):
#         array[j][0] += grow_array[cnt]
#         cnt += 1
#     for j in range(1, m):
#         array[0][j] += grow_array[cnt]
#         cnt += 1


# if __name__ == "__main__":
#     m, n = map(int, sys.stdin.readline().split())
#     array = [[1] * m for _ in range(m)]
#     # 애벌래 초기 배열 선언
#     grow_array = [0] * (2 * m - 1)    #밥줄의 길이 만큼 0으로 초기화를 진행함
    
#     for _ in range(n):     #밥 규칙 배열 (append를 사용하지 않아서 시간을 절약함)
#         a, b, c = map(int, sys.stdin.readline().split())
#         for i in range(a, a + b):
#             grow_array[i] += 1
#         for i in range(a + b, 2 * m - 1):     
#             grow_array[i] += 2

#     grow(array, grow_array)    #기존 배열에 밥줄 규칙에 따른 왼쪽 아래에서부터 0,0 (0,격자) 까지 r모양으로 초기화를 실행 한다.
#     around_grow(array)

#     for i in range(m):
#         print(" ".join(map(str, array[i])))

import sys

M,N=map(int, sys.stdin.readline().split())    #격저사이즈, 몇일 실험할건지 입력 받음

L=[[1 for j in range(M)] for i in range(M)]# 2차원 배열 형태로 모든 요소를 1로 초기화함
day=[0 for i in range(2*M-1)]#밥줄을 의미, 일단 0으로 모든 값을 초기화 한다.



for _ in range(N):
    z,o,t=map(int,sys.stdin.readline().rstrip().split())#zero, one, two의 개수를 입력 받는다.
    for i in range(z,z+o):#+1이 되는 구간을 설정
        day[i]+=1
    for i in range(z+o,2*M-1):#+2가 되는 구간을 설정한다.
        day[i]+=2

#왼쪽 첫째 열
for i in range(M-1,-1,-1):
    L[i][0]+=day[M-1-i]#첫번째 열부터 밥주는걸 시작 한다.

#위쪽 첫째 행 [0]인덱스는 위에서 채워주었다.
for j in range(1,M):
    L[0][j]+=day[M-1+j]# 

#1열 이후라인
for j in range(1,M):#열 정보를 담당할 예정
    for i in range(1,M):#행 정보를 담당할 예정    
        L[i][j]=L[i-1][j]#첫번쨰 열을 제외한 값들은, 모든행이 첫번쨰 행과 같다는 의미

for i in L:
    print(*i)    #Unpaking operater * 을 의미, 이쁘게 출력할떄 사용 한다. [, ] 없애주는 역할





