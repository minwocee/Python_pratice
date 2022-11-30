def solution(arr):
    answer = 0
    for i in arr:
#       for i/2 in arr:
        """
        for i/2 in arr로 사용이 불가능 합니다(아마 ValueError가 발생할것 같습니다.)
        if 조건문을 사용해서 in 키워드를 활용, 내 배열안에 해당 요소가 있는지 검사를 실행합니다.
        """
        if i/2 in arr:
            answer += 1
            
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
arr = [4, 8, 3, 6, 7]
ret = solution(arr)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
