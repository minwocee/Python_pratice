# https://www.acmicpc.net/problem/12018

'''
딱봐도 그리디 문제 이다.
1번: 각 과목별 수강 가능한 최저 점수를 조사후 종합 가능한 리스트를 든다.
2번: 정렬후 최대로 사용 가능한 점수를 조사 한다. (그리디 문제)
'''

'''
3가지의 경우가 필요
-경쟁이 빡세지 않다면 M>m인 경우 --> 그냥 1점 만 써도 수강 신청 확정
-경쟁률이 좀 있는 경우 M<=m인 경우 --> 위에서 부터 M등으로 우선 순위인 학생의 점수와 같으면 된다.
'''


import sys

N,point = map(int, sys.stdin.readline().split())    # 반복횟수, 내 포인트 지정


need_point=[]    # 각 과목별 필요한 점수 포인트를 종합하는 부분

# 반복 횟수 지정
for _ in range(N):
    m,M=map(int, sys.stdin.readline().split())#신청자들, 인원수 컷트
    arr=list(map(int,sys.stdin.readline().split()))
    
    if M>m:    # 인원수가 충분한 경우
        need_point.append(1)
        #print("그냥 1을 넣어줌 완료")
    else:
        arr.sort(reverse=True)
        #print(arr, '현재 입력 받고 오름차순 정렬한 상태')
        need_point.append(arr[M-1])    # 정렬후 M등의 자리를 뺏는다고 생각 한다.
        #print("넣어야 하는 점수: ", arr[M-1])

#이제 그리디 하게 가면 된다.
need_point.sort()
cnt=0
summ=0
for _ in need_point:
    cnt+=1
    summ+=_
    if point-summ<0:
        cnt-=1
        break

print(cnt)