
















def winner(player_list):
    score_list=[]     #어떤 선수가 살아남았고 떨어졌는지 현황을 알려줌
    for q in range(len(player_list)):    #각 선수별 탈락자 현황을 나타내는 리스트 (1이면 생존, 0이면 패배인것, 각 선수 순서대로 적어둘 예정)
        score_list.append(1)     #일단 처음에는 전부 1로 해둠
        
    for i in range(len(player_list[0])):     #준비해온 가위바위보 경우의수의 길이
        
        key=[]    #해당 경기에서의 각 선수들의 가위바위보 결과를 종합
        lose=[]    #지게된 경우의수 1개가 들어감(이 경우의 수가 발동되면 패배)
        
        for j in range(len(player_list)):    #선수의 등번호를 의미함
            if score_list[j]==1:    # 생존자들만 결과 종합에 사용
                key.append(player_list[j][i])    #선수가 낸 가위 바위 보를 key에 넣는 과정
        #여기에서 승부를 확인

        #여기가 승패를 가르는 기준 3경우
        if ("R" in key) and ("S" in key) and ("P" not in key):
            lose.append("S")    #가위 낸사람 탈락
        elif ("R" in key) and ("S" not in key) and ("P" in key):
            lose.append("R")    #주먹 낸사람 탈락
        elif ("R" not in key) and ("S" in key) and ("P" in key):
            lose.append("P")    #보자기 낸사람 탈락
        
        if len(lose)==0:    #만약 패배경우의수 리스트가 아무도 없다면 무승무로 판별하고 다음 라운드 시작
            continue
                
        for j in range(len(player_list)):    #선수의 등번호를 의미함

            if player_list[j][i] == lose[0]:    #만약 해당 선수가 이번에 패배핸 종류를 냈으면 0으로 바꾸어 준다
                score_list[j]=0

    if score_list.count(1)>=2:
        return 0
    else:
        return score_list.index(1)+1
   
        












import sys

T=int(sys.stdin.readline().strip())     #가위바위보 몇판 할건지 출력

for _ in range(T):
    N=int(sys.stdin.readline().strip())    #참여하는 로봇선수들의 머릿수
    player_list=[]     #2차원 배열을 담을 리스트를 생성

    for __ in range(N):
        player_list.append(list(sys.stdin.readline().strip()))    #문자열이 담겨져 있는 2차원 리스트가 만들어 진다
    
    #print(player_list, "----------(2차원 리스트 생성 완료)")
    #이제 가위바위보해서 승자가 나오는지 계산함
    


    print(winner(player_list))
    

