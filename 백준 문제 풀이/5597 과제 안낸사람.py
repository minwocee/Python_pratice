import sys
mlist=list(range(1,31))

[mlist.remove(int(sys.stdin.readline().strip())) for i in range(28)]

print(mlist[0])
print(mlist[1])
