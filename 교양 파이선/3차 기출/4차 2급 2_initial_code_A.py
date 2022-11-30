
def solution(scores):
	people_count = 0
	pass_score = [80, 88, 70]

	for score in scores:
		pass_count = 0
		for i in range(3):
#                       if score[i] > pass_score[i]/2:
			if score[i] < pass_score[i]/2:
				"""
				각 종목의 최저 점수를 맞추었는지 검사를 하는 부분이다.
				당연히 패스점수보다 스코어 점수가 작으면 시험에 떨어지게 된다
				"""
                                
				pass_count = 0
				break
			elif score[i] >= pass_score[i]:
                                
				pass_count += 1
		if pass_count >1:
			people_count += 1
	        
	return people_count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores1 = [[30, 40, 100], [97, 88, 95]]
ret1 = solution(scores1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

scores2 = [[90, 88, 70], [85, 90, 90], [100, 100, 70], [30, 90, 80], [40, 10, 20], [83, 88, 80]]
ret2 = solution(scores2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
