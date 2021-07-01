num=[ ]
max=0
for i in range(0,9):
    a=input()
    a=int(a)
    num.append(a)
    if num[i]>max:
        max=num[i]
        maxnum=i
print("%d\n%d"%(max,maxnum+1))