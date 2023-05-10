# https://www.acmicpc.net/problem/1920

'''
예제 입력 1
5   # 검증해야하는 배열의 개수   100,000 개까지 가능
4 1 5 2 3    # 검증해야하는 배열의 원소들
5    # 검사하는 배열들
1 3 7 9 5    #검사관들

'''

# 방법1: 그냥 무지성 풀이 (N*M=10^10이 나오므로 시간초과 발생)
# import sys

# Test=int(sys.stdin.readline())
# Test_Table=list(map(int,sys.stdin.readline().split()))

# Check=int(sys.stdin.readline())
# Check_Table = list(map(int,sys.stdin.readline().split()))

# for i in Check_Table:
#     if i in Test_Table:
#         print(1)
#     else:
#         print(0)

# 방법2: 이분 탐색을 활용한다(오름차순 정렬이된 자료를 반으로 나눠서 탐색)
# log(N)이 시간복잡도이다.
"""
<준비물>
#오름차순으로 정렬된 숫자들

*target : 찾고자 하는 값
*data : 오름차순으로 정렬된 list
*start : data 의 처음 값 인덱스
*end : data 의 마지막 값 인덱스
*mid : start, end 의 중간 인덱스

<구현 개요>
자료의 중간 값이 (mid) 찾고자 하는 값인지 검사
아니라면 대소관계를 비교하여 start, end 값 이동
동일 연산 반복 (재귀로 구현 가능)
바이너리 서치 구현 (python)
# 바이너리 서치
# data 중에서 target 을 검색하여 index 값을 return 한다.
# 없으면 None을 return한다.
"""
'''
def binary_search(target, data):    # 찾는값, 리스트값
    data.sort()  # 오름차순 정렬
    start = 0    # 시작 인덱스
    end = len(data) - 1    # 마지막 인덱스 3칸이면 3-1=[2]

    while start <= end:    # 시작지점이 끝보다 커지면 종료
        mid = (start + end) // 2     # 중앙 인덱스 설정(리스트의 요소개수가 짝수개 이면 중앙값이 2개가 되지만 상관이 없다)
         
        if data[mid] == target:    # 중앙값이 내가 찾는 수와 같으면, 함수 종료
            return mid # 해당값 반환
        elif data[mid] < target:    #중앙값이 내가 찾고자 하는 값보다 작으면 실행
            start = mid + 1    # 다음 시작값은 현재시점의 중앙값보다+1칸 인덱스 이동
        else:     #중앙값이 찾고자 하는 값보다 크거나 같으면   
            end = mid -1    #끝 인덱스를 중앙인덱스-1로 만든뒤 다시 탐색을 실행

    return None
'''


# target ,start, min, end, table


def Binary_Search(Taget, Table):    
    # Table.sort() 본문에서 실행 완료
    start=0
    end=len(Table)-1
    

    while (start<=end):
        mid=(start+end)//2
        if Table[mid]==Taget:
            return 1    #자체 break 기능을 내장
        elif Table[mid]>Taget:    # 중앙값을 기준으로 target이 왼쪽에 있으면? end를 떙겨옴
            end=mid-1
        else:    # 중앙값을 기준으로 target이 오른쪽에 있으면 start를 떙겨온다고 생각
            start=mid+1
    return 0    #반복문이 끝나면 0을 return
        
import sys

Test=int(sys.stdin.readline())
Test_Table=list(map(int,sys.stdin.readline().split()))

Check=int(sys.stdin.readline())
Check_Table = list(map(int,sys.stdin.readline().split()))

Test_Table.sort()
for i in Check_Table:
    print(Binary_Search(i,Test_Table))



