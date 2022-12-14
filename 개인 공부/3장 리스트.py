#파이썬의 리스트에 대해서 공부 해보자 2022.08.28 작성

a1=list()    #이것도 빈 리스트를 생성하는 방법
a = []    #빈 리스트 생성
b = [1, 2, 3]    #정수형 리스트를 생성
c = ['Life', 'is', 'too', 'short']    #문자열형 리스트 생성
d = [1, 2, 'Life', 'is']    #다양한 자료형이 존재하는 리스트 생성
e = [1, 2, ['Life', 'is']]    #리스트속의 리스트를 생성(중복 리스트)

#리스트의 인덱싱과 슬라이싱
print(b[0])    #리스트에서의 첫번쨰 요소를 출력(반드시 인덱스는 0부터 시작 한다는것을 인지하자)

print(b[0]+b[1])    #1+2=3 출력된다.

print(c[-1])    #리스트의 가장 마지막 요소인 'short'가 출력 된다.

print(e[2])    #중복 리스트임으로 ['Life', 'is']가 출력이 된다. 그렇다면 중복리스트의 내부 요소를 끄집어 낼수 있을까?

print(e[2][0])    #Life 가 출력이 된다.(중복리스트를 타겟 이후 첫번째 요소를 출력)

print(e[2][-1])    #is 가 출력이 된다.(인덱스번호 -1을 사용해 마지막 요소를 설정 해준다.)

'''삼중리스트도 위와 같은 방식으로 사용이 가능하지만 복잡해서 추천하지는 않는다.'''

#리스트의 슬라이싱
k=[1,2,3,4,5]
print(k[0:2])     #[1,2]가 출력이 된다.(인덱스 0번과 1번) 2번은 해당하지 않는다.
k1="12345"
print(k1[0:2])     #12가 출력된다. 문자열을 슬라이싱 할때와 같은 방식이다.

""" list[a:b] 일때 a<= ~~ b< 임을 기억하자(쉽게말해 b번째 인덱스는 포함 하지 않는다!!!)"""

print(k[2:])    #[3,4,5]출력된다.
print(k[:2])    #[1,2]출력된다. (k[2]='3'는 포함이 되지 않는다.)

#중첩리스트에서의 슬라이싱 방법
a0=[1,2,['aa','bb','cc','dd'],3,4,5]
print(a0[2:])    #[[aa,bb,cc,dd],3,4,5]
print(a0[2][1:])    #bb,cc,dd


#리스트의 연산자 활용(+,*,len()함수)
a=[1,2,3]; b=[4,5,6]
print(a+b)    #[1,2,3,4,5,6] 출력됨(a리스트 뒤에 b리스트가 붙는다.)
print(a * 3)    #[1,2,3,  1,2,3,  1,2,3,] 출력 된다.

print(str(a[2])+"hi")    #형변환을 통해서 출력

#리스트에서 수정과 삭제
a=[1,2,3,4,5]
a[0]=10    #첫번째 요소를 수정함
print(a)    #[10,2,3,4,5]가 출력이 된다.

del a[0]    #del을 사용해 첫번째 요소를 삭제
print(a)    #[2,3,4,5] 가 출력이 된다.(첫번쨰 요소인 10이 사라짐)


#리스트에서 사용 가능한 편리한 함수들 모음
#<< append(), sort(), reverse(), index(), insert(), remove(), pop(), count(), extend() >>
a=[1,2,3]
a.append(4)     #정수 4를 a리스트의 끝에 추가한다.(append()함수를 사용)
a.append(['a','b'])    #리스트에 리스트를 추가한다(어떤것도 가능하다.)

b=[1,5,6,7,3,4]
b.sort()    #오름차순 순으로 순서대로 정렬한다.
print(b)

c=['w','a','c','f']
c.sort()    #알파벳 문자도 정렬이 가능하다.
print(c)

a=[1,2,3,4,5,6,7,8,9,10]
a.reverse()    #리스트를 거꾸로 출력해준다.
print(a)

a=[1,2,3,4,5]
print(a.index(3))    #해당 요소의 인덱스 번호를 출력 (지금같은 경우는 2 가 출력 된다.)

a.insert(0,4)    #인덱스[0]에 정수4를 교체한다. (a[0]의 위치에 정수 4를 삽입하라와 같음)

a.remove(3)    #요소 3을 삭제한다.(여러개 존재시 가장 앞의것 하나를 지운다.)

a.pop()    #리스트 a의 마지막 요소를 반환후(출력) 삭제한다.(자료구조에서도 나왔음) 끄집어 낸다고 생각하자

a.pop(1)    #리스트 a의 인덱스[1]번(두번째 항목을 의미)을 반환후(출력) 삭제한다.

a.count(4)    #리스트 a의 원소중 정수 4가 몇번 들어있는지 출력해줌(1번있으면 1, 2번있으면 2 반환)

j=[1,2,3]
p=[4,5]
j.extend(p)    #리스트 j의 끝에 리스트 p를 붙인다. 반드시 extend에는 리스트가 들어와야 한다. j+=[4,5] 와 동일함


#학생들의 점수를 입력받고 출력하는 프로그램을 만들어 보기
scorelist=[]
while True:
        print("학생들의 점수를 입력 하세요:  ")
        scorelist.append(input())
        
        if scorelist[-1]=='멈춰':
            del scorelist[-1]
            break

scorelist.sort()    #오름차순 순으로 정렬함
print(f"최고 득점자의 점수는 {scorelist[-1]} 입니다."  )
print(f"최저 득점자의 점수는 {scorelist[0]} 입니다." )
