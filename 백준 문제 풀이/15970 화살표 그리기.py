# https://www.acmicpc.net/problem/15970

'''
import sys

# 구냥 한 점에서 다른 한 점 까지의 거리만 구하면 된다. 리스트 분리해서
N= int(sys.stdin.readline())

white=[]
black=[]

for _ in range(N):
    mlist=list(map(int,sys.stdin.readline().split()))

    #white 일때
    if mlist[1]==1:
        white.append(mlist[0])
    #black 일떄
    else:
        black.append(mlist[0])

# 각 배열 오름차순 정렬
white.sort()
black.sort()

# white 검사
white_cnt=0
for i in range(len(white)):
    # 극단값 처리 완려
    if i ==0:
        white_cnt+=white[1] - white[0]
    elif i==len(white)-1:
        white_cnt+=white[len(white)-1]-white[len(white)-2]
    else:
        before=white[i-1]
        tmp=white[i]
        after=white[i+1]

        if tmp-before > after-tmp:
            white_cnt+=after-tmp
        
        elif tmp-before < after-tmp:
            white_cnt+=tmp-before
        # 둘이 같은 거리인 경우
        else:
            white_cnt+=after-tmp


for i in range(len(black)):
    # 극단값 처리 완려
    if i ==0:
        white_cnt+=black[1] - black[0]
    elif i==len(black)-1:
        white_cnt+=black[len(black)-1]-black[len(black)-2]
    else:
        before=black[i-1]
        tmp=black[i]
        after=black[i+1]

        if tmp-before > after-tmp:
            white_cnt+=after-tmp
        
        elif tmp-before < after-tmp:
            white_cnt+=tmp-before
        # 둘이 같은 거리인 경우
        else:
            white_cnt+=after-tmp


print(white_cnt)
'''


# 내 생각에는 아마 색이 여러개인 경우를 고려하지 않아서 발생하는것 같다.

# 가까운 점의 개수를 세준다. (mlist는 각 점의 좌표가 오름차순으로 담겨))
def list_counter(mlist):
    mlist.sort()    # 들어온 좌표들을 정렬한다.
    cnt=0   # 반환할떄 쓸 cnt
    for i in range(len(mlist)):
        if i==0:
            cnt+=mlist[1]-mlist[0]
        elif i==len(mlist)-1:
            cnt+=mlist[-1]-mlist[-2]
        else:
            cnt+=min(mlist[i]-mlist[i-1], mlist[i+1]-mlist[i])
        
    return cnt
        
    


import sys

N=int(sys.stdin.readline())


Field=[]
for _ in range(N):
    X, col = map(int, sys.stdin.readline().split())
    Field.append([col,X])    # 색상, X 좌표 형태로 입력 한다.
    
# 입력을 마친뒤 색상별로 정렬 한다.
Field.sort()

# 색상의 개수는 Field의 마지막 리스트의 [0]과 같다

color_range=Field[-1][0]    # 색상의 개수

# 정답개수를 담는 리스트
ans_cnt=0


# 색상별로 리스트를 분리하는데 사용함
for i in range(1,color_range+1):
    same_color=[]
    
    # 한가지 색상별로 좌표를 모으기가 끝남
    for k in Field:
        if k[0]==i:
            same_color.append(k[1])
    
    ans_cnt+=list_counter(same_color)
    # 한 색상별로 모아주기 완료하였으니 이제 점수 계산을 한다.
    
print(ans_cnt)