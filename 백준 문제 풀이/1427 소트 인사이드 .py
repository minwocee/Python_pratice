#  정수를 입력 받고 그 정수 안의 숫자들을 내림차순으로 바꿔서 다시 출력하는 문제












































import sys

N= int(sys.stdin.readline().strip())

mlist=list(str(N))

mlist.sort()
mlist.reverse()
[print(i,end="") for i in mlist]