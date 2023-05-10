# 이전에 풀어봤던 좌표 정렬하기의 Y좌표를 기준으로 출력을 해주는 문제
# N은 10만개까지 입력받음
# x,y 좌표는 -10만~+10만까지의 수가 들어감
# 위치가 같은 좌표는 없음



# 2차원 배열을 정렬할때 [a,b] [a,b+1]인경우 b가 작은 리스트가 먼저 온다!





























import sys

N=int(sys.stdin.readline())
array=[]

for _ in range(N):
    a,b=map(int,sys.stdin.readline().split())    #리스트 형태로 결과물 입력됨
    array.append([b,a])    # Y기준 정렬을 위해 맨앞에 Y값이 온다

array.sort()

[print(array[i][1],array[i][0])for i in range(N)]    #출력할떄는 x,y 형식 맞춰서 정상적으로 출력 한다.

























