# 메모리 초과하는 문제가 발생함 
# 이를 해결하기 위해 색다른 방법을 사용한다



























import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001    # 10001개 길이의 리스트를 생성한다

for _ in range(n):    # 특이한 접근방법: 인덱스 번호를 입력받고 해당위치값 1 증가
    num_list[int(sys.stdin.readline())] += 1    #해당 리스트 칸에 1만큼 증가

for i in range(10001):
    if num_list[i] != 0:    #해당 인덱스 요소값이 0이 아니면 실행
        for j in range(num_list[i]):    #인덱스에 위차한 값의 개수만큼 반복(1이 얼마만큼 더해지는가가 핵심)
            print(i)                    #해서 실행을 한다(처음보는 신기한 방법 기억해두어야 한다)