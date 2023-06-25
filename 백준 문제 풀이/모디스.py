import sys

k = set(sys.stdin.readline().strip())

if ('M'in k) and ('O'in k) and('B'in k) and('I'in k) and('S'in k):
    print("YES")
else:
    print("NO")