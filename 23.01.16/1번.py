import sys

N, L, D=map(int,sys.stdin.readline().split())  #곡개수, 곡길이, 전화벨 간격

# 2 5 7

# 총 15초 길이
러닝타임=N*L + 5*(N-1)


print(러닝타임)










