# # https://www.acmicpc.net/problem/16508


# # 전형적인 그리디 문제 이다.
# # 가장 저렴이 부터 검토를 하는 방식을 통해 해결 가능 하다.
# # 그리디로 풀수 없는 이유: 각각의 액면가가 배수 혹은 약수 관계가 아니기 때문

# # 풀이법: 책 1권으로 해결 가능한 경우, 책 2권으로 해결 가능한 경우 , 책 3권으로 해결 가능한 경우 ... 이런식으로 조사를 실행해본다.
# # 이후 가격을 측정해서 가장 적은 비용을 선택하는 경우의 수를 선택 하면 된다.

# import sys
# from itertools import combinations

# # 타겟문자열
# Target = sys.stdin.readline().strip()

# # 책 목록
# T = int(sys.stdin.readline())
# # 책 정보가 담긴 배열
# book= []
# ans ={}
# # 몇개씩 들어있는지 조회 가능
# for _ in range(T):
#     a,b = sys.stdin.readline().strip().split()
#     book.append(b)
#     ans[b]=int(a)

# # [[35000, 'COMPUTERARCHITECTURE'], [47000, 'ALGORITHM'], [43000, 'NETWORK'], [40000, 'OPERATINGSYSTEM']]
# # print(cost_book)

# '''
# 근데 시간은 또 1초네 , 순열 방식으로 진행하면 NC1, NC2... 2^16-1의 시간복잡도 걸림 65536 가능할지도 순열 방식도?
# '''

# #print(book)
# #print(ans)

# # 이거 min값만 구하면 된다. 아무것도 없으면 -1 출력 하면 된다.
# ans_cost = []

# # 이제 각 경우의 수를 구하면 된다. 커버가 가능한지! 가능하면 ans_cost에 담으면 됨
# # 타겟을 리스트 형식으로 분리하는 과정
# Target1=set(list(Target))
# Target2 ={}
# for i in Target1:
#     Target2[i]=Target.count(i)

# # {'A': 1, 'G': 1, 'H': 1, 'L': 1, 'I': 1, 'M': 1, 'T': 1, 'Y': 1}
# # print(Target2)

# Answer = []
# for k in range(1, T+1):
#     for i in combinations(book, k):
#         king = []
#         # king에 결합을 완료
#         Answer.append(i)
# # [('COMPUTERARCHITECTURE',), ('ALGORITHM',), ('NETWORK',) 처럼 튜플 형태로 잘 들어가는지 확인 완료함
# # print(Answer)
# # 해야 하는것
# '''
# 1. 각 문자열 조합의 경우 확인하고 해당 문자열을 만들수 있으면 체크배열에 넣는다.
# 2. 체크 배열에서 가장 낮은 경우를 확인한다.
# '''

# def make_dic(text):
#     Target12=set(list(text))
#     Target23 ={}
#     for i in Target12:
#         Target23[i]=text.count(i)
#     return Target23


# realans=[]

# # 검사 실행하는 문장
# for K in Answer:
#     king = ''
#     for k2 in K:
#         king+=k2
    
#     # 현재 킹에는 합친 문자열이 저장 된다.
#     king = make_dic(king)
#     print(king, '현재 킹의 정보')
#     cnt = 0
#     for i in list(Target2.keys()):
#         # 못 만드는 경우
#         if (i not in list(Target2.keys()))  or (king[i] < Target2[i]):
#             break
#         else:
#             cnt+=1
#         # 만드는게 가능한 경우
#         if cnt == len(Target2.keys()):
#             realans.append(k)
            
# print(k,  '정답이 될수 있는 리스트들!!!!!!!!')



# 푸는법: 각 가능한 조합의 경우 수를 따져보고, 정답이 될수 있는조합을 예상 가격리스트에 넣고 가장 저렴한것을 출력 하면 된다.

def make_dic(text):
    R ={}
    for i in range(65,91):
        R[chr(i)] = 0
    
    for t in text:
        R[t] +=1
    
    return R

import sys
from itertools import combinations

Target = sys.stdin.readline().strip()
Target_dic = make_dic(Target)

T = int(sys.stdin.readline())
# 가격정보 담음
Book_dic ={}
# 책이름 담음
Book_list =[]
for _ in range(T):
    a,b = sys.stdin.readline().strip().split()
    Book_dic[b] = int(a)
    Book_list.append(b)

comb_list =[]

for i in range(1,T+1):
    for _ in combinations(Book_list, i):
        comb_list.append(_)
        
#print(comb_list)
answer =[]

for i in comb_list:
    king =''
    for i2 in i:
        king +=i2
    
    #print(king)
    #print(i)
    now = make_dic(king)
    cnt =0
    for k in range(65,91):
        if now[chr(k)] >= Target_dic[chr(k)]:
            cnt+=1
        
    if cnt == 26:
        summ=0
        for i2 in i:
            summ+=Book_dic[i2]
        answer.append(summ)
        #print(i, '가 추가 되었습니다.')

if len(answer)==0:
    print(-1)
else:
    print(min(answer))