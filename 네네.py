mlist=list(range(1,10001))    #1~10000까지의 정수를 입력
Total=list(range(1,10001))

def devide(x):#각 자리수를 분해하는 함수를 만들기
    if x>=1000:    #천의자리 분해
        m1000=x//1000    #9903에서 9를 가져옴
        m100=(x-(m1000*1000))//100    #903에서 9를 가져옴
        m10=(x-m1000*1000-m100*100)//10    #0이 들어감
        m1=(x-m1000*1000-m100*100-m10*10)    #3이 들어감
        return x+m1000+m100+m10+m1  #9903+9+9+0+3=9924는 예외
    
    elif x>=100:    #백의자리 분해
        m100=x//100
        m10=(x-m100*100)//10
        m1=(x-m100*100-m10*10)
        return x+m100+m10+m1
    
    elif x>=10:    #십의자리 분해
        m10=x//10
        m1=x-m10*10
        return x+m10+m1
    elif x>=1:
        return x+x


for i in range(10000):
        try:
            if(devide(mlist[i])  in mlist):
                Total.remove(devide(mlist[i]))
        except ValueError:
            continue

print(1)

for i in mlist:
    try:
        print(Total[i])
    except IndexError:
        continue