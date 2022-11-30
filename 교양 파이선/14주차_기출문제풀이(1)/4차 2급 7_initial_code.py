
def func_a(scores1, scores2):  # 성적이 오른 학생
    answer = 0
    for score1, score2 in zip(scores1, scores2):     #zip()함수를 활용해 리스트 2개를 동시에 처리가능ㅇ
        answer = max(answer, score2 - score1)     #증가폭을 알아내는 과정
    return answer

def func_b(scores1, scores2):  # 성적이 내린 학생
    answer = 0
    for score1, score2 in zip(scores1, scores2):
        answer = min(answer, score1 - score2)    #감소폭 알아내는 과정
    return answer
            

def solution(mid_scores, final_scores):
    up = func_a(mid_scores, final_scores)
    print(up)
#   down = func_b(mid_scores, final_scores)
    """
    func_b 함수는 학생들의 점수가 떨어진 정도를 알기위해 만든 함수이다.
    따라서 감소폭값에 해당하는 매개변수의 순서를 잘 고려해서 넣어야 한다.(앞, 뒤를 바꿔 쓰면 안됨)
    """
    down = func_b(final_scores, mid_scores)
    print(down)
    answer = [up, down]
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
mid_scores = [20, 50, 40]
final_scores = [10, 50, 70]
ret = solution(mid_scores, final_scores)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
