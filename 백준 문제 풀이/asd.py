import sys


"""
13일이 금요일임을 찾는게 목적이다.
윤년의 기준 (2월달이 28일이 아닌 29일로 끝나는 해를 윤년이라고 부른다)
1. 400의 배수년도
2 100의배수가 아니면서, 4의배수인 년도
3. 400의 배수가 아니면서, 100의 배수인 연도는 윤년이 아니다.

2019/1/1 화요일 2019/1/4 금 1/11(금)
윤년이면 2번 카운트가 된다고 생각하자
"""


N= int(sys.stdin.readline())

cnt=0

# #2019년부터 비교를 시작한다

for i in range(2020, N+1,2):
    cnt+=7
    

print(cnt+2)

#2019년2개 
#2020년2개
#2021년1개


