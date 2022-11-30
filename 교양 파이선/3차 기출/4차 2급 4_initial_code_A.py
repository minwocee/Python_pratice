
def solution(classes, m):
	count = 0
	"""
	학생의 수가 31명이라도 조교가 2명이 필요하다(1명이 남았기 때문)
	아래의 for문 안에 while을 사용한게 -30 -30 을 계속 해주면서 조교의 수를 세어주기 떄문이다
	"""
	for num in classes:
                
		while num > 0: # while (@@@):
                      
			num -= m  # num (@@@) m
			
			count += 1
			
	return count

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
classes = [80, 45, 33, 20]
m = 30
ret = solution(classes, m)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
