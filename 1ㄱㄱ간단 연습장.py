#if문 활용예제
k=int(input("1부터 100사이의 정수를 입력 하시오: "))

if k<100:
    print("입력한 정수가 100보다 작음")
    print(f"a = {k}")

if k>=100:
    print("프로그램 종료") 

#예제 4-2 if-else 활용

k=int(input("1부터 100사이의 정수를 입력 하시오: "))

if k<100:
    print(f"입력한 a의 값은 {k}이며 100보다 작음")
    print("프로그램 종료") 
else:
     print(f"입력한 a의 값은 {k}이며 100보다 크다")
     print("프로그램 종료") 


#중복 if-else문 활용
k=int(input("1부터 100사이의 정수를 입력 하시오: "))
if k>=0:
    if k==0:
        print("입력한 정수는 0임")
    else:
        print("입력한 정수는 %d이고 양수임"%k)
else:
    print("입력한 정수는 %d이고 음수임"%k)

#나이와 점수에 따라 합/불을 정하는 프로그램
age, score=map(int,input().split())

if age>20:
    if score>80:
        print("합격입니다")
    else:
        print("점수가 너무 낮아 불합격 입니다.")
else:
    print("나이가 너무 어려서 불합격 입니다.")