#          22.10.10  딕셔너리(dictionary)정리
# 딕셔너리(dictionary)는 사전처럼 2개의 요소를 하나로 묶어서 표현된다.
# 중괄호{} 으로 묶어서 구성되며 키(key)와 값(Value)의 쌍으로 구성
# 형식: dictionary_name= {key1:value1, key2:value2, key3: value3...}
# 기존 생성한 딕셔너리에 key-value 추가하는법: dicname[key값]=value값    (인덱스[]괄호처럼 중괄호 임을 유의하자)
# 리스트나 튜플처럼 순차적(sequential)으로 해당 요소값을 구하지 않고 key를 거쳐서 value를 얻는다.
# 순서가 없으므로 인덱스 번호를 이용한 접근 불가, key를 이용해 접근해야 한다.
# key는 고유한 값이므로 중복되는 key의 값을 설정해두면 하나를 제외하고 중복된것 전부 무시됨(유일성)
# 딕셔너리 key는 유일 : 이미 존재하는 key값을 사용해서 한쌍의 key-value를 추가하면 기존에 있던 key-value를 덮어씌움
# 딕셔너리의  key는 변경이 불가 : 문자열(Strings), 숫자(Numbers), 튜플(Tuples)는 키(Dictionary key)로 활용가능(list는 불가)
# key =해당 사물함 잠금 열쇠, value =사물함 내의 내용물 이라고 생각

dic1={}    #빈 딕셔너리를 생성한다.(대괄호 임을 주의하자)
dic2=dict()    #이것도 빈 딕셔너리를 생성하는 법

dic1={"이름":"홍길동",  "나이":"999",   "학번": "19586984"}    #딕셔너리에 3개의 key-value 가 존재
dic2={"학번들":[1999,2000,20001]}    #딕셔너리의 value에 리스트가 들어갈수도 있다.
dic2["학생들의 나이"]=[12,34,56]    #dic2에 새로운 key값과 value를 추가하는 과정한다.

print(dic2)    #{'학번들': [1999, 2000, 20001], '학생들의 나이': [12, 34, 56]} 출력된다.
print(dic2["학번들"])    #딕셔너리 에서 "학번들"(key)와 연결된 value값을 호출한다.[1999, 2000, 20001] 출력됨

dic1["이름"]="김민준"    #이름의 value(홍길동-->김민준)이 교체가 된다.
print(dic1["이름"])    #김민준이 출력 된다.





#                               <딕셔너리의 함수와 메서드 활용>

# len(): len(dic_name)  ,  딕셔너리의 key개수를 반환한다.
# del(): del(dic_name[key값])  ,  입력한 key-value 쌍을 딕셔너리에서 삭제한다.
# pop(): dic_name.pop(key값)  ,  해당 key에담긴 value를 반환후 삭제한다.
# popitem(): dic_name.popitem()  ,  임의의 key-value를 반환후 삭제한다.(랜덤 반환후 삭제기능)
# keys(): dic_name.keys()  ,  해당 딕셔너리의 key값만 모아서 반환해준다.(무슨 키값이 있는지 모를떄 사용)
# values(): dic_name.values()  ,  해당 딕셔너리의 value값만 모아서 반환 해준다.(무슨 value가 담겨있는지 모를떄 사용)
# items(): dic_name.items()  ,  해당 딕셔너리의 key-value쌍을 모아서 튜플(tuple) 형태로 반환한다.
# clear(): dic_name.clear()  ,  해당 딕셔너리의 모든 key-value를 삭제하고 빈 딕셔너리를 생성
# get(): dic_name.get(key)  ,  해당 딕셔너리의 key에 담긴 value를 반환한다.(dic_name[key]와 같은 기능)
# in: key값 in dic_name  ,  해당 키가 딕셔너리 안에 존재하면 True 없으면 False 를 반환한다.
# update(): dic_name.update({key1:value1, key2:value2....})  ,  한번에 여러개의 key-value 조합을 넣고싶을때 가능



#del
dic1={"학생1":"김민수", "학생2":"홍길동", "학생3":"나문희"}
del(dic1["학생2"])    #"학생2":"홍길동" 이 딕셔너리에서 삭제가 된다.
print(dic1)    #{'학생1': '김민수', '학생3': '나문희'} 출력

