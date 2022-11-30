# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(scores, cutline):
    # 여기에 코드를 작성해주세요.
    """
    아주 간단한 문제이다. 일점 점수를 넘으면 카운트를 세주는 문제이다. FOR 문 안에 IF 문을 사용해 
    카운팅을 진행하는 방법을 사용하면 쉽다.
    """
    answer = 0
    for s in scores:
        if s >= cutline:
            answer += 1
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores = [80, 90, 55, 60, 59]
cutline = 60
ret = solution(scores, cutline)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
