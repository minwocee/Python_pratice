import sys


'''
Present, X, Y, Z = map(int, sys.stdin.readline().split())
MAX_A = min(X,Y,Z)



arr = [i for i in range(0,MAX_A+1)]

# (깍두기(A) 한변의 길이)^3 <=담는통의 부피/깍두기개수 조건을 만족하는지 검사하는 함수
def check(A):
    # 이 조건을 만족하면 검토 가능한 해 이다.(최적을 보장하지는 않는다.)
    if A^3<=(X*Y*Z)/Present:
        return True
    else:
        return False


def N_check(A):
    # 몇개가 들어갈수 있는지 판단하는 함수 이게 N과 일치하면서 
    # 그리디 하게 가져가야 하는것이 목표이다.
    return Z*((X*Y)//A*A)
# middle이 check함수를 만족하고, middle+1이 check 함수를 만족하지 않는 middle이 최적값이라고 생각한다.
def binary_search():
    
'''

# 다른분의 풀이 참조 https://sophuu.tistory.com/50
'''
import sys

# 개수, 통가로, 통세로, 통높이
N, L, W, H = map(int, sys.stdin.readline().split())

# 시작, 끝
# 나는 min값을 끝으로 두었는데 이분은 max를 끝값으로 두었다. 이게 확실하기는 하지
# 아무리 커도 max값을 넘지는 않을것이니 
S, E = 0, max(L, W, H)


# 특정 조건을 만족할때 끝내는 이분탐색이 아닌, 10000번 정도면 찾겠지 하는 마인드로 반복문을 돌리는 경우 이다.
# 수렴할때 까지 반복을 진행한다는 말
for _ in range(10000):
    M = (S + E) / 2    #중간값
    # 들어갈수 있는 정사각형의 개수를 의미하는 count
    count = (L // M) * (W // M) * (H // M)
    
    # 한변의 길이를 M으로 둘때 만들어 지는 정사각형의 개수(count)가 
    # 찾고자 하는 N보다 크면 좀더 M의 길이를 늘리는 방향으로 해야 함
    
    # 한변의 길이를 M으로 둘때 만들어 지는 정사각형의 개수(count)가 
    # 찾고자 하는 N보다 작으면 M의 길이를 줄여서 더 많이 담아야 한다.
    
    # 아래의 조건문은 늘렸다, 줄였다 핑앤 퐁을 반복하면서 최적의 값을 찾는 과정 이다.
    # 이래서 소수점이 나왔던 것이였구나...
    if count >= N:
        S = M
    else:
        E = M


# 상한 오차가 10^-9 까지 허용한다는게 무슨 말인지는 잘 모르겠는데
# 일단은 소수점 아래 9자리 숫자까지 허용해보자
print("%.9f" %(E))



'''
# 다시한번 풀어보자

import sys
N,X,Y,Z = map(int, sys.stdin.readline().split())


cnt = 0

start = 0
end = max(X,Y,Z)

while(cnt<100000):
    middle = (start + end) / 2
    now_N = (X//middle)*(Y//middle)*(Z//middle)
    
    # 이렇게 시작을 떙겨오면 now_N이 작아질 확률이 증가함(큼직큼직하게 A를 잡음)
    if now_N>= N:
        start = middle
    else:
        # 이렇게 끝을 땡겨오면 now_N이 커질 확률이 증가함(조금조금 A를 잡음)
        end = middle
    
    cnt+=1
    
print("%.9f" % middle )