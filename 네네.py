mlist1=[88.5,87.8,83.4,86.7,87.5,91.5,88.6,100.3,95.6,93.3,94.7,91.1,91.0,94.2,87.8,89.9,88.9,87.6,84.3,86.7]

mlist1.sort()
print("리스트 길이", len(mlist1))

count=0
for i in range(len(mlist1)):
    print(mlist1[i], end=" ")
    count+=1

    if count%10==0:
        count=0
        print()