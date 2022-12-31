# https://www.acmicpc.net/problem/10250

import sys

_ = int(sys.stdin.readline())
# 한번 zip 함수를 사용해볼까유

for __ in range(_):
    k='%05d' % 2   #앞자리수는 0으로 채우되, 5칸을 할당 한다. 숫자는 2를 대입 00002 출력 완료
    print(k)
    Hotel_height, Hotel_max_room, now_client = map(int, sys.stdin.readline().split())
    Table=[list(range(str)) for i in range(1,Hotel_height+1)]

    
