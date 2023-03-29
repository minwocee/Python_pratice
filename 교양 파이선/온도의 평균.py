import sys

day=list(map(float, sys.stdin.readline().strip().split()))


print("온도의 평균", sum(day)/len(day))