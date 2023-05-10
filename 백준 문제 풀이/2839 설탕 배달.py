# 설탕 무계가 주어짐
# 5kg 3kg 설탕 봉지가 존재 이때 설탕봉투가 필요한 개수를 구하여라







































def sugar_bt(sugar):
    bag = 0
    while sugar >= 0 :
        if sugar % 5 == 0 :  # 5의 배수이면
            bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
            print(bag)
            break
        sugar -= 3  
        bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
    
    else:
        print(-1)
            


import sys

N=int(sys.stdin.readline())

sugar_bt(N)