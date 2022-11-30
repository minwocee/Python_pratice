def solution(day, numbers):
    count = 0
    for number in numbers:
        if number%2 == day%2:
            """
            day%2는 그날이 짝수인가 홀수인가를 구분하는 역할이다
            number%2 차량번호 또한 짝숭니가 홀수 인가를 판별하는 식이다.
            이떄 짝수차량==짝수일, 홀수차량==홀수일이여야 입장이 가능 하다는 점
            """
            count += 1
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
day = 17
numbers = [3285, 1724, 4438, 2988, 3131, 2998]
ret = solution(day, numbers)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
