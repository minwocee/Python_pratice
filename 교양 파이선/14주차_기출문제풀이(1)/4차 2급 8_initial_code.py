
def solution(n, votes):
    answer = 0
    votes_len = len(votes)
    candidate = votes[0]
    
    count = 1
    for i in range (1, votes_len) :     #몇 표를 얻었는가 확인하는 과정
        if candidate == votes[i] :
            #print(candidate) # 2
            count += 1
        else :
            count -= 1
        if count == 0 :
            candidate = votes[i]
            #print(candidate) # 첫번째 루프 2,1,3,1,2,1 두번째 루프 1,2,1,2
            count = 1

    test_count = 0
    for i in range(0, votes_len) :
        if votes[i] == candidate :
            #print(votes[i]) # 첫번째 루프 1,1,1,1 두번째 루프 2,2,2,2
            test_count += 1
            #print(test_count) # 1,2,3,4

#   if test_count < votes_len // 2 :    """고쳐야하는 부분"""
    """
    과반수를 "넘어야지" 해당 선거인이 당선되는구조
    test_count가 과반수(투표자수/2) 보다 커야지 당선이므로 부등호의 방향을 수정해야 한다.
    """
    if test_count > votes_len // 2 :
        answer = candidate
    else :
        answer = -1
        
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
n1 = 3
votes1 = [1, 2, 1, 3, 1, 2, 1]
ret1 = solution(n1, votes1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

n2 = 2
votes2 = [2, 1, 2, 1, 2, 2, 1]
ret2 = solution(n2, votes2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")
