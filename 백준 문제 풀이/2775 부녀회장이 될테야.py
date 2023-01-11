# https://www.acmicpc.net/problem/2775

import sys

Test = int(sys.stdin.readline())

for _ in range(Test):    #테스트셋 반복 횟수 
    층 = int(sys.stdin.readline())    #층수 설정
    호수 = int(sys.stdin.readline())   #호수 설정
    아파트 = [list(range(1,호수+1))]

    for _  in range(층):
        아파트.append([0]*호수)
    
    for a in range(1, 층 +1):
        for b in range(0, 호수):
            아파트[a][b]= sum(아파트[a-1][0:b+1])

    print(아파트[층][호수-1])







