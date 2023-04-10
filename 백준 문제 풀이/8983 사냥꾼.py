#https://www.acmicpc.net/problem/8983

# 시간제한 1초, 메모리 제한 128MB

# 사대의 수는  10^5개, 동물의 수는 10^5개, 사정거리는 10^9 까지 허용 (모든 좌표 값은 10^9보다 작거나 같은 양의정수)

'''
import sys

# 입력 첫줄: 사대수, 동물수, 사정거리 주어짐
M,N,L = map(int, sys.stdin.readline().split())

# 사대의 위치를 나타내는 좌표 준비
M_list = list(map(int, sys.stdin.readline().split()))

# 동물의 위치를 나타내는 좌표 준비(안의 값은 튜플로 이루어 진다.)
N_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans_dic = {}

# 동물들의 좌표를 해쉬테이블로 만들고, 나중에 True의 개수를 세줄 예정 이다.
for _ in N_list:
    ans_dic[_]=False

# 사로 1개당 죽이는 동물들의 카운터를 세준다.
for _ in M_list:
    
    # 동물들의 정보가 담긴 튜플 1개씩 꺼낸다.
    for k in N_list:
        X,Y=k[0],k[1]
        
        if ans_dic[k]!=True and Y <= L-(abs(_ - X)):
            ans_dic[k]=True
            
# 이제 정답을 출력 한다.
mt= list(ans_dic.keys())

cnt=0
for _ in mt:
    if ans_dic[_]:
        cnt+=1

print(cnt)

'''
# 위의 문제는 4번 테스크 까지만 적용이 가능함, 10^9개의 사로와 자료의 개수에선
# 시간 초과가 발생, 다른 방법을 사용 해야 한다.

# 이분탐색이 타겟값 없이 찾는 경우를 알아 이분 탐색을 써야 하는걸 알음
# 근처에 있는 애들을 탐색하는 경우를 알아 보자



import sys

# 사로 수, 동물 수, 사정거리 입력 받는다.
M,N,L = map(int, sys.stdin.readline().split())

# 사로 리스트
M_list = list(map(int, sys.stdin.readline().split()))

# 동물좌표(튜플)이 담긴 리스트
N_list = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]

# 사로 리스트 정렬을 함
M_list.sort()

# 이분탐색 시작

# 동물의 x좌표, y좌표가 1개씩 들어간다.
for a,b in N_list:
    start,end = 0, len(M_list)-1
    
    while(start<end):
        mid=(start+end)//2    
        
        if M_list[mid] == a:
            # start 값을 활용 할 것이다.(추후 중앙, 왼쪽, 오른쪽 사로 비교할때 쓸 예정)
            start = mid
            break
        elif M_list[mid] < a:
            start=mid+1
        elif M_list[mid] > a:
            end = mid -1
    
    # 이제 이분 탐색을 마침, 그럼?
    # 타겟을 찾으면? start는 a와 일치하는 해당 좌표 임
    # 타겟을 찾지 못하면? start는 a와 가장 가까운 왼쪽 좌표 임
    
    cnt=0
    # a와 사로가 일치하고, 사정거리 안에 들어온 경우
    if abs(M_list[start]-a)+b <= L:
        cnt+=1
    elif start+1 < len(M_list) and abs(M_list[start+1]-a)+b <= L:
        cnt += 1
    elif start > 0 and abs(M_list[start-1]-a)+b <= L:
        cnt += 1
print(cnt)

# 아 모르겠다 머리가 너무 아프다.