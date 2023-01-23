# https://www.acmicpc.net/problem/2805
'''
import sys

# 나무의 개수, 가져가야할 나무길이
Tree , Take_tree = map(int, sys.stdin.readline().split())

# 나무 길이정보 리스트 입력받는다.
Tree_list=list(map(int, sys.stdin.readline().split()))

start=0
end=max(Tree_list)

while(start<=end):

    middle=(start+end)//2
    summ=0

    for tree in Tree_list:
        if tree-(middle)>0:    #자른 나무가 존재하면
            summ+=tree-(middle)    #나무의 총합



    # 현재 나무 다 자름
    if summ>Take_tree:
        end=middle-1
    else:
        start=middle+1

# 앞영역 : True
# 뒷영역 : False


# 다른분의 코드를 분석하자
N, M = map(int, input().split())    #나무개수, 원하는 나무토막
tree = list(map(int, input().split()))    #나무 길이 리스트
start, end = 1, max(tree) #이분탐색 검색 범위 설정(인덱스값이 아닌 요소값)

while start <= end: #적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2    #중앙값(index 번호 아님), 톱날의 위치라고 생각
    
    log = 0    #벌목된 나무 총합
    for i in tree:    #나무 하나 하나씩 꺼내서 검사함
        if i >= mid:    # 만약 선택한 나무가 톱날의 높이보다 크면
            log += i - mid     #벌목을 진헹한다(바구니에 담는다.)
    
    #벌목을 마치고, 원하는 나무토막을 만족하는지 검사합나다.
    if log >= M:    #만약 필요한 나무의 양보다 더 많이 자르거나 같으면, 
        start = mid + 1    #톱의 높이를 올린다.
        print(start,'나무가 너무 많아요')
    else:    #벌목양이 부족하면?( log<M 일 때 )
        end = mid - 1    #톱의 높이를 낮춘다.
        print(end,'나무가 조금요')
print(end)     #톱날이 왔다 갔다 했을때 가장 조금 자르는 수

"""
이분탐색
착각1: start,end가 무조건 인덱스 번호는아님
착각2: 무조건 target값을 찾는게 아님

"""
'''
    


import sys

N,M=map(int, sys.stdin.readline().split())

Tree_list=list(map(int, sys.stdin.readline().split()))

start=1    #나무의 길이는 1 이상
end= max(Tree_list)

while(start<=end):
    middle=(start+end)//2
    벌목총합=0
    for T in Tree_list:
        if T>middle:   #만약 잘리면
            벌목총합+=T-middle    #벌목 총합
    
    # 나누기 시작
    if 벌목총합>=M:#나무 너무 많이 자름
        start=middle+1
    else:
        end=middle-1

print(end)



