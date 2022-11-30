# for index_num, 실제값 in enumerate([1,2,3,44,5]):
#    print(index_num, 실제값)

# """
# 인덱스 번호들과 실제 값이 담긴 것

# """


# A,B = map(int, input().split())

# print(A)

# a,b=[100,200]    #자동으로 앞에 리스트 요소, 뒤의 리스트 요소를 나눈다

# print(a)
# print(type(b))

j=[1, 1, 0, 0, 1, 0, 1, 0, 0, 0]
print(enumerate(j))
print(list(enumerate(j)))
for i in reversed(list(enumerate(j))):     #이거 매우 유용함

   print(i)