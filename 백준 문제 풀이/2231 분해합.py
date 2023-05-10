# 198 + 1+ 9 + 8 =216이 완성이 된다. 따라서 216의 생성자는 198이 된다 
# 이 과정을 역순으로 추적해서 만드는 경우의 수를 계산하면 된다. 모든 경우를 다 따져보도록 하자
#
#
#






















""" 방법1 permutations(순열) 활용법 단 시간초과는 무조건 뜬다고 생각"""

# 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 
import sys
from itertools import combinations
from itertools import permutations
# 생성자가 있는경우, 없는경우 둘다 존재한다.

def find_combination(N):
    arr=list(range(1,N+1))   #1 부터 N 까지의 정수가 담긴 리스트를 활용한다.
    
    for comb in permutations(arr,len(str(N))):     # 1자리수면 1개뽑기 2자리수면 2개 뽑기 N 자리수면 N개 뽑기를 실행한다.    
        m_str=''
        for i in comb:
            m_str+=str(i)
        if (int(m_str)+ sum(comb)) ==N:
            return (int(m_str))


N=int(sys.stdin.readline())    #N을 입력받는다.
print(find_combination(N))



"""방법2  map(문자열)을 통해 분리를 하는 방법"""
import sys

N= int(sys.stdin.readline())
answer=0
for i in range(1,N+1):
    A=list(map(int, str(i)))    #정수 i를 str로 변환후 하나씩 꺼내서 리스트와 한다  **핵심**  int 254이면 [2,5,4]의 정수가 담긴 배열을 만든다.
    if sum(A)+i==N:
        print(i)
        break
    elif i==N:    #생성자가 본인 하나일 경우 (한자리수만 존재 1,2,3,4,5,6,7,8,9)
        print(0)

