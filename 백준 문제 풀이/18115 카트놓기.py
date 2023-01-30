# https://www.acmicpc.net/problem/18115

'''
핵심--> 내 손으로 그림 그려보기

1. 행동지령을 거꾸로 보면서 바닥에서 손으로 돌리는 과정을 생각하기
2. 내 손패을 deque로 두는것이 좋다.
'''

from collections import deque
import sys

N=int(sys.stdin.readline())

order = list(map(int, sys.stdin.readline().split()))

order=order[::-1]    # 행동순서를 역순으로 바꿔주기
ans_list=deque()    # 손 카드팩을 디큐화 한다.

num=1


for o in order:
    if o==1:    #손 맨 위에 놓기(왼쪽이 위, 오른쪽이 아래)
        ans_list.appendleft(num)
        

    elif o==2:    #손 위에서 두번쨰 삽입
        ans_list.insert(1,num)    #인덱스 1번 위치에 num을 삽입한다.
        
    
    elif o==3:    #손 맨 밑에 카드 넣기(왼쪽이 위, 오른쪽이 아래)
        ans_list.append(num)
    num+=1


for i in ans_list:
    print(i, end=' ')