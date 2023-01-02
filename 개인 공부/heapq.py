from heapq import heappush as push

# 힙 생성은 그냥 파이썬에서 리스트 형태로 사용하면 된다.

my_hip=[]

# heappush를 사용해서 (힙변수명, 원소) 식으로 진행을 한다.
push(my_hip, 4)
push(my_hip, 1)
push(my_hip, 2)
push(my_hip, 3)
push(my_hip, 5)
push(my_hip, 6)

print(my_hip)

#힙은 기본적으로 이진트리의 구조를 채택해서 사용 한다.