import sys
N=int(sys.stdin.readline().strip())

Problem=sys.stdin.readline().strip()    #이미 바뀌어 버린 결과물임
Problem=list(Problem)
#원본 글자를 구하는 과정입니다 착각하지 맙시다

if len(Problem)%2==0:   #문자의 개수가 짝수일 경우 실행
    for _ in range(N):
        for i in range(int(len(Problem)/2-1),0,-1):#문자 6개면 range(2)이다
            Problem.append(Problem[2*i-1])
            del(Problem[2*i-1])
        print("1회씩 변환한 결과: ",str(Problem))    
    #[print(Problem[i],end='') for i in range(len(Problem))]
        
else:
    for _ in range(N):
        for i in range(int(len(Problem)/2),0,-1):#문자 6개면 range(2)이다
            Problem.append(Problem[2*i-1])
            del(Problem[2*i-1])
        print("1회씩 변환한 결과: ",str(Problem))     
    #[print(Problem[i],end='') for i in range(len(Problem))]


