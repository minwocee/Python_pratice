# https://www.acmicpc.net/problem/11723

'''

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)   # 이놈만 출력에 관여함
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다. 

'''

import sys

N=int(sys.stdin.readline())

Table=[False]*21#0~21

for _ in range(N):
    order=sys.stdin.readline().strip()

    if 'add' in order:
        k=int(order.split()[1])#숫자만 꺼냄

        Table[k]=True

    elif 'check' in order:
        k=int(order.split()[1])#숫자만 꺼냄

        if Table[k]:
            print(1)
        else:
            print(0)
    
    elif 'remove' in order: 
        k=int(order.split()[1])#숫자만 꺼냄

        Table[k]=False
    
    elif 'toggle' in order: 
        k=int(order.split()[1])#숫자만 꺼냄

        if Table[k]==True:
            Table[k]=False
        else:
            Table[k]=True
    
    elif 'all' in order:
        Table=[True]*21
    
    elif 'empty' in order: 
        Table=[False]*21
    
