# https://www.acmicpc.net/problem/16507

# 시간제한 1초, 메모리 제한 512MB
'''
import sys
# np.mode 최빈
# np.min 최소
# np.max  최대
# np.median 중앙
# np.meadn 평균

width, height, Test_case = map(int, sys.stdin.readline().split())


Photo = [list(map(int, sys.stdin.readline().split())) for _ in range(width)]


# 시간초과 오류 발생 할 확률이 높음(최악의 시간 복잡도 계산)
# 그럼 한개의 해쉬테이블을 만들어서 거기에 누적값을 저장하면 끝임


# 누적합 테이블 제작 시작하기
# 1. 0으로 초기 상태 크기만큼 초기화후 0,0을 실제 테이블 0,0으로 초기화함
# 2. 이후 첫번째 행 누적합 실행
# 3. 이후 첫번째 열 누적합 실행
# 4. 이후 나머지 영역 누적합 실행하면 끝

sum_table = [[0]*height for _ in range(width)]

sum_table[0][0]=Photo[0][0]

# 첫번째 행 초기화
for r in range(1,height):
    sum_table[0][r] = sum_table[0][r-1]+ Photo[0][r]
    
# 첫번째 열 초기화
for c in range(1,width):
    sum_table[c][0] = sum_table[c-1][0]+ Photo[c-1][0]
    
    
# 나머지 영역 초기화 (하이라이트임)
for row in range(1, width):
        for colum in range(1, height):
            
            # 다음 누적합 테이블은?   실제값목표점 1개 + 위에까지의 누적합 + 왼쪽 까지의 누적함 - (두개의 누적합의 교집합 부분 빼주기)
            sum_table[row][colum] = Photo[row][colum] + sum_table[row-1][colum] + sum_table[row][colum-1] - sum_table[row-1][colum-1]



# 한개의행, 한개의 열만 처리 할때 발생 하는 문제를 해결하기 위해 첫행,첫열을 0으로 초기화 함
# 그럼 이상한값 해결도 가능, 행-열을 1,1로 시작하는 형태로 만드는것이 가능하다.
sum_table=[[0]*(height+1)]+sum_table

for i in range(1,width+1):
    sum_table[i]=[0]+sum_table[i]

# 섬 테이블 출력 하기
# for _ in sum_table:
#     print(_)


# 누적합 테이블을 완성함, 이제 출력만 해주면 끝이다.
for _ in range(Test_case):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    
    A=sum_table[x2][y2]-sum_table[x2][y1-1]-sum_table[x1-1][y2]+sum_table[x1-1][y1-1]
    
    print( int(A/((x2-x1+1)*(y2-y1+1))))

'''



# 정답 코드
import sys

width, height, Test_case = map(int, sys.stdin.readline().split())

Photo = [list(map(int, sys.stdin.readline().split())) for _ in range(width)]

sum_table = [[0]*height for _ in range(width)]

sum_table[0][0]=Photo[0][0]

for r in range(1,height):
    sum_table[0][r] = sum_table[0][r-1]+ Photo[0][r]
    
for c in range(1,width):
    sum_table[c][0] = sum_table[c-1][0]+ Photo[c][0]
    
    
for row in range(1, width):
        for column in range(1, height):
            sum_table[row][column] = Photo[row][column] + sum_table[row-1][column] + sum_table[row][column-1] - sum_table[row-1][column-1]


sum_table=[[0]*(height+1)]+sum_table

for i in range(1,width+1):
    sum_table[i]=[0]+sum_table[i]


for _ in range(Test_case):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    
    A=sum_table[x2][y2]-sum_table[x2][y1-1]-sum_table[x1-1][y2]+sum_table[x1-1][y1-1]
    
    print( int(A/((x2-x1+1)*(y2-y1+1))))