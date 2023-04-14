for i in range(1,11,1):
    score=int(input("점수를 입력하시오 :"))
    if score >= 95 :
        print("A+")
    elif score >= 90 :
        print("A")
    elif score >= 85 :
        print("B+")
    elif score >= 80 :
        print("B")
    elif score >= 75 :
        print("C+")
    elif score >= 70 :
        print("C")
    elif score >= 65 :
        print("D+")
    elif score >= 60 :
        print("D")
    else :
        print("F")