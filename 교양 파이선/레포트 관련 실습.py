aa=[]

for i in range(5):
    aa.append(0)

hap=0
for i in range(5):
    aa[i]=int(input(str(i+1)+"번째 숫자: "))

print("입력한 수의 합:",sum(aa))

mlist=[1,2,3]

mlist[1:3]=[100,200]

print (mlist)
mlist=[i for i in range(10)]
print(mlist)

Size_counter=[0 for _ in range(6)]     #사이즈 카운터 리스트를 만든뒤 0을 6번 넣어줌

print(Size_counter)


# 코스프로 기출문제 1
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(shirt_size):
	answer = []    #정답 리스트를 생성한다.
	answer.append(shirt_size.count("XS"))     #각 사이즈 별로 개수를 세어주고 정답 리스트에 넣어준다.
	answer.append(shirt_size.count("S"))
	answer.append(shirt_size.count("M"))
	answer.append(shirt_size.count("L"))
	answer.append(shirt_size.count("XL"))
	answer.append(shirt_size.count("XXL"))
	return answer    #결과 리스트를 통째로 반환해줌


shirt_size = ["XS", "S", "L", "L", "XL", "S"]    #사용자들이 본인 사이즈를 적고간 리스트 생성
ret = solution(shirt_size)

print("solution 함수의 반환 값은", ret, "입니다.")


#집가기전에 푼 문제
import math

def solution(people):
    answer=[0 for _ in range(4)]    #4칸 확보해줌
    #코딩 시작
    for i in range(5):
        if people[i]<95:
            answer[0]+=1

        elif people[i]>=95 and people[i]<100:
            answer[1]+=1
        
        elif people[i]>=100 and people[i]<105:
            answer[2]+=1
        
        elif people[i]>=105 :
            answer[3]+=1
    return answer    #4칸의 리스트를 반환 함


people=[97,102,93,100,107]

ret=solution(people)

print("solution 함수의 반환 값은",ret,"입니다.")


















