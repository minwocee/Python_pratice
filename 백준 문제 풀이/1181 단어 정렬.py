# 조건에 따라 단어를 정렬해서 출력하는 문제
# 조건1 짧은 단어가 우선순위
# 조건2 같은 길이의 단어이면 사전순(오름차순) 순으로 정렬을 하는 문제

# 단어의 개수는 N=20000 개 까지 허용함
# 단어의 허용가능 길이는 50을 넘지 않는다.

# 팁 [abc, ab ,a] 문자열 리스트를 정렬하면 [a, ab, abc] 가 된다.


























import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())
set_lst = set(lst)    #문제에서 같은 요소가 있으면 한번만 출력하라고 했기 때문이다
lst = list(set_lst)    #정렬한걸 다시 리스트로 바꿔줌
lst.sort()
lst.sort(key = len)    #이게 정말 핵심적인 키워드임 정렬의 기준을 len()이 짧은 게 앞으로 오게 정렬함

for i in lst:
    print(i)

