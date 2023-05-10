# https://www.acmicpc.net/problem/10816


import sys

Original=int(sys.stdin.readline())
Original_list=list(map(int, sys.stdin.readline().strip().split()))

Check=int(sys.stdin.readline())
Check_list=list(map(int, sys.stdin.readline().strip().split()))

ans_list=[]

for _ in Check_list:
    counter=0
    for k in Original_list:
        if _ == k:
            counter+=1
    ans_list.append(counter)

for _ in ans_list:
    print(_,end=' ')
















