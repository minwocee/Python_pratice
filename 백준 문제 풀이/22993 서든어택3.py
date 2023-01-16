# https://www.acmicpc.net/problem/22993
import sys


N= int(sys.stdin.readline())


# 준원이가 A[0]임

table = list(map(int,sys.stdin.readline().split()))

'''
5
2 1 2 3 4
'''

# 나보다 낮은애들을 잡아먹을수 있음
my_at=table[0]

mlist=table[1:]

mlist.sort()

if N==1:
    print("Yes")
    exit(0)

for i in mlist:
    if my_at>i:
        # print(i,"흡수")
        my_at+=i
        # print(my_at, "내공격력")
    

if my_at>mlist[-1]:
    print("Yes")
else:
    print("No")
