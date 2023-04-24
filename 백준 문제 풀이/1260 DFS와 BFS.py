# https://www.acmicpc.net/problem/1260

import sys

# 노드, 엣지, 시작노드
N,M,V = map(int, sys.stdin.readline().split())

Field={}

for _ in range(M):
    