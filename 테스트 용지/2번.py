import sys

N=int(sys.stdin.readline())

Table = list(map(int ,sys.stdin.readline().split()))

Table.sort()
Table.reverse()


if len(Table)==1:
    print(1)
    exit(0)
#print(Table)

for i in Table:
    cnt =0
    for _ in Table:
        if i<= _:
            cnt+=1

    if cnt>=i:
        print(i)
        break
