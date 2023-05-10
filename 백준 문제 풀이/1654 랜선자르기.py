# https://www.acmicpc.net/problem/1654

import sys

보유랜선개수, 필요랜선개수 = map(int, sys.stdin.readline().split())

"""
4 11
802
743
457
539

답: 200 길으로 잘라내면 원하는 11개의 랜선을 만들수 있다.
딱봐도 2분탐색을 이용해서 만드는 문제 같다 한본 해보자
"""
Table=[int(sys.stdin.readline()) for _ in range(보유랜선개수)]

# 이분탐색 시작
start=1
end=max(Table)

while(start<=end):
    middle=(start+end)//2
    summ=0
    for T in Table:
        summ+=T//middle
    
    #자른랜선개수 >=필요랜선의 개수
    # 1순위: 필요한 만큼 랜선의 개수를 맞추는게 중요
    # 2순위: 이왕이면 긴 랜선으로 잘라주는게 좋으므로 >= 이렇게 표현을 한것

    if summ>=필요랜선개수:    
        start=middle+1
    else:
        end=middle-1
print(end)

