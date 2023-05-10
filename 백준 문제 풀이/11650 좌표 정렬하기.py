# 좌표를 정렬하는 문제
# 조금 어려운 문제임







































# import sys

# N=int(sys.stdin.readline().strip())

# arr1=[]
# arr2=[]


# for i in range(N):
#     a1,a2=map(int,sys.stdin.readline().strip().split())
#     arr1.append(a1)
#     arr2.append(a2)

# arr1.sort()
# arr2.sort()


# for i in range(N):
#     print(arr1[i], arr2[i])
# 11650번 : 좌표 정렬하기
import sys


n = int(sys.stdin.readline())

array = []

for i in range(n):
    [a, b] = map(int, input().split())     #2개의 요소를 가지는 리스트를 생성함
    array.append([a, b])     #리스트속에 리스트가 들어가는 형태

s_array = sorted(array)    #2차원 리스트 정렬을 시작한다

for i in range(n):
    print(s_array[i][0], s_array[i][1])









