# 4개의 함수를 생성 하고 진행을 해보자 산술평균, 중앙값(반드시 홀수 임), 최빈값구하기, 범위 출력하기
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 










#산술평균 구하기(소수점 아래 첫번째에서 반올림 실행해서 정수로만 표현)
def my_average(my_list):
    if len(my_list)<=1:    #만약 변량이 1개인 경우 산술평균은 그냥 변량 1개임
        return my_list[0]
    else:
        return round(sum(my_list)/len(my_list))

#중앙값 구하기
def my_middle(my_list):    
    if len(my_list)<=1:    #만약 변량이 1개인 경우 중앙값은 그냥 변량 1개임
        return my_list[0]
    else:
        return my_list [ round (len(my_list)/2) ]

#최반값 구하기(단, 최빈값이 여러개 존재하면 가장 작은것에서 2번째를 구함)
def my_popular(my_list):
    if len(my_list)<=1:    #만약 변량이 1개인 경우 최빈값은 그냥 변량 1개임
        return my_list[0]
    else:    #여기서 부터가 진짜 문제임 1번: 최빈값이 하나만 나오는 경우 2번: 최빈값이 2개 이상일때
        #침고로 count 함수를 쓰면 시간 초과가 뜨기 때문에 본인이 직접 최빈값을 구하는 코드를 구현해야함
        # 최빈값을 구하는 과정, 이후 2개이상의 최빈값이 존재하면 찾아서 2번째것을 출력한다
        
        top=0    #현재 가장 큰값
        my_counter=1    #카운터
        for i in range(len(my_list)-1):
            if my_list[i]==my_list[i+1]:    #만약 현재와 다음것이 같다면
                my_counter+=1    #중첩개수를 세는 카운터를 1개 증가 시킨뒤
                top=max(top,my_counter)    #임시 최빈값을 갱신한다
            elif my_list[i]!=my_list[i+1]:    #만약 현재와 다음것이 다르다면
                top=max(top,my_counter)    #임시 최빈값을 갱신한다
                my_counter=1    #그리고 카운터를 초기화한다
        #print(top,"현재 최빈값의 절대값 입니다(나중에 삭제 하세요~)")
        #그럼 현재 top에는 최빈값이 찍히는데 이게 과연 단일 개수의 최빈값인지 중복이되는 최빈값인지 모른다
        #그렇다면 이제 단일개수 최빈값, 중복 개수 최빈값인지 검사를 실행하고 2번째것을 찾으면 된다.
        
        multy_top=0    
        your_counter=1
        final_round=[]    #최빈값이 들어가는 리스트

        for i in range(len(my_list)-1):    #똑같이 검사를 실행
            if my_list[i]==my_list[i+1]:
                your_counter+=1
                multy_top=max(multy_top,your_counter)
                
            elif my_list[i]!=my_list[i+1]:
                multy_top=max(multy_top,your_counter)
                
                if top==multy_top:
                    final_round.append(my_list[i])
                your_counter=1

    
        if len(final_round)<=1:
            return final_round
        else:
            return final_round




#범위를 구하기
def my_range(my_list):
    if len(my_list)<=1:    #변량이 1개 밖에 없으면 범위는 0이 되는 경ㅇ루
        return 0    
    else:
        return (my_list[-1]-my_list[0])    #가장 큰값에서 가장 작은값을 빼줌
    


#****************************************** MAIN 함수 시작 *********************************************************************


import sys

N=int(sys.stdin.readline().strip())    #입력받는 변량의 개수를 의미

my_list=[int(sys.stdin.readline().strip()) for i in range(N)]    #리스트에 변량의 삽입을 완료함

my_list.sort()    # 변량들을 오름차순 정렬을 완료함

#print("결과값 출력 시작 (나중에 삭제 해야 함)")

#산술평균 출력
print(my_average(my_list))

#중앙값 출력
print(my_middle(my_list))

#최빈값 출력
print(my_popular(my_list))

#범위 출력
print(my_range(my_list))
















