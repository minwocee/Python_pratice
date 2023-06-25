import sys

'''
T = int(sys.stdin.readline())

for _ in range(T):   #테스트케이스 개수
    
    N = int(sys.stdin.readline())     #입력한문자열개수
    mlist = [sys.stdin.readline().strip() for __ in range(N)]    #입력문자열모음리스트
    #mlist.sort(key=lambda x : len(x))    #문자열 길이를 기준으로 정렬을 실행한다.
    flag = True
    
    for k in range(N):
        now_len = len(mlist[k])    #선택한 문자열의 길이
        now_text = mlist[k]    #911, 97625999, 91125426이 선택됨
        
        for i in range(k+1, N):
            if now_len> len(mlist[i]):
                continue
            if now_text == mlist[i][0:now_len]:
                print("NO")
                flag = False
                break
        if flag == False:
            break
            
    if flag:
        print("YES")
        


'''
# 다른분의 코드

'''
t = int(input())

def check():
    for i in range(len(a)-1):
        if a[i] == a[i+1][0:len(a[i])]:
            print('NO')
            return
    print('YES')

for _ in range(t):
    n = int(input())
    a = []
    for i in range(n):
        a.append(input().strip())
    a.sort()
    check()
'''

import sys

T = int(sys.stdin.readline())

def check():
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1][0:len(arr[i])]:
            print('NO')
            return
    print('YES')
    
for _ in range(T):
    N = int(sys.stdin.readline())
    arr = [sys.stdin.readline().strip() for __ in range(N)]
    arr.sort()
    check()