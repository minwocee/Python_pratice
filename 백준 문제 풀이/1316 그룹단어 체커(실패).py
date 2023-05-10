# 간단히 말해 앞에서 나왓던 단어가 1번 다른 글자가 나온다음에는 뒤에 또 붙으면 안된다 이말이다





















#그룹 단어를 검사는 함수를 만들어 보자
def group_word_compile (mystr):    #문자열 1개를 검사하는 함수
    mystr=mystr+"+"
    mystr=mystr+"+"
    i=0
    while(True):
        if mystr[i]!=mystr[i+1]:    #만약 연속특성이 끊기게 된다면 발생하는 이벤트
            if i!=mystr.rfind(mystr[i]):    #현재 인덱스뒤에 같은 값을 가진 인덱스가 존재한다면 틀린것
                #현재 인덱스 번호와 뒤에서 부터 찾은 요소의 인덱스 번호가 일치 하지 않는다면 그룹특성 해제
                return 0
                break
        
        if i==len(mystr)-1:
            return 1
            break
        i+=1
        
                
                

        

    
            
    









import sys

N=int(sys.stdin.readline().strip())
summ=0
for i in range(N):
    summ+=group_word_compile(sys.stdin.readline().strip())
print(summ)