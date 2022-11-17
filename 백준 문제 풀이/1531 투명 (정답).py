#2차원 리스트 구현을 응용
#리스트 컴프티 헨션을 활용해 [0]을 집어 넣어 주는게 핵심이다
































import sys



N, M = map(int, sys.stdin.readline().strip().split())

li = [[0]*100 for _ in range(100)]     #[0] 이라는 리스트를 한줄에 100번씩리스트 속에 넣는다 (리스트 컴프리헨션을 활용)
#[ [0,0,0,0,0,0,0,0,0,0,0.....], ]  [0,0,0,0,0,0,0,0,0,0,0.....],   [0,0,0,0,0,0,0,0,0,0,0.....],   ] 꼴로 들어간다


#모든 좌표는 1~100사이의 자연수이다
for _ in range(N):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    
    for X in range(x1, x2+1):      # 해당 2차원 리스트의 요소에 값을 더해주는 연산을 실행함
        for Y in range(y1, y2+1):    # 인덱스 번호에 +1해야 마지막 값을 선택할수 있다 
            li[X-1][Y-1] = li[X-1][Y-1]+1     #리스트의 값을 업데이트 해서 사용




counters=0     #가리는 타일을 계산
for i in range(100):       #100*100 검사 실행
    for j in range(100):
        if li[i][j] > M:    #만약 M보다 커지면 가려지게 됨
            counters += 1
print(counters)