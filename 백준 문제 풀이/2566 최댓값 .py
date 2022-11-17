#9*9=81개의 릴레이션(표)가 존재함
# 각 표의 내용물에 0~100 까지의 수가 들어 있고 가장 큰 값(최대값)을 가지는 칸의 최대값, 행,열을 반환하자
# 2차원 배열을 활용하자


























# 9*9의 2차원 배열을 탐색하는 함수를 만들자
def find_two_relation (relation):   #2차원 리스트가 들어오는 곳
    topLv=-1    #최대값의 왕좌(자주 바뀜)
    X,Y=-1,-1    #행좌표, 열좌표 저장하는 곳

    #1줄 1줄씩 탐색을 실시 해보자
    for colum in range(9):

        for row in range(9):
            if topLv<=relation[colum][row]:
                topLv=relation[colum][row]
                X,Y=colum,row

    return topLv,X,Y

import sys

relation=[list(map(int,sys.stdin.readline().strip().split())) for row in range(9)]
#2차원 배열을 한줄로 만드는 효율적인코드

#[print(relation[_]) for _ in range(9)] * 모든 2차원 배열을 출력하는 함수를 만듬
answer=list(find_two_relation(relation))
print(answer[0])
print(answer[1]+1,answer[2]+1)




















