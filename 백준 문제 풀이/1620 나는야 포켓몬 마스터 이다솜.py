# https://www.acmicpc.net/problem/1620

import sys

Dogam, Quiz = map(int, sys.stdin.readline().split())    #도감의 정보와 퀴즈개수를 입력 받음

# 도감 정보 입력
Dogam_dic={sys.stdin.readline().strip():str(i) for i in range(1,Dogam+1)}


m_dic=list(Dogam_dic.items())

for pok, num in m_dic:
    Dogam_dic[num]=pok

for _ in range(Quiz):
    n=sys.stdin.readline().strip()
    print(Dogam_dic[n])
