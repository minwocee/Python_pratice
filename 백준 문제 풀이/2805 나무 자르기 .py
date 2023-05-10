# https://www.acmicpc.net/problem/2805

# 이진탐색 함수를 구현 해보자

# start(index), end(index), middle(index), 정렬된 리스트, 타겟값
'''
def binary_search(sort_list, target):
    # 시작값 설정
    start=0    #시작 인덱스
    end=len(sort_list)-1    #마지막 인덱스
    

    while start<=end:
        middle=(start+end)//2

        if sort_list[middle]==target:
            return middle    #찾는 값의 인덱스번호를 반환한다.
        elif target<sort_list[middle]:
            end=middle-1
        elif target>sort_list[middle]:
            start=middle+1

def binary_search1(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        print(mid)
        if data[mid] == target:
            return mid # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return None

mlist=list(range(1,100))    # 0~99까지의 정수가 들어간다.

print(binary_search1(50,mlist))

print(mlist.index(50), '50의 인덱스 번호')
'''

import sys

# 나무의 개수, 가져가야할 나무길이
Tree , Take_tree = map(int, sys.stdin.readline().split())

# 나무 길이정보 리스트 입력받는다.
Tree_list=list(map(int, sys.stdin.readline().split()))
'''
20 15 10 17 로 나무의 길이를 입력받았다고 가정
그럼 가장 길이가 큰 20부터 잘라내는걸 시작해보면 좋을것같다

나무의 길이에 따른 획득 길이
20    (0,0,0,0)     --> 나무길이 0 달성
19    (1,0,0,0)     --> 나무길이 1 달성
18    (2,0,0,0)     --> 나무길이 2 달성
17    (3,0,0,0)     --> 나무길이 3 달성
16    (4,0,0,1)     --> 나무길이 4 달성
15    (5,0,0,2)     --> 나무길이 7 달성
14    (0,0,0,0)

'''
# 일단 큰 나무를 기준으로 잘라내기를 하면서 얻은 합을 바탕으로
# 정렬된 리스트를 만들어 보고, 이걸 이분탐색을 활용하여 찾은뒤
# 가장길이가 큰 나무 - target의 인덱스 결과가 우리가 원하는 답이다!

# 난 천재인가?


# 이제 이진트리 탐색을 위한 리스트를 만들어보자
# 만약 내가 찾고자 하는 값이 없으면 인위적으로 값을 넣어주고 +1한 인덱스 번호를 반환하면 좋을것 같다

#ans_list={0}    # 집합 형태로 만들자 어차피 중복값은 존재하지 않는다.
ans_list=[]

king=max(Tree_list)
for i in range(0,king+1):
    summ=0
    for tree in Tree_list:
        if tree-(king-i)>0:
            summ+=tree-(king-i)
    ans_list.append(summ)

#ans_list=list(ans_list)

#ans_list.sort()    #정렬된 리스트 생성 완료
#print(ans_list)
start=0
end=len(ans_list)-1


while(start<=end):
    middle=(start+end)//2
    
    if ans_list[middle]==Take_tree:
        break
    elif ans_list[middle]<Take_tree:
        start=middle+1
    elif ans_list[middle]>Take_tree:
        end=middle-1


#print(middle)
#print(ans_list)
print(king - middle)
    
