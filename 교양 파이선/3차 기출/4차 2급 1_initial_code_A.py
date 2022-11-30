def solution(schedule):
    answer = []
    for idx, i in enumerate(schedule):
        """
        해당 리스트의 자료형, 실제담긴 값을 튜플 형태로 반환하는 enumerate()함수 입니다.
        이떄 idx변수는 인덱스 번호, i변수에는 실제값이 담겨서 출력하게 됩니다.
        """
    #idx=0,1,2,3,4,5,6,7,8,9
    # i ="O", "X", "X", "O", "O", "O", "X", "O", "X", "X"
    #순서가 있는 자료형을 입력 받아 인덱스 값을 포함하는 enumerate 객체를 반환
#       if i == @@@:
#           answer.append(@@@)
        print(idx, i)
        if i == "X":
            answer.append(idx+1) # idx = 1,2,6,8,9
            
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
schedule = ["O", "X", "X", "O", "O", "O", "X", "O", "X", "X"]
ret = solution(schedule)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
