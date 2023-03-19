# https://www.acmicpc.net/problem/2621

# 빨R 파B 노Y 초G 4가지 색
# 1~9까지 9장
# 총 9*4 = 36개의 색 존재

'''
5장 색 같고, 오름차순 일때(가중치 1): 가장큰 숫자 +900 점수임

5장중 4개의 숫자 같음: 같은숫자 + 800


반례 목록들
반례1
Y 4
Y 3
Y 2
Y 5
Y 6
답 906


반례2
B 3
R 3
B 7
Y 3
G 3
답 803

반례3
R 5
Y 5
G 7
B 5
Y 7
답 757


반례4
Y 3
Y 4
Y 8
Y 6
Y 7
답 608


반례5
R 7
R 8
G 9
Y 6
B 5
답 509


반례6
R 7
Y 7
R 2
G 7
R 5
답 407


반례7
R 5
Y 5
Y 4
G 9
B 4
답 354


반례 8
R 5
Y 2
B 5
B 3
G 4
답 205


반례 9
R 1
R 2
B 4
B 8
G 5
답 108

반례 10
B 3
B 7
R 1
B 2
Y 7
답 207


'''

# 무수히 많은 elif문의 요청이?

import sys

Field=[tuple(sys.stdin.readline().strip().split()) for _ in range(5)]


# 색깔 담아둔 리스트
color_list=[Field[0][0],Field[1][0],Field[2][0],Field[3][0],Field[4][0]]

# 숫자 int로 반환해서 담아둔 리스트
num_list=[int(Field[0][1]),int(Field[1][1]),int(Field[2][1]),int(Field[3][1]),int(Field[4][1])]



# 5장중 색같고, 오름차순일때 경우 가장큰 숫자 +900이 존재 하는지
if Field[0][0]==Field[1][0]==Field[2][0]==Field[3][0]==Field[4][0]:
    mlist=[int(Field[0][1]),int(Field[1][1]),int(Field[2][1]),int(Field[3][1]),int(Field[4][1])]
    mlist.sort()
    
    if mlist[0]+4==mlist[1]+3==mlist[2]+2==mlist[3]+1==mlist[4]:
        print(mlist[-1]+900)
        exit(0)

# 5장중 4장이 숫자가 같을때 경우
A=list(set(num_list))
if len(A)==2:
    if (num_list.count(A[0])==4 and num_list.count(A[1])==1):
        print(A[0]+800)
        exit(0)
        
    elif (num_list.count(A[0])==1 and num_list.count(A[1])==4):
        print(A[1]+800)
        exit(0)
        
    # 5장중 3장의 숫자가 같고 나머지 2장도 같은 경우 처리
    elif (num_list.count(A[0])==2 and num_list.count(A[1])==3):
        print(A[1]*10+A[0]+700)
        exit(0)
        
    elif (num_list.count(A[0])==3 and num_list.count(A[1])==2):
        print(A[0]*10+A[1]+700)
        exit(0)
        
        
B=list(set(color_list))

# 5장의 카드가 모두 색이 같을때
if len(B)==1:
    print(max(num_list)+600)
    exit(0)
    
    
# 5장의 카드가 숫자가 연속적일때
mlist2=sorted(num_list)
if mlist2[0]+4==mlist2[1]+3==mlist2[2]+2==mlist2[3]+1==mlist2[4]:
    print(mlist2[-1]+500)
    exit(0)


from collections import Counter

# 5장중 3장의 숫자가 같을때
A=list(set(num_list))
if len(A)==3:
    K=Counter(num_list)
    King=K.most_common()   # 전체 쌍을 튜플의 형태로 반환 한다.
    
    #if 2 2 1 조합 일떄의 경우
    if King[0][1]==2 and King[1][1]==2:
        if King[0][0]>King[1][0]:
            print(King[0][0]*10 + King[1][0]+300)
            exit(0)
        elif King[0][0]<King[1][0]:
            print(King[0][0] + King[1][0]*10+300)
            exit(0)
    # if 3 1 1 조합일때의 경의
    elif King[0][1]==3:
        print(int(King[0][0])+400)
        exit(0)

if len(A)==4:
    K=Counter(num_list)
    King=K.most_common()   # 전체 쌍을 튜플의 형태로 반환 한다.
    print(King[0][0]+200)
    exit(0)
    
print(max(num_list)+100)
    

