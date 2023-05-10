# https://www.acmicpc.net/problem/8911




# 길이는 500 까지 허용 한다. 좌표는 500 까지만 허용한다.


def table_search(N):   #N은 문자열이다. (FBLR 들어가 있음)
    # TT=[[0]*501 for qwer in range(501)]
    
    # TT[250][250]=1    #현재위치 1로 초기화

    now=[250, 250]
    # 모듈러 연산 진행  위 오른쪽 아래 왼쪽
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    현재방향=0    #북 쪽을 보고 있음

    ddx=[250]
    ddy=[250]

    for n in N:
         
        if n=='L':#왼쪽
            현재방향-=1
            현재방향%=4

        elif n=='R':#오른쪽
            현재방향+=1
            현재방향%=4

        elif n=='F':#앞
            q1, q2 = now[0]+dx[현재방향], now[1]+dy[현재방향]
            ddx.append(q1)
            ddy.append(q2)
            now=[q1,q2]

        elif n=='B':#뒤
            q1, q2 = now[0]-dx[현재방향], now[1]-dy[현재방향]
            ddx.append(q1)
            ddy.append(q2)
            now=[q1,q2]

    if len(ddx)==0 or len(ddy)==0:
        return 0
    
    X축=max(ddx)-min(ddx)
    Y축=max(ddy)-min(ddy)

    return X축*Y축    #직사각형의 넓이를 반환 한다.




import sys

T=int(sys.stdin.readline())

for _ in range(T):
    N=sys.stdin.readline().strip()     #지시표 입력받음
    print(table_search(N))



