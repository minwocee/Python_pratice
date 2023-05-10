#https://www.acmicpc.net/problem/18111


"""
작업1: 땅파기 (2초)
작업2: 땅놓기 (1초)

출력: (걸린시간(), 땅의높이(이왕이면 가장 높은쪽))

1순위: 최소시간 --> 2순위 최소시간이라는 전제하에 가능하면 높이가 높은쪽이 우선됨


1 1
1 2
(블록 제거하는게 이득인 상황, 하향 평준화가 더 빠름)
2초 높이 1


1 1
2 2
(블록 까는게 이득인 상황, 상향 평준화가 더 빠름)

2초 높이: 2


"""
'''
(없애는데 2초)
(설치하는데 1초)
제거=2설치(이왕이면 이게 좋다)


1 2 3
4 5 6
7 8 9

1 1
3 3 

1 (0),(-1),(-2),(-3),(-4),(-5),(-6),(-7),(-8)
2
3
4
5
6
7 654321(-1)(-2)
8 7654321(-1)
9 87654321 합

이렇게 모든 경우의 수를 따져야 하나 시간초과가 나지 않을까 두렵군
'''

def 최적_함수(mlist, B):    # 1 2 3 4 5 6 7 8 9
    ans=[128000001, 0]    #최악의 경우를 위해 가장 크게 해둔다.(더 시간이 작은 경우가 기존의 왕을 죽이고 왕이 됨)
    
    for i in range(min(mlist),max(mlist)+1):#리스트에서 요소 하나씩 꺼냄
        sec_count=0
        now_have=B

        for k in mlist:
            if i-k<0:#블록을 제거해야하는경우
                sec_count+=(k-i)*2
                now_have+=(k-i)
            else:#블록을 추가하는경우
                sec_count+=(i-k)            
                now_have-=(i-k)

        if now_have>=0 and ans[0]>=sec_count:    #작업을 하면서 블록이 부족한 경우가 생기지 않으면~ 가능한 경우의수 리스트에 넣어준다.
            ans=[sec_count, i]
            # 작업후블록, 걸린시간, 기준높이
    return ans   

    



import sys

N,M,B=map(int, sys.stdin.readline().split())    #세로, 가로, 이미가진블록

Table=[]

for _ in range(N):
    Table.extend(list(map(int, sys.stdin.readline().split())))


Ans_list=최적_함수(Table, B)


print(Ans_list[0], Ans_list[1])


# 높이 : [소모시간 , 필요블록, 작업중 얻은블록] 형태 
# B + make_block >=need block 이여야만 원하는 결과 얻는게 가능함
# 3번 예시가 그렇다. 설치할떄 블록이 부족한지 분석을 해주어야한다.

# min max를 기준으로 찾아야 한다ㅣ

# 이진탐색을 쓰지 못하는 이유: B(가지고 시작한 블록)가 부족한 경우에는 설치하는 방법을 못쓰고, 블록을 제거하는 방법을 사용 해야 한다.