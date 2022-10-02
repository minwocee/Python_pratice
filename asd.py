#약수의 개수를 구하고 약수를 출력해주는 프로그램을 만들자(좀 까다롭지만 유용)

while True:
    num=int(input("정수를 입력 하시오(0은 종료키): "))
    if not num:
        break    #정수가 아니면 반복문을 탈출하는듯
    if num<0:
        print("양의 정수를 입력하시오")
        continue    #다시 처음으로 돌아간다.
    count=0    #약수의 개수를 세어주는 변수를 선언 한다.
    for i in range(1,num+1):
        if num%i==0:
            print('{0:5}'.format(i),end=' ')    #앞에 4칸을 띄워줌(마지막 인덱스인 [4]에 i가 들어가고 나머지는 공백으로 채움)
            count+=1
    print()
    print("{0}의 약수의 개수: {1}개 입니다.\n".format(num,count))