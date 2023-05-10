# https://www.acmicpc.net/problem/15312

import sys
from collections import deque
'''
print(ord('A'))   #65에 해당
print(ord('Z'))    #90에 해당
'''
my_dict={}

mapping=[3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
cnt=0
for _ in range(65,91):
    my_dict[chr(_)]=mapping[cnt]
    cnt+=1

# my_dict에 각 번호별 매핑 완료!

# 이제 앞,뒤의 번호를 더해서 %10 나머지 연산 해주면 끝이다.
A=list(sys.stdin.readline().strip())    # 종민이 이름
B=list(sys.stdin.readline().strip())    # 그녀 이름 받기 

arr=[]

for a,b in zip(A,B):
    arr.append(my_dict[a])
    arr.append(my_dict[b])
    
#print(arr, "시작 숫자 배열")

# 이제 숫자 들어갔으니, 길이가 2인 arr 배열이 완성될때 까지 반복문을 돌린다.

while(True):
    arr1=[]
    for i in range(len(arr)-1):
        arr1.append((arr[i]+arr[i+1])%10)   #앞숫자와 뒷숫자를 합친후 다른배열에 넣는 중이다.
    
    #print(arr1,'arr1의 현재 연산 상태')
    arr=arr1
    
    # 종료 조건
    if len(arr)==2:
        print(str(arr[0])+str(arr[1]))
        exit(0)
        
        
        

