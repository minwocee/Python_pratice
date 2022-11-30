#공강 계산기

def func_a(time_table):
    answer = 0
    print(time_table) # [1, 1, 0, 0, 1, 0, 1, 0, 0, 0]
    for i, t in reversed(list(enumerate(time_table))):    #enumerate(): 인덱스번호,요소값을 튜플로 반환
        """
        [(0, 1), (1, 1), (2, 0), (3, 0), (4, 1), (5, 0), (6, 1), (7, 0), (8, 0), (9, 0)]
        으로 반환되는 리스트를 reversed 함수를 활용해 거꾸로 나타낸다
        리스트 속에 튜플 요소가 들어가 있는 형태
        이후 연산을 실행해 처음 1이 나오는 인덱스를 찾는 함수 이다.
        """
        #reversed : 0,0,0,1,0,1,0,0,1,1
        #print(i) #9,8,7,6      [6]에서 부터는 뒤에있는 0을 살펴볼 필요가 없음(마지막 수업)
        #print(t) #0,0,0,1
        if t == 1:
            answer = i
            break
    return answer

def func_b(time_table, class1, class2):       #0의 개수를 세는 함수
    
    answer = 0
    for i in range(class1, class2): #class1=0, class2=6     
        if time_table[i] == 0:
            #print(time_table[i]) # 0,0,0
            #print(i) # 2,3,5
            answer += 1
    return answer

def func_c(time_table):
    answer = 0
    for i, t in enumerate(time_table):
        #print(i) #0
        #print(t) #1
        if t == 1:
            answer = i
            break
    return answer

#def solution(time_table):
#    answer = 0
#    first_class = func_@@@(@@@)
#    last_class = func_@@@(@@@)
#    answer = func_@@@(@@@)
#    return answer
"""
func_a 는 뒤에서 부터 검색해 1이 나오는 인덱스를 알아내는 함수
func_b 는 내가 수업이 끝날때 까지 0의 개수를 세주는 함수
func_c 는 처음 수업이 시작하는 인덱스를 알아내는 함수
세가지 함수의 용도를 잘 파악하면 풀이하는데 문제 없다.
"""
def solution(time_table):
    answer = 0
    first_class = func_c(time_table)
    #print(first_class)
    last_class = func_a(time_table)
    #print(last_class)
    answer = func_b(time_table, first_class, last_class)
    
    return answer


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
time_table = [1, 1, 0, 0, 1, 0, 1, 0, 0, 0]
ret = solution(time_table)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
