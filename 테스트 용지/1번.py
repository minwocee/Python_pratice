import sys

N= int(sys.stdin.readline())



Table = [sys.stdin.readline().strip() for __ in range(N)]

#print(Table)

for i in Table:    # i가 테이블 요소 1개이다.
    i2=i[::-1]

    if i2 in Table:
        print(len(i2), i2[len(i2)//2])
        break