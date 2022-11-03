def solution(scores):
    count=0
    for s in range(len(scores)):
        if scores[s]<=200:
            count+=1
    return count

scores=[100,200,300,400]
ret=solution(scores)
print(ret)