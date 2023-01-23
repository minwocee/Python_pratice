# https://www.acmicpc.net/problem/4949


'''
모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다
(좌우 대칭인지 검사를 함)
print(ord('a')) #97
print(ord('z')) #122
print(ord('A')) #65
print(ord('Z')) #90

print(ord('('))    #40
print(ord(')'))    #41

print(ord('['))   # 91
print(ord(']'))    # 93
print(ord('/'))    # 92


import sys

Table= list(sys.stdin.readline().strip().split())

소괄호=0    #소괄호 카운터  ( +1  )-1 이 원리
대괄호=0    #대괄호 카운터  

real=[]

for i in Table:
    
    k=ord(i)
    if (97<=k<=122) or (65<=k<=90):   #알파벳이면 필요없음
        continue
    else:
        real.append(i)

print(real)

'''


'''
# 다른사람의 코드 분석 (이분은 stack을 사용함)
while True :
    a = input()
    stack = []    #스택임 (입구 출구가 하나)

    if a == "." :    #점 하나만 문장에 들어오면 무한 반복을 깸
        break

    for i in a :    # 문자열 a 에서 요소를 하나씩 꺼낸다.
        if i == '[' or i == '(' :
            stack.append(i)
       
        elif i == ']' :    #대괄호 닫는거면
            if len(stack) != 0 and stack[-1] == '[' :    # 스택이 비어있지 않으면서( ]만 있는거 방지), 마지막 스택 요소랑 쌍이면 쌍 제거
                stack.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
            else : 
                stack.append(']')    #닫는 대괄호 추가
                break
        
        elif i == ')' :    #소괄호 닫는거면
            if len(stack) != 0 and stack[-1] == '(' :    # 스택이 비어있지 않으면서( ]만 있는거 방지), 마지막 스택 요소랑 쌍이면 쌍 제거
                stack.pop()    # 쌍제거(스택이 비어있으면, pop연산시 오류가 나기 때문)
            else :
                stack.append(')')     # 아니면 닫는괄호를 추가한다.
                break    #반복을 깬다(내생각에는 이때 No 출력을 진행해도 결과는 같을것같다.)
    
    if len(stack) == 0 :    # 만약 스택이 비어 있으면, 균형이 맞는거임
        print('yes')
    else :    # 만약 스택이 비어 있지 않으면, ) ] 같은 불순물들이 남아있는것이므로 No를 출력한다. 
        print('no')
'''





#이런 식으로 짝이 존재하는 문제는 스택을 이용해보자

import sys


while(True):
    Table=sys.stdin.readline().rstrip()  #오른쪽 방향의 개행문자만 지워야 한다.
    
    my_stack=[]    #스택 저장 공간
    
    if Table=='.':
        exit(0)

    
    for T in Table:
        if T=='(' or T=='[':    #여는 괄호는 스택에 추가
            my_stack.append(T)
        
        
        elif T==')':
            
            # 여기서 조심해야 하는점: len(my_stack)을 먼저 해줘야 오류가 없음
            # my_stack[-1]=='(' <-- 이 식이 스택이 비어있지 않을 떄를 가정하에 이루어지기 때문
            # 같은 if문의 조건이라도 앞에서부터 우선순위가 적용이 된다는점을 인지하자
            if len(my_stack)!=0 and my_stack[-1]=='(' :   
                my_stack.pop()
            else:
                my_stack.append(T)
                break
        
        
        elif T==']':
            if len(my_stack)!=0 and my_stack[-1]=='[':
                my_stack.pop()
            else:
                my_stack.append(T)
                break
    

    if len(my_stack)==0:
        print('yes')
    else:
        print('no')

