"""
목차
1. 클래스 선언
2. 메소드
3. 클래스 변수와 인스턴스 변수
4. self
"""


#                                        <클래스 선언>
"""
객체: 실세계에 존재하는대상    만들어진 붕어빵(클래스를 통해 만들어진 객체, 인스턴스 라고 함)
클래스: 객체를 만들기 위한 틀(template, 템플릿)    붕어빵틀
속성(attribute): 변수로 다양한 데이터형을 나타냄
행위(method): 클래스 내부의 함수
"""


#                      클래스 만드는 형식
""" <형식1>
class 클래스이름:     #속성
    변수이름1
    변수이름2
    .
    .
    .
    변수이름 N

    def 메소드이름(self: 인스턴스 자신을 의미):    #메소드(함수리고 생각)
        실행문 1
        실행문 2 
        .
        .
        .
        실행문 N
"""

"""<형식2>  #실제로 사용하려면 인스턴스를 생성해서 사용해야함
class 클래스이름:
    pass   (아무것도 없는 빈 클래스를 생성, pass 키워드 활용)
"""

"""<형식3>
class 클래스이름:
    def __init__(self, name):     #__init__: 클래스를 초기화하는 메서드 (언더바 2개는 특별함)
        self.name = name
"""

"""<형식4>
인스턴스명=클래스명()
student1 = STUDENT()    #student1이라는 인스턴스를 생성함(STUDENT클래스를 따른다)

만약 type(studen1)을 하면 
<class '__main__.STUDENT'>라고 뜬다(STUDENT클래스로부터 생성된걸 알수 있다.)
"""


#                           메소드(함수)
"""형식
class Student:
    def student_info(self, name, email, phone):   #self를 제외한 name, email, phone을 넘겨받음
        self.name = name(매개변수1)
        self.email = email(매개변수2)
        self.phone = phone(매개변수3)
        # 인스턴스화한 클래스에 이름,이메일, 휴대폰의 정보를 넣어주는 함수를 만듬
"""

# 예제 7-1 간단한 클래스 사용과 적용
class Student:
    def studnet_info(self, name, email, phone):
        self.name=name
        self.email=email
        self.phone=phone

# 인스턴스화 한다
student1=Student()

student1.studnet_info("오태식", "naver.com", "01047832349")    #속성 삽입하는 과정

print(student1.name,student1.email,student1.phone)    #오태식 naver.com 01047832349


# 7-1 __init__활용

class St__init__: 
    def __init__(self,name):    #자기자신 초기화 할때(반드시 매개변수가 있어야지 된다.)
        self.name = name

student2= St__init__("홍길동")    #따로 St__init__.__init__("홍길동") 이라고 적지 않아도 됨(__init__)
student3= St__init__("김철수")

print(student2.name, "2번학생의 이름을출력")    #홍길동 2번학생의 이름을출력
print(student3.name, "3번학생의 이름을출력")

print(type(student2.name), "2번학생의 name의 타입을출력")    #<class 'str'> 2번학생의 name의 타입을출력
print(type(student2.name), "2번학생의 name의 타입을출력")



# 예제 7-3
class _student:
    def __init__(self, name, email, phone):    # 클래스 속성에 값 초기화 하는 부분(생성과 동시에 소멸)
        self.name= name
        self.email= email
        self.phone= phone

    def to_print(self):
        return "{}\t{}\t{}".format(    #출력을 위한 문자열을 반환하는 함수
            self.name, self.email, self.phone
        )


student_list=[    #클래스 변수가 담긴 리스트를 만들어준다
    _student("홍길동","qwer@naver.com","01048967894"),
    _student("김철수","asdf@naver.com","0101234654"),
    _student("홍길동이","qweruiop@naver.com","01065132548"),
    _student("김철수이","asdflkhj@naver.com","01098765434")
]

print("이름", "email", "phone", sep="\t\t")    #3단어를 탭 2번씩 두어서 구분 하겠다
print("-"*50)

for _ in student_list:    #리스트속에담긴 클래스 변수들을 출력하는 과정
    print(_.to_print())





#    메소드
"""
생성자(constructor) 메소드:  __init__
생성과 동시에 속성값을 초기화

소멸자(destructor) 메소드:  __del__
객체를 사용후 소멸시키고자 할 때 사용

__repr__() 메소드:
인스턴스 자체를 print() 문으로 출력시 사용한다

비교 메소드:
__lt__(), __le__(), __gt__(), __ge__(), __eq__(),__ne__() 등으로 비교 연산자(<, <=, >, >=, ==, !=)이용하여
인스턴스 간의 크기를 비교할 때 사용
"""
print("-"*30)
# 예제 7-4 
class Pythonschool:
    def __init__(self,name,email,phone):
        self.name=name
        self.email=email
        self.phone=phone

    def printstudent(self):
        print("이름: ", self.name)
        print("이메일: ", self.email)
        print("전화번호: ", self.phone)
    
    def __del__(self):
        print(self.name, "객체가 소멸되었습니다.")

    def __repr__(self):    #인스턴스 자체의 이름을 출력시 사용함
        return self.name    ##<__main__.Pythonschool object at 0x0000026D693ABA30> 안쓰면 이거 뜸

