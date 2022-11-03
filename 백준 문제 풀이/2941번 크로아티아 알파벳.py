# 문자열에서 특정 콤보를 만족하면 1개를 세어준다고 생각








#다른 방법 문자열의 총 개수에서 컴보를 만족하며 1개씩 줄어들게하는 방법도존재 (이따 해보자)

#혹은 콤보를 만족하면 문자열 스플릿이 가능한지도









#이건 좀 무식한 방법중 하나임

# def find_croatia_alpabet_forlist (input_str):    #크로아티아 알파벳 조건을 찾는 함수
#     count=len(input_str)
#     count-=input_str.count("c=")
#     count-=input_str.count("c-")
#     count-=input_str.count("dz=")
#     count-=input_str.count("d-")
#     count-=input_str.count("lj")
#     count-=input_str.count("nj")
#     count-=input_str.count("s=")
#     count-=input_str.count("z=")

#     return count



# import sys

# N=sys.stdin.readline().strip()

# print(find_croatia_alpabet_forlist(list(N)))

import sys

croatia_alpabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
mystr=sys.stdin.readline().strip()    #글자를 입력 받음

for i in croatia_alpabet:
    mystr = mystr.replace(i, '*')  #'c='가 존재하는 모든 문자를replace를 활용해 전부 바꿔버린다
    #replace는 모든 문자열을 교체하는데 사용이 가능하다는 점을 인지


print(len(mystr))










