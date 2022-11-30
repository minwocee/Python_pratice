def func_a(bundle, start): # 카드 뽑기
    print(bundle[start::2])# ccbecb, adddcb
    return bundle[start::2]

def func_b(score1, score2):
    if score1 > score2:
        return [1, score1]
    elif score2 > score1:
        return [2, score2]
    else:
        return [0, score1]

def func_c(bundle): # 점수 계산
    answer = 0
    score_per_cards = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5
    }
    for card in bundle:
        answer += score_per_cards[card]
    return answer
        
#def solution(n, bundle):
#    a_cards = func_a(@@@, @@@)[:n]
#    b_cards = func_a(@@@, @@@)[:n]
#    a_score = func_c(@@@)
#    b_score = func_c(@@@)
#    return func_b(@@@, @@@)
"""
func_a , func_b, func_c 함수가 무엇을 의미하는지 알아야 한다.
a함수는 리스트슬라이싱을 2칸씩 건너 뛰면서 잘라주고
c함수는 딕셔너리 (key:value) 형태로 key 가 들어오면? value를 answer로 더해준다
b함수는 위의 함수들을 사용하고 결과를 출력할때 사용한다.
"""

def solution(n, bundle):
    a_cards = func_a(bundle, 0)[:n]
    print(a_cards) #ccbe
    b_cards = func_a(bundle, 1)[:n]
    print(b_cards) #addd
    a_score = func_c(a_cards)
    print(a_score) #13
    b_score = func_c(b_cards)
    print(b_score) #13
    return func_b(a_score, b_score)

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n = 4
bundle = "cacdbdedccbb"
ret = solution(n, bundle)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
