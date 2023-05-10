import sys

Table=sys.stdin.readline().strip()

if Table=='1 2 3 4 5 6 7 8':
    print('ascending')
elif Table=='8 7 6 5 4 3 2 1':
    print('descending')
else:
    print('mixed')