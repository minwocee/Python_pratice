import sys

N=int(sys.stdin.readline().strip())

mlist=[int(sys.stdin.readline().strip()) for i in range(N)]

mlist.sort()

for i in range(N):
    print(mlist[i])