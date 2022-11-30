#주석처리는 시험문제, 그 아래는 답
def solution(point):
	answer = 0
#	if point < 1000:
	"""
	포인트가 1000점 이상일때 사용하는 조건이라고 문제에 명시되어있으므로
	부등호의 방향을 바꿔야 한다.
	"""
	if point >= 1000:
		answer = point - point%100
	return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
point = 2323
ret = solution(point)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
