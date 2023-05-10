#






































import sys

S=sys.stdin.readline().strip()

my_set=set()    #집합은 중복을 허용하지 않는 형태

for i in range(len(S)):
    for k in range(i,len(S)):
        word=S[i:k+1]    #리스트 스플릿
        my_set.add(word)

print(len(my_set))