#pop
dic1={"학생1":"김민수", "학생2":"홍길동", "학생3":"나문희"}
print(dic1.pop("학생1"))    #김민수가 출력되고 "학생1":"김민수"가 삭제된다.
print(dic1)    #{'학생2': '홍길동', '학생3': '나문희'}

#popitem
dic1={"학생1":"김민수", "학생2":"홍길동", "학생3":"나문희", "학생4":"이순재"}
for i in range(len(dic1)):    #무작위 딕셔너리의 value가 출력되고 해당하는key-value가 삭제된다.
    print(dic1.popitem())    #하지만 파이썬 3.8버전에서는 뒤에서 부터 반환후 삭제로 변경된다(내가 그렇다.)

#keys
dic1={"학생1":"김민수", "학생2":"홍길동", "학생3":"나문희", "학생4":"이순재"}
print(dic1.keys())    #dict_keys(['학생1', '학생2', '학생3', '학생4']) 출력

mlist=list(dic1.keys())    #만약 이렇게 쓰면 key값이 전부 리스트에 담기는걸 가능(활용이 가능)
print(mlist)

#values
dic1={"학생1":"김민수", "학생2":"홍길동", "학생3":"나문희", "학생4":"이순재"}
print(dic1.values())     #dict_values(['김민수', '홍길동', '나문희', '이순재']) 출력된다.(value만 출력)

#items
dic1={"학생1":"김민수", "학생2":"홍길동", "학생3":"나문희", "학생4":"이순재"}
print(dic1.items())    
    #dict_items([('학생1', '김민수'), ('학생2', '홍길동'), ('학생3', '나문희'), ('학생4', '이순재')])
    # 튜플로 묶여서 반환된다.

mlist1=list(dic1.items())
print(mlist1)    #[('학생1', '김민수'), ('학생2', '홍길동'), ('학생3', '나문희'), ('학생4', '이순재')]
print(type(mlist))    #<class 'list'>
print("------------------------------------")

print(mlist[0],mlist[1])    #학생1 학생2 (key 값만 출력이 되는 현상 발생)
    #어떻게 해야 value까지 리스트화 할때 표현이 가능 할까? ()
print(list(mlist[0]))    #['학', '생', '1'] 으로 한글자로 분해가 가능 (이거 나중에 응용 가능한 예시가 떠오른다.)


#len()
dic1={"학생1":"김민수", "학생2":"홍길동", "학생3":"나문희", "학생4":"이순재"}
print(len(dic1))    #딕셔너리의 길이(key개수)를 반환한다. (4 반환 된다.)

#clear
dic1={"학생1":"김민수", "학생2":"홍길동", "학생3":"나문희", "학생4":"이순재"}
dic1.clear()
print(dic1)    #빈리스트가 출력 된다.

#get
dic1={"학생1":"김민수", "학생2":"홍길동", "학생3":"나문희", "학생4":"이순재"}
print(dic1.get("학생3"))    #나문희 출력된다.
print(dic1["학생3"])    #위와 같은 기능

print(dic1.get("학생7"))    #key가없으면 get()함수 사용시 None반환된다.
#print(dic1["학생8"]) KeyError: '학생8' 발생

#update
dic1={"학생1":"김민수", "학생2":"홍길동", "학생3":"나문희", "학생4":"이순재"}
dic1.update({"학생1":"문상훈", "학생2":"김유정", "학생5":"나미춘"})    #학생1,학생2의 value가 수정, 학생5:나미춘 추가
print(dic1)

# #알아두면 좋은좀더 가독성 좋은 ppint 사용법
# from pprint import pprint as pp
# dic1={"학생1":"김민수", "학생2":"홍길동", "학생3":"나문희", "학생4":"이순재"}
# pp(dic1)    #{'학생1': '김민수', '학생2': '홍길동', '학생3': '나문희', '학생4': '이순재'}




#                                         <집합(set)>

