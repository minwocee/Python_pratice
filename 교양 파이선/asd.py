size=list(range(10))

for i in range(10):
    num=int(input("치수를 입력 하시오: "))

    if num<=85:
        size.append("XS")
    elif num<=90:
        size.append("S")
    elif num<=95:
        size.append("M")
    elif num<=100:
        size.append("XL")
    else:
        size.append("XXL")
print(size.count("XS"),size.count("S"),size.count("M"),size.count("XL"),size.count("XXL"))













# for i in range(10):    #10회 반복한다.
#     id=input("새 아이디: ")
#     ps=input("새 비번: ")
    
#     if id=="성결대학교" and ps=="파이데이아1":
#         print("접속을 환영 합니다.")
#         break
    

#     print("아이디와 비번을 정확히 입력하세요")

# N=int(input("출력을 원하는 단을 인력 하시오: "))

# for i in range(1,10):
#     print(f"{N} * {i} = {N*i}", end="   ")