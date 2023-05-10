# N은 50만개까지 주어진다. 
# 큐를 쓰는 문제인가

"""
<Case 1>
N=4 
(1)234
234
(3)42
42
(2)4

<Case 2>
N=6
(1)23456
(3)4562
(5)
624
246

"""

# 방법1 큐를 이용해서 풀이 (큐는 한방향으로만 입력, 출력이 가능한 구조)

# def my_queue(N):
#     N_list=list(range(1,N+1))
#     while(len(N_list)!=1):   #한줄 남을 때 까지 반복
#         #1번 규칙 적용 (맨앞 날리기)
#         N_list.pop(0)
#         #2번 규칙 적용 (맨앞 뒤로 보내기)
#         N_list.append(N_list.pop(0))
#     return N_list[0]
    

# import sys

# N=int(sys.stdin.readline())
# print(my_queue(N))

# 방법2 덱 (deque)를 이용해서 풀이하자 (양방향에서 풀이가 가능한 문제)
import collections    # 이 방식을 사용하면 collections 
from collections import deque    #덱 방식 활용을 위해 선언
import sys


N = int(sys.stdin.readline())    
my_deque = deque(list(range(1,N+1)))

while(len(my_deque) !=1):
    my_deque.popleft()    
    # *핵심* deque는 양뱡향 연결리스트라서 popleft를 사용하면 
    # 시간복잡도는 O(1)이다. (그냥 연결을 끊어버림)
    # queue에서는 pop()은 O(N)이다. (삭제하고 연결을 끊어버림)
    my_deque.append(my_deque.popleft())    #오른쪽으로 추가를 하는 함수
    # my_deque.appendleft(my_deque.popleft()) 왼쪽에서 추가를 하는 함수
    
print(my_deque[0])
 



# 출력 패턴을 찾아서 푸는 방법 

# input = int(input())
# square = 2

# while True:
#     if (input == 1 or input == 2):
#         print(input)
#         break
#     square *= 2
#     if (square >= input):
#         print((input - (square // 2)) * 2)
#         break








