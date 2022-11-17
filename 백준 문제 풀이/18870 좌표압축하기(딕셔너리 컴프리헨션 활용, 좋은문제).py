# 크기가 작은 정수부터 0순위, 1순위 ,2순위를 부여해서 출력 하는 문제
# 현재 시간초과가 발생함 다른 방법을 찾아야 함




































# 시간초과 나서 다시 품

# import sys



# N=int(sys.stdin.readline().strip())

# mlist=list(map(int, sys.stdin.readline().strip().split()))

# answerlist=[-1]*1_000_001

# sortlist=sorted(set(mlist))    #정렬한 리스트를 생성함


# # 낮은 숫자를 가진 인덱스 요소에 번호를 부착한다
# for k in range(len(sortlist)):
#     for i in range(N):
#         if sortlist[k]==mlist[i]:
#             answerlist[i]=k

# [print(i,end=" ") for i in answerlist if i!=-1]


import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))     #초기 정수 들어가는 리스트

arr2 = sorted(set(arr))     #중복을 제거하고 다시 오름차순 리스트 정렬을 완료 함

mydic = {arr2[i] : i for i in range(len(arr2))}    # 딕셔너리도 컴프리헨션 사용이 가능하다(중요함)

for i in arr:    #초기 값이 하나씩 들어감
    print(mydic[i], end = ' ')