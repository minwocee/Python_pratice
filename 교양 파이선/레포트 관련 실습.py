# def fpython():    #들여쓰기 안한 부분은 함수에 포함이 되지 않는다는 점
#     print("Python")
# print("코스프로 자격증")


# def fadd(x,y):    # 매개변수 2개를 더해서 반환해주는 fadd 함수 
#     sum=x+y
#     print("{} + {} = {}".format(x,y,sum))

# fadd(1,100)


# #과제1번 문제 소스코드
def fadd(x,y):
    sum=x+y
    #print("{} + {} = {}".format(x,y,sum))
    return sum

def fsub(x,y):
    sum=x-y
    #print("{} - {} = {}".format(x,y,sum))
    return sum

def fmult(x,y):
    sum=x*y
    #print("{} * {} = {}".format(x,y,sum))
    return sum

def fdiv(x,y):
    sum=x/y
    #print("{} / {} = {}".format(x,y,sum))
    return sum

x,y=map(int,input("연산을 원하는 두 숫자르 입력 하시오(예시: 2 4): ").split())
operate=input("연산사를 입력 하시오(예시: +,-,*,/): ")

if(operate=="+"):
    print(fadd(x,y))
if(operate=="-"):
    print(fsub(x,y))
if(operate=="*"):
    print(fmult(x,y)) 
if(operate=="/"):
    print(fdiv(x,y))




