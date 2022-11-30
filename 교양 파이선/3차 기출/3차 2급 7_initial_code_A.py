
def solution(num_apple, num_carrot, k):
    answer = 0
    
    if num_apple < (num_carrot * 3):
        answer = num_apple // 3
        
    else:
        answer = num_carrot  
        print("answer는",answer) 
    num_apple -= answer * 3
    print("num_apple은",num_apple)
    num_carrot -= answer
    print("num_carrot은",num_carrot)
    
    i = 0
    k = k - (num_apple + num_carrot)
    print("k는",k)
    while k - (num_apple + num_carrot + i) > 0: 
        """
        num_apple은 위의 if-else를 거치면서 주스를 만들때 사용이 가능한 사과의 수를 의미
        num_carrot은 위의 if-else를 거치면서 주스를 만들때 사용이 가능한 당근의 수를 의미
        """
        if i % 4 == 0:
            answer = answer - 1
            print("리턴 answer는",answer) 
        i = i + 1
        k = k - 1
        
    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
num_apple1 = 5
num_carrot1 = 1
k1 = 2
ret1 = solution(num_apple1, num_carrot1, k1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

num_apple2 = 10
num_carrot2 = 5
k2 = 4
ret2 = solution(num_apple2, num_carrot2, k2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
