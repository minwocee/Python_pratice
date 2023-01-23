# https://www.acmicpc.net/problem/2343


# 잘 만났다. 최근에 배운 이분탐색으로 해결해보자



'''
9 3    # 9곡을 3파트로 나누고 싶다는말
1 2 3 4 5 6 7 8 9    # 각 강의의 길이
'''

# 이분 탐색을 그럼 어떻게 쓸까가 고민이군

import sys

곡, 파트 = map(int, sys.stdin.readline().split())

Table=list(map(int,sys.stdin.readline().split()))


start=1#시작
end=max(Table)#끝

while (start<=end):
    middle=(start+end)//2

    if middle<파트:
        start=middle+1
    else:
        end=middle-1

print(middle)




