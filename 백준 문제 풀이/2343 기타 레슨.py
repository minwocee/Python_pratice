# https://www.acmicpc.net/problem/2343


# 잘 만났다. 최근에 배운 이분탐색으로 해결해보자



'''
9 3    # 9곡을 3파트로 나누고 싶다는말
1 2 3 4 5 6 7 8 9    # 각 강의의 길이
'''


# 이분 탐색을 그럼 어떻게 쓸까가 고민이군

'''
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

'''

#내가 단번에 풀지 못한 이유
'''
start, end, middle 을 무엇으로 둘지 감을 못잡음(이 문제 같은 경우는 Table에서 start=max(Table), end=sum(Table))
이렇게 잡았다. 이분 탐색에서 가장 중요한건 S E M 이렇게 3개를 어떻게 잡느냐가 핵심인것 같다.
'''

'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())#곡개수, 블루레이개수
video = list(map(int, input().split()))#각각의 노래의 러닝타임

vm = max(video)
start = vm
end = sum(video)

res = 10**9
while(start <= end):
    mid = (start+end)//2
    cnt = 1    #현재 블루레이 담는개수
    tmp = 0


    for i in range(n):    # 0~ 노래개수-1 까지 대입 시작

        if(tmp+video[i] <= mid):    # 만약 현재 블루레이에 비디오를 더 넣을 수 있다면
            tmp += video[i]
        else:
            cnt += 1
            tmp = video[i]
        if(cnt > m):
            break



    if(cnt > m):    # 만약 블루레이의 개수보다 더 많이 나눠 담으면, 좀더 큰 뭉텅이로 담기시작
        start = mid+1
    else:    # 만약 블루레이의 개수기준보다 작게채우거나, 같으면 실행
        end = mid-1    # 좀더 촘촘하게 채워 본다.
        if(mid >= vm):    # 만약 중앙값이 리스트의 최대값보다 크면
            res = min(res, mid)    # 

print(res)
'''



import sys

곡_개수, 블루레이_개수 = map(int, sys.stdin.readline().split())    # 곡개수, 블루레이_개수
곡_Table=list(map(int, sys.stdin.readline().split()))    # 곡의 러닝타임

# 9 2 7 3 4 (5곡이 존재)

# 9 S, 25 E, 17 M

#곡_Table의 정렬을 하지는 않는다.(노래의 순서를 유지 해야 하기 때문이다.)
start=max(곡_Table)    #가장 큰 곡이 짤리지 않게 하기 위해서
end=sum(곡_Table)
king=10000000000    #나중에 결과값 비교할때 쓴다

while(start<=end):
    middle=(start+end)//2    #최대값-총합의 평균
    현재담는블루레이트랙번호=1    #1번트랙에 노래를 담기 시작함
    현재블루레이_용량=0

    for i in range(곡_개수):# 0~ 곡개수-1 (모든인덱스 탐색)
        if(현재블루레이_용량+곡_Table[i]<=middle):#최대값-총합의 평균보다 작으면 가용주머니에 담는다
            현재블루레이_용량+=곡_Table[i]
        else:#담는 블루레이용량이 평균을 초과 한 경우
            현재담는블루레이트랙번호+=1#다음트랙으로 점프
            현재블루레이_용량=곡_Table[i]#다음트랙으로 담기 시작
        
        if(현재담는블루레이트랙번호>블루레이_개수):#블루레이의 개수보다 더 많이 담으려한다(간단히 말해 담아야 하는 곡들이 다 담기지 못하는 경우)
            break


    if(현재담는블루레이트랙번호>블루레이_개수):#블루레이의 개수보다 더 많이 담으려한다(간단히 말해 담아야 하는 곡들이 다 담기지 못하는 경우)
        #좀더 많이씩 담아야 하지
        start=middle+1

    else:
        end=middle-1
        if(middle>=max(곡_Table)):#중앙값이 리스트최대값보다 크면
            king=min(king,middle)

print(king)


# 문제를 풀고나서 참고한 정리 잘된 블로그
# https://deok2kim.tistory.com/109
'''
블루레이의 수용 가능한 용량에 따라서 블루레이의 개수가 나뉘는데, 
이를 이분탐색을 활용하여 원하는 블루레이 개수-->블루레이 용량 이렇게 찾는다고 생각하면 편하다

이분탐색은 뭘 찾을건가를 핵심으로 두고 생각하는게 좋다.
'''







