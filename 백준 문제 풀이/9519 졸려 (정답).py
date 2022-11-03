def even(Problem):    #리스트가 들어가는 매개변수임(짝수일때)
    counter=0 
    while(True):
    #if len(Problem)%2==0:   #문자의 개수가 짝수일 경우 실행
        for i in range(int(len(Problem)/2-1),0,-1):#문자 6개면 range(2)이다
            Problem.append(Problem[2*i-1])
            del(Problem[2*i-1])
        counter+=1    
        
        if Problem==answer:
            break
    return counter    #주기를 반환함


def odd(Problem):    #리스트가 들어가는 매개변수임(짝수일때)
    counter=0 
    while(True):
    #if len(Problem)%2==0:   #문자의 개수가 짝수일 경우 실행
        for i in range(int(len(Problem)/2),0,-1):#문자 6개면 range(2)이다
            Problem.append(Problem[2*i-1])
            del(Problem[2*i-1])
        counter+=1    
        
        if Problem==answer:
            break
    return counter    #주기를 반환함



#***************************************************************************************************************


import sys
N=int(sys.stdin.readline().strip())
Problem=sys.stdin.readline().strip()    #이미 바뀌어 버린 결과물임
Problem=list(Problem)
answer=list(Problem)
#원본 글자를 구하는 과정입니다 착각하지 맙시다
#scama
if len(Problem)%2==0:
    sum=N%even(Problem)    #입력 횟수와 주기를 나머지 연산함
    for _ in range(sum):
        for i in range(int(len(Problem)/2-1),0,-1):#문자 6개면 range(2)이다
            Problem.append(Problem[2*i-1])
            del(Problem[2*i-1])
    [print(Problem[_],end='') for _ in range(len(Problem))]

else:
    sum=N%odd(Problem)
    for _ in range(sum):
        for i in range(int(len(Problem)/2),0,-1):#문자 6개면 range(2)이다
            Problem.append(Problem[2*i-1])
            del(Problem[2*i-1])
    [print(Problem[_],end='') for _ in range(len(Problem))]