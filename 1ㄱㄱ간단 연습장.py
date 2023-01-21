'''
from heapq import heappush, heappop, heapify, nlargest, nsmallest


print(nsmallest(3,[1,2,3,4,5,6])[2])


mlis=[1,2,3,4,5]

while mlis:    #mlis에 값이 존재하는한 무한 반복 한다.
    print(mlis.pop())
'''

mydic={}

mydic.get('hello',3)

print(mydic.get('hello',3))    #해당 키가 존재하지않으면, 3을 반환한다.

print(mydic)