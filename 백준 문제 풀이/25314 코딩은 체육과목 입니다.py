import sys

N = int(sys.stdin.readline())

k = N//4

now = ''

for _ in range(k):
    now += 'long '
    
print(now + 'int')
    