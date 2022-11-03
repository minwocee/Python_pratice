import sys

N=int(sys.stdin.readline().strip())

Problem=sys.stdin.readline().strip()

#원본 글자를 구하는 과정입니다 착각하지 맙시다

#만약 Problem의 문자개수가 짝수인 경우는?(가운데 두개는 뒤로 보내고 나머지 양끝에서 하나씩 짝지어줌)
mstr=[]
for _ in range(N+1):
    if len(Problem)%2==0:
        for i in range(int(len(Problem)/2-1)):    #acefdb 를 기준으로 해보면 2번만 
            mstr.append(Problem[i])
            mstr.append(Problem[-(i+1)])
            
        mstr.append(Problem[int(len(Problem)/2-1)])
        mstr.append(Problem[int(len(Problem)/2)])
        Problem=(mstr)
        mstr=[]
    else:
        for i in range(int(len(Problem)/2)):    #acefdb 를 기준으로 해보면 2번만 
            mstr.append(Problem[i])
            mstr.append(Problem[-(i+1)])
            
        mstr.append(Problem[int(len(Problem)/2)])
        Problem=(mstr)
        mstr=[]


[print(Problem[i],end="") for i in range(len(Problem))]



#뒤에서 k번째 글자는 앞에서부터 k번째와 k+1번째 글자 사이로 이동한다.