# 집합은 키만 모아 놓은 딕셔너리의 특수한 형태로 중복을 허용하지 않고 순서가 없는게 특징(나중에 리스트 중복제거시에도 응용 가능)
# 집합은 순서가 없으므로 인덱싱으로 값을 얻을 수 없으므로 저장된 값을 인덱싱으로 접근하려면 
# 리스트나 튜플로 변환한 후 접근해야 함 *****list(집합), tuple(집합) 을 사용하라는 말씀*****
# 집합은 중괄호{}안에 저장하고 콤마(,) 으로 구분 한다.
# 형식: set_name={key1, key2, key3.....}     (키값만 존재, 유일성있다.)
# 집합은 리스트, 튜플이나 딕셔너리와는 다르게 []로 특정 요소만출력할 수는 없고
# 만약 이렇게 사용할 때는 타입오류 TypeError: 'set'object is not subscriptable 가 발생






#                                    <집합(set)의 메서드와 함수>

# add(): set_name.add(x)  ,  이미 존재하는 해당 집합에 key x를 추가한다.
# update(): set_name.update([x,y,z])  ,  해당 집합에 key(x, y, z)를 한번에 추가한다.
# remove(): set_name.remove(x)  ,  해당 집합에서 key x를 삭제한다.(만약 x가 집합key중에 없으면 KeyError 발생)
# discard(): set_name.discard(x)  ,  remove()와 같은 기능 이지만 만약 x가 집합key중에 없어도 KeyError 발생하지 않는다.
# clear(): set_name.clear()  ,  해당 집합의 모든 요소를 삭제한다.
# in: key값 in set_name  ,  해당 집합에 key값이 있는지 검사하고 있으면 True ,없으면  False 가 반환된다.
# set(): set([1,1,2,2,3,3])-->{1,2,3} 완성(중복값이 제거, key는 유일하기 떄문)  ,  다른 자료구조(list,tuple)을 집합(set)으로 변환

#set
list1=["가", "나", "가","나", "다"]
print(set(list1))    #{'나', '다', '가'} 출력 (중복된 요소가 삭제)

#add
set1={1,2,3,4,5}
set1.add(6)
print(set1)    #{1, 2, 3, 4, 5, 6} 출력 (key:6 이 추가각 된다.)

#update
set1={1,2,3,4,5}
set1.update([6,7,8])
print(set1)    #{1, 2, 3, 4, 5, 6, 7, 8} 출력  (key값 6,7,8 동시에 추가가능)

#remove
set1={1,2,3,4,5}
set1.remove(5)
print(set1)    #{1, 2, 3, 4} 출력 (key 값 5 삭제 됨)

#discard
set1={1,2,3,4,5}
set1.discard(3)     #key=3 삭제 완료
set1.discard(6)    #remove는 오류가 발생하지만 discard는 오류 발생이 없다.
print(set1)    #{1, 2, 4, 5} 출력됨

#clear
set1={1,2,3,4,5}
set1.clear()    #집합 key를 전부 삭제후 빈 집합으로 만들어 준다.
print(set1)    

#in
set1={1,2,3,4,5}
if 5 in set1:    #5가 set1에 들어 있으면 참 없으면 거짓 반환.
    print("key=5는 set(집합)안에 존재 합니다.")

#set
set1=set("abcd,abcd,abcd")    #문자열도 분해하고 중복을 제거해서 집합에 담는게 가능하다.
print(set1)    #{',', 'a', 'd', 'b', 'c'} 출력

#range
set1=set(range(10))
print(set1)    #연속적인 숫자 {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} 출력 된다.



#                                   <집합의 연산자 활용>          |(쉬프트+'역슬래시'), &, -, ^
# |: 합집합 연산자로  set.union(집합1, 집합2)으로도 가능
# &: 교집합 연산자로 set.intersection(집합1, 집합2)으로도 가능
# -: 차집합 연산자로 set.difference(집합1, 집합2)으로도 가능
# ^: XOR 연산자로 set.symmetric_difference(집합1, 집합2)으로도 가능 하다.

set1={1,2,3,4,5}
set2={3,4,5,6,7,}

print(set1|set2)    #{1, 2, 3, 4, 5, 6, 7} 출력 된다.  (합집합)
print(set.union(set1,set2))

print(set1&set2)    #{3, 4, 5} 출력 된다.  (교집합)
print(set.intersection(set1, set2))

print(set1-set2)    #{1, 2} 출력 된다.  (차집합)
print(set.difference(set1,set2))

print(set1^set2)    #{1, 2, 6, 7} 출력 된다.  (XOR 집합, 두집합의 겹치지 않는 부분을 출력)
print(set.symmetric_difference(set1,set2))