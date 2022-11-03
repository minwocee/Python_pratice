import sys

N=int(sys.stdin.readline().strip())
numlist=list(map(int, sys.stdin.readline().strip().split()))
keynum=int(sys.stdin.readline().strip())

print(numlist.count(keynum))
