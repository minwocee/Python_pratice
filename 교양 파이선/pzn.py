def pzn(x):
    return x%2

N=int(input("짝수-홀수 판별을 원하는 수를 입력 하세요: "))

if pzn(N)==0:
    print("짝수 입니다")
if pzn(N)==1:
    print("홀수 입니다.")