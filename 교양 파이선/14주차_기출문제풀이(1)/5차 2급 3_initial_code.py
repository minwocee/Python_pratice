def solution(speed, cars):
    answer = 0
    """
    각 구간을 설정하는 티셔츠 문제와 비슷하게 풀면 되지만 이떄 11/10을 1.1로 바꿔주면 2진수 비트 오류가 
    발생하기 때문에 모두 정수형의 계산식을 사용해야 합니다.
    """
    for x in cars:     #실수값을 2진수로 변환할때 나오는 오류가 존재하기에 실수는 계산시 조심해야 함
        if x >= speed * 11 / 10 and x < speed * 12 / 10:      #0.9를 사용하면 2진수 계산 오차 때문에 안됨
            answer += 3                                       #파이썬만의 문법적 오류 
#       elif x >= @@@ and x < @@@:
        elif x >= speed * 12 / 10 and x < speed * 13 / 10:      #20퍼센트 ~ 30퍼센트 사이
            answer += 5
#       elif x >= @@@:
        elif x >= speed * 13 / 10:     #과속 기준의 30퍼센트 이상일시
            answer += 7
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
speed = 100
cars = [110, 98, 125, 148, 120, 112, 89]
ret = solution(speed, cars)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
