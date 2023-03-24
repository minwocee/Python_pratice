#https://www.acmicpc.net/problem/2942


# 우선 공약수 관련 문제인것 같다. 유클리드 호제법 혹은 에라토스테네스의 체가 의심된다.

# 에라토스테네스의 체는 소수를 구하는구나 공약수가 아니
'''
4 8개로 이루어져 있다, 이들의 공약수는 1,2,4 이며 따라서 3개이다.
15 12개로 이루어져 있다, 이들의 공약수는 1,3 이며 따라서 2개이다.
42 105 의 공약수는 1.3,7,,21이며 따라서 4개가 나온다.
'''

import sys
from math import gcd
from math import sqrt
R,G=map(int,sys.stdin.readline().split())  #빨강 초록사과

최대공약수=gcd(R,G)    #최대공약수 추출 완료

# 이제 최대공약수를 기준으로 약수를 구하면 된다.

# 루트씌운걸로 크기를 줄여서 시간복잡도가 양호
now_sprt=int(sqrt(최대공약수))

ans=[]
# 이제 쌍을 구하면 끝이다. (최대공약수에서 약수를 또찾는 문제 -> 1~sqrt(최대공약수))까지만 탐색하면 된다.
for i in range(1,now_sprt+1):
    if R%i==0 and G%i==0:     #  sqrt(최대공약수) 이하에서 나누어 떨어지면~아래 실행
        
        if i==(최대공약수//i):    # R:4 G:8의 경우 1,2,2,4로 약수가 들어가는걸 방지한다.
            ans.append(i)
            continue
        
        ans.append(i)
        ans.append(최대공약수//i) #최대공약수임, now_sqrt 하면 안됨

for i in ans:
    print(i,R//i , G//i)

'''
for k in 공약수:
    print(k, R//k, G//k)
'''
# 위처럼 일일이 브루트포스 방식으로 해결하면 시간초과가 발생한다는 문제

'''
예시를 들어보겠습니다. 100의 약수는 
1,2,4,5, <10> ,20,25,50,100 이렇게 이루어 지는데, 중앙 <10>을 기준으로 왼쪽-오른쪽 쌍을 이루게 됩니다.
이때 양측을 나누는 10은 100에 루트를 씌운 10입니다.

위의 원리를 이용하여 루트씌운 중앙을 기준으로 왼쪽만 구하면 자연스럽게 오른쪽도 구할수 있으므로, 
일반적으로 풀이하는 브루트 포스 방식보다 시간복잡도가 O(N)에서 O(sprt(N))으로 감소한다는 점!!!!!
'''

# 마침 학교에서 배웠던 유클리드 호제법을 사용 해보자
# 최대 공약수를 찾고, 해당 수의 약수 집합을 구하면 될것 같다.


# 1. 유클리드호제법 사용해서 최대공약수 구함
# 2. DP 사용해서 최대공약수의 약수들을 구하면 될듯?

# 1번 유클리드 호제법 실행, 아니 그냥 GCD 쓰자


#print(최대공약수)

# 2. 최대공약수를 구했으니, 이제 약수 구하는걸 해보자
# 공약수=[]

# for i in range(1,최대공약수+1):
#     if 최대공약수%i==0:
#         공약수.append(i)