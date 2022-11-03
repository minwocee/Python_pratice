def solution(price, money):
    answer =0
    msum=sum(price)
    answer=money-msum
    
    if answer<=0:
        return -1
    
    return answer

price=[2100,3200,2100,800]
money=10000
ret=solution(price,money)
print(ret)