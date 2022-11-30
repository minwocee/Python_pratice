# 나이(정수), 이름(문자열)이 순서대로 주어짐
# 조건1 나이가 어린사람이 먼저 출력
# 조건2 나이가 같다면 먼저 입력받은 사람 순으로 출력

# 회원수 N은 100,000 개 이하
# 나이는 1~200까지의 정수
# 이름은 알파벳 대소문자로 조합, 최대 100자의 이름까지 허용





























import sys

N= int(sys.stdin.readline())
age=[]
name_list=[[]]*201
for _ in range(N):
    a, n= map(str,sys.stdin.readline().strip().split())
    age.append(int(a))
    k=list(name_list[a])
    k.append(n)
    name_list[a]=k

print(age, "나이가 담긴 리스트")
print(name_list)



