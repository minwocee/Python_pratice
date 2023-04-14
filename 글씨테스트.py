'''
# 첫번째 문제 (for, if 문만 사용)
for i in range(1,11,1):
    score = int(input("점수를 입력하세요: "))
    
    if score>=90:
        print("합격입니다.")
        print("축하합니다.")


# 두번째 문제 (for, if-else 문만 사용)
for i in range(1,11,1):
    score = int(input("점수를 입력하세요: "))
    
    if score>=70:
        print("합격")
    else:
        print("불합격")
'''

# 세번째 문제 (for, if-elif-else 문만 사용함)
for i in range(1,11,1):
    score = int(input("점수를 입력 하세요: "))
    
    if score>=95:
        print("당신의 학점: A+")
    elif score>=90:
        print("당신의 학점: A")
    elif score>=85:
        print("당신의 학점: B+")
    elif score>=80:
        print("당신의 학점: B")
    elif score>=75:
        print("당신의 학점: C+")
    elif score>=70:
        print("당신의 학점: C")
    elif score>=65:
        print("당신의 학점: D+")
    elif score>=60:
        print("당신의 학점: D")
    else:
        print("당신의 학점: F")