my_student1=Pythonschool("홍길동이", "ㅁㄴㅇㄹ@naver.com", "010-1234-5678")
my_student1.printstudent()     #클래스 내에서 활용하는함수들이 같이 들어 있다고 생각
print(my_student1)    #클래스 자체를 프린트 하는 경우 __repr__(self)에서 지정한 return값이 반환됨
#여기서는 self.name인 홍길동이가 출력 된다
del my_student1    #출력하고 클래스 인스턴스 사라짐



#예제 7-7   클래스메소드에서 비교연산자역할을 하는 메소드 모음집(BOOLean 형태로 반환함)

class m_student:
    def __init__(self, name, age):   #초기화
        self.name = name
        self.age = age
    
    def __eq__(self, other):   #이퀄
        return self.name == other.name
    
    def __ne__(self, other):    #낫이퀄
        return self.name != other.name

    def __gt__(self, other):    #greater than
        return self.name > other.name
    
    def __ge__(self, other):    #greater equal than
        return self.name >= other.name
    
    def __lt__(self, other):   #lessthan
        return self.name < other.name
    
    def __le__(self, other):    #less equal than
        return self.name <= other.name

student123 =m_student("김철수", 23) 

#자기자신과 비교용 클래스 메서드 사용
print(student123==student123)     #True
print(student123!=student123)     #False
print(student123>student123)     #False
print(student123>=student123)     #True
print(student123<student123)     #False
print(student123<=student123)     #True





#클래스 변수와 인스턴스 변수
"""
클래스 변수 : 모든 인스턴스가 공유하여 사용가능

인스턴스 변수 : 해당 인스턴스에서만 사용

상속(inheritance): 부모로부터 메소드, 속성을 모두 물려 받는 형태

메소드 오버라이딩(overriding): 기존에 만들어둔 메소드를 다시 정의할떄 사용됨
"""

# 예제 7-8
class Reg:
    reg_num=0    #아래에서 클래스 변수로 활동(전역변수와 비슷, 모든 인스턴스가 공유하면서 사용)
    
    def __init__(self,name):
        self.name=name
        Reg.reg_num+=1
    
    def __del__(self):
        Reg.reg_num-=1

student1=Reg("홍길동이")
student2=Reg("오태식이")

print(student1.name)    #클래스 변수 +1
print(student2.name)    #클래스 변수 +1
print(Reg.reg_num)    # 2출력됨
del (student1)     #클래스 변수 -1
print("삭제 진행후 클래스 변수의 상태: ", Reg.reg_num)    #1 출력된다



# 새로운 예제
class Calc:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    
    def add(self):
        result=self.first+self.second
        return result
    
    def mul(self):
        result=self.first*self.second
        return result
    
    def sub(self):
        result=self.first-self.second
        return result
    
    def div(self):
        result=self.first/self.second
        return result
    
Calc1=Calc(4,2)
print("두 수의 합", Calc.add())
print("두 수의 나눗셈", Calc.div())

class 상속받는Calc(Calc):   #클래스 상속받는 메서드 생성 완료
    pass


Calc2=상속받는Calc(6,2)
print("두 수의 합", Calc2.add())
print("두 수의 나눗셈", Calc2.div())
print("두 수의 곱", Calc2.mul())
print("두 수의 빼기", Calc2.sub())


class 상속받는Calc(Calc):    #기존에 있는 상속자 클래스에 메서드를 추가함(부모메서드+내메서드까지)
    def power(self):      #메소드 오버라이딩이다, 부모를 수정하지 않고도 이어서 사용이 가능하다는점을 기억
        result=self.first**self.second
        return result


Calc3=상속받는Calc(4,2)
print("제곱한 결과: ", Calc3.power())    #제곱한 결과

#d=Calc(4,0)   #d인스턴스
#print(d.div())     #4나누기 0이면 오류가 발생함



#                Self 키워드 탐구
"""
self는 클래스로부터 만들어진 인스턴스 그 자체를 의미함
인스턴스가 생성되면 self를 적용하여 클래스에서 정의된 속성과 행위(메소드)를 사용
"""

class UnderSelf:
    def meth1(self):
        print("python 1")

    def meth2():
        print("python 2")

s1 = UnderSelf()    #인스턴스 생성
s1.meth1()    #파이썬1 프린트
print("id(s1) = ", id(s1))    #s1인스턴스의 메모리 주소가 출력이 된다
#s1.meth2    #self 가 없어서 오류가 발생함

UnderSelf.meth2()
print("ID언더셀프 메소드2", id(UnderSelf.meth2)) #1342다시작성
