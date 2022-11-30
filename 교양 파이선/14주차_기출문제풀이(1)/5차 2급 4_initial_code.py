def solution(taekwondo, running, shooting):
    answer = 0
    if taekwondo >= 25:    #태권도 처리 부분
#   	answer += @@@
    	answer += 250     #25회 이상 이기면 250점을 더하라고 문제에 나와 있다.
    else:
    	answer += taekwondo * 8
    answer += 250 + (60 - running) * 5     #달리기 처리 부분
    count = 0
    for s in shooting:    #사격 처리 부분
    	answer += s
    	if s == 10:
    		count += 1
    if count >= 7:
#   	answer += @@@      #7발을 전부 다 맞추면 100점이 추가된다를 적는다.
    	answer += 100
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
taekwondo = 27
running = 63
shooting = [9, 10, 8, 10, 10, 10, 7, 10, 10, 10]
ret = solution(taekwondo, running, shooting)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
