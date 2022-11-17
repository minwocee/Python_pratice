# 100*100 사이즈의 도화지에 검은색 10*10 크기의 색종이를 붙여서 검은색 색종이의 크기를 
#측정해보자

#본인은 이걸 집합의 차집합으로 풀었다


























#11,12,13,14,15,16
#12345678910


# 검은색 도화지의 면적을 집합으로 만들어 구현
def black_papper(X,Y):   #(3,7) 경우
    bl_list=[]
    for y in range(Y,Y+10):    #7
        for x in range(X,X+10):    #3
            bl_list.append(y*100+x)    #해당 블록을리스트에넣음

    return bl_list













import sys

N=int(sys.stdin.readline().strip())
white_papper=set(list(range(10000)))    #0~9999 까지의 집합 생성


for i in range(N):
    X,Y=map(int, sys.stdin.readline().strip().split())
    white_papper=white_papper-set(black_papper(X,Y))

print(10000-len(white_papper))


