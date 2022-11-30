def solution(calorie):
    answer = 0
    min = 1000
    
    for x in calorie:
#       if min > x:
#           answer += (min - x)
        """
        위와같이 min>x 이면 1000>713 이 되버리므로 문제가 바로 생기게 된다.
        다음 인덱스 항목이 현재 인덱스 항목보다 클때 우리는 연산을 실행해야 한다.
        """
        if min < x:
            answer += (x - min)
            print(answer) # 208, 459
        else:
            min = x
            print(min) # 713, 665, 500

    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
calorie = [713, 665, 873, 500, 751]
ret = solution(calorie)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
