# 그래프 탐색 문제이다.
# 이번 기회에 그래프 탐색을 박살내겠다
'''
test 케이스1
<입력>
11 5
9
2
4
5
11

<출력>
0
0
2
2
2


test case 2
<입력>
11 5
1
2
3
4
5

<출력>
0
1
1
1
1
1
'''
import sys
import math
# x = 8
# result = math.log(x, 2)  #log2에x승을 의미한다.
# print(result)

# 땅 개수, 오리 개수
Ground, duck = map(int, sys.stdin.readline().split())

# 인덱스 1번부터 사용할 예정임
graph = [False]*(Ground+1)

for i in range(duck):
    Want=int(sys.stdin.readline())
    b = Want
    
    # 뭔가 이거 바텀업 방식으로 하는게 맞는것 같다
    조상님과가장가까운True노드번호=-1
    while(Want!=1):
        # 1회 조상님 방문 거슬러 올라가기
        if graph[Want]:    #True면 누가 땅 먹은곳에서 만나게 됨
            조상님과가장가까운True노드번호=Want
        Want//=2    # 이것 때문에 틀림 57행에 넣어서

    # 올라가면서 단 한번도 주인있는 땅을 만나지 않음
    if 조상님과가장가까운True노드번호 == -1:
        print(0)    #, "막히지 않음"
        graph[b] = True
    else:
        print(조상님과가장가까운True노드번호)    #, "이 노드에서 막혔음"