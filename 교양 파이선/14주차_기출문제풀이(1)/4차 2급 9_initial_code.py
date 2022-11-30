#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(score):
    # 여기에 코드를 작성해주세요.     (동점자는 공동 2등후 다음은 4등으로 넘어감) 이건 좀 어렵네요
    answer = [1 for _ in range(len(score))]     #일단 전부다 1로 채우고 시작함. 이 부분은 우리가 직접 작성
    print(answer) # [1, 1, 1, 1, 1, 1, 1, 1]
    for i in range(len(score)):
        for j in range(len(score)):
            if score[i] < score[j]:
               answer[i] += 1 
               print(answer) # [1, 2, 2, 7, 5, 6, 8, 4], [4,2,2,1]
    """
    함수를 전부 만드는 문제이다. 조심해야 할 부분은 공동 득점자는 같은 순의를 매기고 그 다음 점수자는 2->4등으로 
    채점이 된다. 일단 처음 모든 사람의 등수를 1등으로 만들어 주고 2중 반복문을 통해 현재 나보다 큰 사람이 있다?
    그럼 1등-->2등으로 바꾸는 과정을 계속 진행하면  [1, 2, 2, 7, 5, 6, 8, 4]  로 나오는데 이때 리스트의 값이
    순위가 된다. 반복문을 2번 사용해야 하는 까다로운 문제이다. 잘 생각해서 풀자
    """
    return answer      

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
score1 = [90, 87, 87, 23, 35, 28, 12, 46]
ret1 = solution(score1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

score2 = [10, 20, 20, 30]
ret2 = solution(score2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")
