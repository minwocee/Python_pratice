# https://www.acmicpc.net/problem/2684
# 시간제한 1초, 메모리 128MB

# 단순한 투포인터 문제라고 생각 함
# 혹은 리스트 슬라이싱을 통해서도 풀수 있는 문제 라고 생각함

# 앞면: H, 뒷면: T

# 출력순서
# TTT TTH THT THH HTT HTH HHT HHH 총 8가지 경우의 수를 의미 함
# 무조건 연속임, 40C3이 38번 나타니지는 않으니

# 투포인터 기법을 통해서 풀어보자
import sys

# 테스트 케이스의 개수는 1~1000 까지 주어짐
T=int(sys.stdin.readline())

# 테스트 케이스의 개수만큼 프로그램을 실행한다.
for _ in range(T):
    # 40개의 Head, Tail 입력 받음
    Field=sys.stdin.readline().strip()
    
    # 결과물 출력할때 사용할 8개의 딕셔너리 자료구조(이 순서대로 출력 하면 됨)
    ans_dic={'TTT':0,'TTH':0,'THT':0,'THH':0,'HTT':0,'HTH':0,'HHT':0,'HHH':0,}
    
    #투포인터 탐색 시작
    start =0

    while(start !=38):
        # 3칸씩 끊어서 검사하는데 사용
        tmp = Field[start : start+3]
        
        # 해당 요소의 value값을 1 증가 한다.
        ans_dic[tmp] = ans_dic[tmp] + 1
        
        start +=1
    
    # 연산 결과물 출력
    print(ans_dic['TTT'], ans_dic['TTH'], ans_dic['THT'], ans_dic['THH'], 
          ans_dic['HTT'], ans_dic['HTH'], ans_dic['HHT'], ans_dic['HHH'])
    
