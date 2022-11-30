#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(people):
    #여기에 코드를 작성해주세요.
    """
    우리가 항상 해오던 특정 범위 안에 들어가면 해당 인덱스를 올리는 함수이다.
    4칸의 0으로 이루어진 배열이 순서대로 S M L XL 의 카운터 숫자가 되고,
    for 문속에 4개의 if-elif 문을 넣으면 범위의 분별이 가능하다. 
    """
    answer = [0 for _ in range(4)] # [0, 0, 0, 0], ,리스트 컴프리헨션 사용


    for p in people:    #인덱스를 증가시키는 방법을 활용함
        if p < 95:
            answer[0] += 1
            print("p < 95 :",answer) # [1, 1, 1, 0]
        elif p >= 95 and p < 100:
            answer[1] += 1
            print("p >= 95 and p < 100", answer) # [0, 1, 0, 0]
        elif p >= 100 and p < 105:
            answer[2] += 1
            print("p >= 100 and p < 105",answer) # [0, 1, 1, 0][1, 1, 2, 0]
        elif p >= 105:
            answer[3] += 1
            print("p >= 105", answer) # [1, 1, 2, 1]
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
people = [97, 102, 93, 100, 107]
ret = solution(people)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
