# https://www.acmicpc.net/problem/16967

# 배열 A가 있다고 쳐보자
"""
1 2 3
4 5 6
7 8 9
"""

#근데 이걸 숫자1을 기준으로 좌표이동을 한다 해보자(X, Y)   여기서는 (1,1) 이동을 한다 치자
# 겹치는부분을 더하고 안겹치면 그냥 0으로 놓는다.
# 이렇게 이동을 반복하면
"""  2*4 배열을 1,1만큼 위치 이동을 하면 발생하는 결과
1  2  3  4  0
5  7  9  11 4
0  5  6  7  8
"""
# 단 문제에서는 역으로 결과물을 주어지고 변환을 실시해서 원본배열을 찾는게 목적이다.

# 한번 움직인 배열의 규칙을 찾고 역으로 반환을 진행해서 구해보는 방식을 생각해보자



# import sys

# Original_Rows,Original_Colums, Move_Row, Move_Colum = map(int ,sys.stdin.readline().split())    # 행개수, 열개수, X축 움직임, Y축 움직임

# # 이제 입력받음

# Table=[list(map(int, sys.stdin.readline().split()))for _ in range(Original_Rows+Move_Row)]

# # 해당 2차원 배열의 내용물에 정수 0이 없으면 인커전(겹침)이 발생하는 배열이고 양끝을 제외한 부분이 중복합이 발생을 한다. 

# Answer=[]

# for i in Table:     #리스트를병합하는 과정
#     if 0 in i:
#         Answer.extend(i)    #하나의 리스트로 이어준다.

# for i in range(len(Answer)):     #0 제거하는 반복문을 실행한다.
#     try:
#         Answer.remove(0)
#     except(ValueError):    #만약 0을 모두 삭제하면 실행을 한다.
#         break

# set(Answer)
# Answer=list(Answer)

# for a in range(0,len(Answer),Original_Colums):    #이제 규칙에 맞게 출력을 실시한다
#     for b in range(a,a+Original_Colums):
#         print(Answer[b],end=' ')
#     print()

"""  다른분의 코드 참고"""
import sys

h, w, x, y = map(int, sys.stdin.readline().rstrip().split())    #행 열 X이동 Y이동
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h+x)]    # 나라면 [[0]]*10 이런식으로 할듯

def solve():
    recovered_arr = [[0 for _ in range(w)] for _ in range(h)]    # 나라면 [[0]]*h 이런식으로 할듯 컴프리헨션안쓰고
    check = [[0 for _ in range(w)] for _ in range(h)]
    #여기서부터가 분석의 시작
    for i in range(h):     #행반복
        for j in range(w):     #열반복
            if i < h and j < w:
                check[i][j] += 1     #모든요소에 +1을 해준다 (기본)
            
            if i+x < h and j+y < w:     #좌표이동후 겹치게되는 부분에 다시 +1을한다(2가되면 겹치기 시작)
                check[i+x][j+y] += 1

    for i in range(h):     #행반복
        for j in range(w):     #열반복
            if check[i][j] == 1:     #만약 해당 요소가 1이면(겹치지가 않으면)
                recovered_arr[i][j] = arr[i][j]    #그냥 그대로 결과값에 넣어주고
            
            elif check[i][j] == 2:     #만약 해당 요소가 2이면 (본격적인 중복겹침합이 발생한다)
                recovered_arr[i][j] = arr[i][j] - recovered_arr[i-x][j-y]     #원본배열에서 정답배열의 위치히동한 인덱스 만큼 뺼셈을 하고 넣어준다.
    
    for i in range(h):     #행반복
        for j in range(w):     #열반복
            print(recovered_arr[i][j], end=' ')     #이제 정답지 출력을 실행한다.
        print()     #엔터키 눌러주는 역할

solve()     #정답을 출력하는 함수 실행

# 이걸 푼 사람은 정말 배열에 대한 이해가 뛰어나다고 생각이 된다 정답지에 순차적으로 0부터 인덱스를 넣어두되, 겹치는 부분 (정수2)
# 가 발생하면 해당 좌표의 위치에서 [i-x][j-y]를 실행해서 정답 배열에서 불러와서 뺄셈을 실행한다(정답 인덱스는 순차적으로 넣어주었기 떄문에 존재한다는게 문제의 핵심)