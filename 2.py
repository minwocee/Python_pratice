#점수를 입력받고 출력

scorelist=[]
while True:
        print("학생들의 점수를 입력 하세요:  ")
        scorelist.append(input())
        
        if scorelist[-1]=='멈춰':
            del scorelist[-1]
            break

scorelist.sort()
print(f"최고 득점자의 점수는 {scorelist[-1]} 입니다."  )
print(f"최저 득점자의 점수는 {scorelist[0]} 입니다." )