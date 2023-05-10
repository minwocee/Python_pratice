# https://www.acmicpc.net/problem/3020

'''
N: 동굴의 길이(장애물의 개수)  (2 ≤ N ≤ 200,000) -> 항상 짝수임
H: 동굴의 천장 높이 세로 (2 ≤ H ≤ 500,000)
'''

# 목적은 가장 적게 장애물을 파괴하는것 ,

# 결과: 8개를 파괴한다 3번 구간으로 갔을때 


'''
6 7
1
5
3
3
5
1

결과 
2(최소장애물) 3(가능한 구간 개수)
'''


'''
# 우선 시간복잡도를 고려하지 않고 내 방식대로 풀어보자
import sys

N,H = map(int, sys.stdin.readline().split())    # 장애물 개수, 동굴의 높이 입력 받음


Cave=[int(sys.stdin.readline())*10 for _ in range(N)]

#print(Cave)# [1, 5, 3, 3, 5, 1]

ans=[]

for gugan in range(5,H*10,10):
    G_cnt=0
    #print('현재 높이 입니다: ',gugan)
    for i in range(N):
        # 짝수번 인덱스인 경우 (아래에 설치됨)
        if i%2==0:
            if 0<gugan<Cave[i]:    # 부딫히면 카운터 증가
                G_cnt+=1
                
        # 홀수번 인덱스인 경우 (위에 설치됨)
        elif i%2!=0:
            if H*10>gugan>(H*10-Cave[i]):    # 부딫히면 카운터 증가
                G_cnt+=1
        
    ans.append(G_cnt)
        
small=min(ans)
print(small, ans.count(small))
'''
# 위의 코드는 답은 나오지만 시간복잡도가 터짐 

# 시간복잡도를 줄이는 방법
# 1. 이분탐색
# 2. 누적합(프리픽스)

'''
간단히 말해서 0,5까지의 높이가 있는 동굴이 있다고 치면
1,3,5,2,4가 있다고 쳐보자

그렇다면 
1구간: 5
2구간: 4
3구간: 3
4구간: 2
5구간: 1

이렇게 되는데 (일반적으로 생각하는 기준)
누적합 방식으로 생각하면
5구간에만 부딫히는 개수: 1
4구간에만 부딫히는 개수: 1
3구간에만 부딫히는 개수: 1
2구간에만 부딫히는 개수: 1
1구간에만 부딫히는 개수: 1

5구간: 5구간에만 부딫히는 개수 = 1
4구간: 5구간에만 부딫히는 개수 + 4구간에만 부딫히는 개수= 1+1 = 2
3구간: 4구간에만 부딫히는 개수 + 3구간에만 부딫히는 개수= 1+2 = 3
2구간: 3구간에만 부딫히는 개수 + 2구간에만 부딫히는 개수= 1+3 = 4
1구간: 2구간에만 부딫히는 개수 + 1구간에만 부딫히는 개수= 1+4 = 5

이런 원리로 적용이 된다.
'''

# 위의 개념을 토대로 다시 한번 해보자

import sys

N,H=map(int,sys.stdin.readline().split())

cnt=0
down=[]
up=[]
for _ in range(N):
    if cnt%2==0:
        down.append(int(sys.stdin.readline()))
    else:
        up.append(int(sys.stdin.readline()))
        
    cnt+=1
    
# 정상적으로 업 다운 실행 완료
preview=[0]*(H+1)

# 누적합 연산 결과를 담을때 쓸것임
ans=[0]*(H+1)

# down 부터 살펴본다.

for i in down:
    preview[i]+=1
    
print(preview,'down 파트 누적합 전')

# 0 1 0 1 0 1 0 0    (각 요소들의 결과)
# 0 3 2 2 1 1 0 0    (누적합 결과)

cn=0
for _ in range(len(ans)-1,0,-1):
    cn+=preview[_]
    ans[_]+=cn

# 누적합 완료 print(ans)
print(ans,'down 파트 누적합 완료')

# up의 경우 계산을 실시한다.(위에 붙어있다는걸 인지해야함, 빼주고 +1)

preview=[0]*(H+1)

for i in up:
    preview[H-i+1]+=1

print(preview, "up파트 누적합 전")    #[0, 1, 0, 1, 0, 1, 0, 0] up파트

cn=0
#ans1=[0]*(H+1)
for _ in range(len(ans)):
    cn+=preview[_]
    ans[_]+=cn

print(ans, 'up 파트 누적합 완료 + down 파트 누적합의 결과물')

ans.remove(0)

# 결과 출력
print(min(ans), ans.count(min(ans)))
    
