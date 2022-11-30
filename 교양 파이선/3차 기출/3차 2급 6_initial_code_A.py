def solution(tile_length):
    answer = ''
    com = 'RRRGGB'
    if tile_length%6 == 1 or tile_length%6 == 2 or tile_length%6==4:
        answer=-1
        """
        com의 패턴인 RRR,GG,B를 유지하면서 이루어 져야 한다.
        이때 RRR GG  B 가 따로 떨어져서 존재를 할수는 있지만 RR R  G 는 혼자 존재할수 없기에 위의 3가지 제한
        사항들을 적어주는게 문제의 핵심이다. 
        
        """
    else:
        for i in range(tile_length):  # tile_length = 11
            answer += com[i % 6]
            #print(answer)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
tile_length1 = 11
ret1 = solution(tile_length1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

tile_length2 = 16
ret2 = solution(tile_length2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")
