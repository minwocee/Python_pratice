

"""추가적인 팁 (파이썬에서 모든 경우의 수를 for문을 사용하지 않고 바로 만들어주는 함수 사용법)"""
from itertools import permutations     #순열을 의미한다 (순서가 존재한다)
from itertools import combinations      #조합을 의미한다 (순서가 없다 ABC CBA 같은걸로 본다)

Table=['A','B','C']
print(list(map(''.join, permutations(Table))))    #원소가 3개 사용하는 순열 리스트
print(list(map(''.join, permutations(Table,2))))   #원소가 2개 사용하는 모든 경우의수 리스트
print(list(map(''.join, permutations(Table,1))))   #원소가 1개 사용하는 모든 경우의수 리스트

print(list(map(''.join, combinations(Table,3))))    #원소가 3개 사용하는 모든 경우의수 리스트
print(list(map(''.join, combinations(Table,2))))   #원소가 2개 사용하는 모든 경우의수 리스트
print(list(map(''.join, combinations(Table,1))))   #원소가 1개 사용하는 모든 경우의수 리스트