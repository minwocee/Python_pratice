x=int(input("짝수를 입력 하시오"))

try:
    if x%2!=0:
        raise Exception("짝수를 입력 하세요")
    if x==0:
        raise Exception("0을 입력했군요")

except Exception as e:    #as 사용해야 위의 문자열들이 정상적으로 출력된다
    print("예외가 발생했습니다", e)    #

else:
    print("잘하셨습니다. 입력한 수는 짝수 입니다.")

finally:
    print("\n프로그램을 종료 합니다")